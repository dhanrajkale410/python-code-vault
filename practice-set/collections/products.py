# Given a dictionary of products and their prices, find the product with the highest price.

product_prices = {
    "Laptop": 1200,
    "Mouse": 50,
    "Keyboard": 150,
    "Monitor": 300
}

highest_price_product = max(product_prices, key=product_prices.get)
print(highest_price_product)                # Laptop