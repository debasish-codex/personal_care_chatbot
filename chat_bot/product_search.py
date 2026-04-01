# product_search.py

import csv

def search_products(user_input):

    results = []

    # 🔹 Step 1: Preprocess input
    text = user_input.lower()
    text = text.strip()

    # 🔹 Step 2: Extract price condition (e.g., under 300)
    price_limit = None

    words = text.split()

    for i in range(len(words)):
        word = words[i]

        if word == "under" or word == "below":
            if i + 1 < len(words):
                next_word = words[i + 1]

                if next_word.isdigit():
                    price_limit = int(next_word)

    # 🔹 Step 3: Open CSV file
    with open("data/products.csv", mode="r", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        # 🔹 Step 4: Loop through rows
        for row in reader:

            brand = row["Brand"].lower()
            product_name = row["Product Name"].lower()
            price = row["Current Price"]

            # Convert price to int
            try:
                price = int(price)
            except:
                continue

            match = True

            # 🔹 Step 5: Check price condition
            if price_limit is not None:
                if price >= price_limit:
                    match = False

            # 🔹 Step 6: Check brand match
            brand_match = False

            if brand in text:
                brand_match = True

            # If user mentioned brand but it doesn't match
            if brand_match == False:
                for word in words:
                    if word in brand:
                        brand_match = True
                        break

            # 🔹 Step 7: Final condition
            if price_limit is not None:
                # If price filter exists → ignore brand mismatch
                pass
            else:
                if brand_match == False:
                    match = False

            # 🔹 Step 8: Add to results
            if match == True:
                results.append(row)

    # 🔹 Step 9: Return results
    return results