from fetch import fetch_data
import processing as p


def main():
    print("Starting Chicago crime data analysis...")

    # Step 1: Fetch data
    df = fetch_data()

    # Step 2: Run processing & export routines
    p.export_fbi_code_counts(df)
    p.export_month_year_counts(df)
    p.export_district_counts(df)
    p.export_primary_type_counts(df)
    p.export_time_range_counts(df)
    p.export_arrest_summary(df)
    p.export_ward_counts(df)

    print("All exports completed successfully.")


if __name__ == "__main__":
    main()