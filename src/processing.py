import pandas as pd
from calendar import month_name
from pathlib import Path

# Output directory
OUTPUT_DIR = Path("data")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def export_fbi_code_counts(df):
    df = df.dropna(subset=['date', 'fbi_code']).copy()
    df['year'] = df['date'].dt.year
    result = df.groupby(['fbi_code', 'year']).size().reset_index(name='record_count')
    result.to_csv(OUTPUT_DIR / "fbi_code_counts_2010_2019.csv", index=False)
    print(f"✅ Exported FBI code counts: {len(result)} rows")


def export_month_year_counts(df):
    df = df.dropna(subset=['date']).copy()
    df['month'] = df['date'].dt.month_name()
    df['year'] = df['date'].dt.year
    result = df.groupby(['month', 'year']).size().reset_index(name='count')

    # Ensure calendar order
    month_order = list(month_name)[1:]
    result['month'] = pd.Categorical(result['month'], categories=month_order, ordered=True)
    result = result.sort_values(['year', 'month'])

    result.to_csv(OUTPUT_DIR / "month_year_counts_2010_2019.csv", index=False)
    print(f"✅ Exported month-year counts: {len(result)} rows")


def export_district_counts(df):
    result = df['district'].value_counts(dropna=True).reset_index()
    result.columns = ['district', 'count']
    result = result.sort_values(by='count', ascending=False)
    result.to_csv(OUTPUT_DIR / "police_district_counts.csv", index=False)
    print(f"✅ Exported police district counts: {len(result)} rows")


def export_primary_type_counts(df):
    result = df['primary_type'].value_counts().reset_index()
    result.columns = ['primary_type', 'count']
    top_11 = result.head(11)
    top_11.to_csv(OUTPUT_DIR / "top_11_primary_types.csv", index=False)
    print(f"✅ Exported top 11 primary types: {len(top_11)} rows")


def export_time_range_counts(df):
    df = df.dropna(subset=['date']).copy()
    df['hour'] = df['date'].dt.hour
    df['year'] = df['date'].dt.year

    def get_time_range(hour):
        if 4 <= hour < 7:
            return "4am–7am"
        elif 7 <= hour < 12:
            return "7am–12pm"
        elif 12 <= hour < 17:
            return "12pm–5pm"
        elif 18 <= hour < 21:
            return "6pm–9pm"
        elif 21 <= hour <= 23:
            return "9pm–12am"
        else:
            return "12am–4am"

    df['time_range'] = df['hour'].apply(get_time_range)

    result = df.groupby(['time_range', 'year']).size().reset_index(name='count')
    time_order = ["12am–4am", "4am–7am", "7am–12pm", "12pm–5pm", "6pm–9pm", "9pm–12am"]
    result['time_range'] = pd.Categorical(result['time_range'], categories=time_order, ordered=True)
    result = result.sort_values(['year', 'time_range'])

    result.to_csv(OUTPUT_DIR / "time_range_counts_2010_2019.csv", index=False)
    print(f"✅ Exported time range counts: {len(result)} rows")


def export_arrest_summary(df):
    df = df.copy()
    df['year'] = df['date'].dt.year
    df = df[df['year'].between(2010, 2019)]

    result = df.groupby(['year', 'arrest']).size().unstack(fill_value=0)
    result = result.rename(columns={True: 'arrest_true', False: 'arrest_false'})
    result['total'] = result['arrest_true'] + result['arrest_false']
    result = result.reset_index()

    result.to_csv(OUTPUT_DIR / "arrest_summary_2010_2019.csv", index=False)
    print(f"✅ Exported arrest summary: {len(result)} rows")


def export_ward_counts(df):
    df = df.dropna(subset=['date', 'ward']).copy()
    df['ward'] = pd.to_numeric(df['ward'], errors='coerce')
    df = df[df['date'].dt.year.between(2010, 2019)]

    result = df['ward'].value_counts().sort_index().reset_index()
    result.columns = ['ward', 'record_count']
    result.to_csv(OUTPUT_DIR / "ward_record_counts_2010_2019.csv", index=False)
    print(f"✅ Exported ward record counts: {len(result)} rows")