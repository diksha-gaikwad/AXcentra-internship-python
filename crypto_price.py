import requests

def get_crypto_price():
    coin = input("Enter cryptocurrency name (bitcoin, ethereum): ")
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"

    response = requests.get(url)
    data = response.json()

    if coin in data:
        print(f"{coin.capitalize()} price (USD):", data[coin]["usd"])
    else:
        print("Invalid cryptocurrency name!")

if __name__ == "__main__":
    get_crypto_price()
