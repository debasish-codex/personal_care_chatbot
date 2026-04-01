# intent_detector.py

def detect_intent(user_input):

    # 🔹 Step 1: Preprocess input
    text = user_input.lower()
    text = text.strip()

    # 🔹 Step 2: Define keyword lists
    support_keywords = ["return", "refund", "replace", "offer", "discount"]

    general_keywords = ["benefit", "why", "how", "use", "advantages"]

    product_keywords = ["lipstick", "face wash", "cream", "price", "under", "below", "above"]

    brand_keywords = ["elle 18", "mars", "coloressence"]

    # 🔹 Step 3: Check Support Intent (Highest Priority)
    support_found = False

    for word in support_keywords:
        if word in text:
            support_found = True
            break

    if support_found == True:
        return "support"

    # 🔹 Step 4: Check Product Intent
    product_found = False

    # Check product keywords
    for word in product_keywords:
        if word in text:
            product_found = True
            break

    # Check brand keywords
    if product_found == False:
        for brand in brand_keywords:
            if brand in text:
                product_found = True
                break

    # Check numbers (price related)
    if product_found == False:
        for char in text:
            if char.isdigit():
                product_found = True
                break

    if product_found == True:
        return "product"

    # 🔹 Step 5: Check General Intent
    general_found = False

    for word in general_keywords:
        if word in text:
            general_found = True
            break

    if general_found == True:
        return "general"

    # 🔹 Step 6: Check Unknown
    words = text.split()

    if len(words) < 2:
        return "unknown"

    # 🔹 Default
    return "general"