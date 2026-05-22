from extract import scrape_main
from load import save_to_csv, save_to_postgresql
from transform import transform_data


def main():
    """Main ETL Pipeline."""

    print("Memulai proses Extract...")
    raw_data = scrape_main()

    if not raw_data:
        print("Tidak ada data yang berhasil diambil")
        return

    print("Memulai proses Transform...")
    clean_data = transform_data(raw_data)

    if clean_data.empty:
        print("Transformasi data gagal")
        return

    print("Memulai proses Load CSV...")
    save_to_csv(clean_data)

    print("Memulai proses Load PostgreSQL...")
    save_to_postgresql(clean_data)

    print("ETL Pipeline berhasil dijalankan")


if __name__ == "__main__":
    main()