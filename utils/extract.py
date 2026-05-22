import time

        rating = card.find("p", class_="rating").text.strip()

        colors = card.find("p", class_="colors").text.strip()

        size = card.find("p", class_="size").text.strip()

        gender = card.find("p", class_="gender").text.strip()

        product = {
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Colors": colors,
            "Size": size,
            "Gender": gender,
            "timestamp": timestamp,
        }

        return product

    except AttributeError as e:
        print(f"Error extracting product: {e}")
        return None


def scrape_main(start_page=1, end_page=50, delay=1):
    """Fungsi utama scraping seluruh halaman website."""
    products = []

    try:
        for page in range(start_page, end_page + 1):
            url = BASE_URL.format(page)
            print(f"Scraping page: {url}")

            content = fetch_content(url)

            if not content:
                continue

            soup = BeautifulSoup(content, "html.parser")

            product_cards = soup.find_all("div", class_="collection-card")

            timestamp = datetime.now()

            for card in product_cards:
                product = extract_product(card, timestamp)

                if product:
                    products.append(product)

            time.sleep(delay)

        return products

    except Exception as e:
        print(f"An error occurred during scraping: {e}")
        return []