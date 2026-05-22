import pandas as pd
        df = pd.DataFrame(data)

        # Hapus nilai null
        df = df.dropna()

        # Hapus duplicate
        df = df.drop_duplicates()

        # Hapus invalid product
        df = df[df["Title"] != "Unknown Product"]

        # Cleaning Price
        df["Price"] = (
            df["Price"]
            .replace(r"[^\d.]", "", regex=True)
            .astype(float)
            * EXCHANGE_RATE
        )

        # Cleaning Rating
        df["Rating"] = (
            df["Rating"]
            .str.extract(r"(\d+\.?\d*)")
            .astype(float)
        )

        # Cleaning Colors
        df["Colors"] = (
            df["Colors"]
            .str.extract(r"(\d+)")
            .astype(int)
        )

        # Cleaning Size
        df["Size"] = (
            df["Size"]
            .str.replace("Size:", "", regex=False)
            .str.strip()
        )

        # Cleaning Gender
        df["Gender"] = (
            df["Gender"]
            .str.replace("Gender:", "", regex=False)
            .str.strip()
        )

        # Konversi timestamp
        df["timestamp"] = pd.to_datetime(df["timestamp"])

        # Reset index
        df = df.reset_index(drop=True)

        return df

    except Exception as e:
        print(f"Error during transformation process: {e}")
        return pd.DataFrame()