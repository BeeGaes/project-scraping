from sqlalchemy import create_engine


CSV_PATH = "products.csv"

DB_URL = (
    "postgresql+psycopg2://developer:supersecretpassword"
    "@172.19.192.1:5432/fashiondb"
)


def save_to_csv(dataframe, file_path=CSV_PATH):
    """Menyimpan data ke CSV."""

    try:
        dataframe.to_csv(file_path, index=False)
        print(f"Data berhasil disimpan ke CSV: {file_path}")

    except Exception as e:
        print(f"Error saving CSV: {e}")


def save_to_postgresql(dataframe, db_url=DB_URL):
    """Menyimpan data ke PostgreSQL."""

    try:
        engine = create_engine(db_url)

        with engine.connect() as connection:
            dataframe.to_sql(
                "fashion_products",
                con=connection,
                if_exists="replace",
                index=False,
            )

        print("Data berhasil disimpan ke PostgreSQL")

    except Exception as e:
        print(f"Error saving to PostgreSQL: {e}")