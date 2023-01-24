import menu

product_list = menu.products


def calculate_tab(table):
    tab = 0
    for item in table:
        for product in product_list:
            if item["_id"] == product["_id"]:
                tab += (product["price"] * item["amount"])
    return {"subtotal": f"${round(tab, 2)}"}
