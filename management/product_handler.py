import menu
import collections

product_list = menu.products


def get_product_by_id(id):
    if type(id) != int:
        raise TypeError("product id must be an int")
    objeto = {}

    try:
        for product in product_list:
            if product["_id"] == id:
                objeto = product
        return objeto
    except AssertionError:
        return objeto


def get_products_by_type(category):
    print(type(category))
    if type(category) != str:
        raise TypeError("product type must be a str")
    new_list = []
    for product in product_list:
        if product["type"] == category:
            new_list.append(product)
    return new_list


def add_product(menu, **item):
    bigger_id = 0
    for product in menu:
        if product["_id"] > bigger_id:
            bigger_id = product["_id"]
    bigger_id += 1
    item["_id"] = bigger_id
    menu.append(item)
    return item


def menu_report():
    lenght = len(product_list)
    sum_of_items = 0
    count = collections.Counter()
    for product in product_list:
        sum_of_items += product["price"]
        count[product["type"]] += 1
    media = sum_of_items / lenght
    product_count = f"Products Count: {lenght}"
    price_mid = f"Average Price: ${round(media, 2)}"
    common = count.most_common(1)[0][0]
    common_type = f"Most Common Type: {common}"
    return (f"{product_count} - {price_mid} - {common_type}")
