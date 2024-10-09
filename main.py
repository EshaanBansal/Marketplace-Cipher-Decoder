def decode_prices(encoded_prices, key):
    decoded_prices = []
    for price in encoded_prices:
        decoded_price = price ^ key
        decoded_prices.append(decoded_price)
    return decoded_prices
