import requests

def parse(card_name):
    url_template = "https://catalog.onliner.by/sdapi/catalog.api/search/videocard?desktop_gpu[0]={0}&desktop_gpu[operation]=union"
    url = url_template.format(card_name)

    r = requests.get(url)
    products = r.json()["products"]

    return [{"name": product["extended_name"],
    "price": float(product["prices"]["price_min"]["amount"])} for product in products if product["prices"] != None]
    
def take_top_prices(products):
    def get_price(product):
        return product["price"]
    products.sort(key = get_price)
    return products[:5]

def format_message(products):
    return "\n".join([f"\"{product['name']}\": {product['price']} BYN" for product in products])

def get_prices(card_name):
    try:
        prod = parse(card_name)
        prod_sort = take_top_prices(prod)
        return format_message(prod_sort)
    except Exception:
      return "Введите правильное наименование видеокарты. Например: 'gtx1050ti'"

