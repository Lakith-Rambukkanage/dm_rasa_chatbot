from dummy_data.dummy_data import products_list


def product_search(product_category, product_name, size, colour, material, brand):

    # query
    query_vector = {
        "product_category": product_category,
        "product_name": product_name,
        "size": size,
        "colour": colour,
        "material": material,
        "brand": brand,
    }

    # products list
    products = products_list

    # to track top 3 scores
    score_list = [0, 0, 0]  # top 3 items
    response_product_list = []

    # score each item with weight
    for product in products:
        score = 0
        if product["product_category"] == query_vector["product_category"]:
            score += 3  # most weight
        if product["product_name"] == query_vector["product_name"]:
            score += 2  # more weight
        if product["size"] == query_vector["size"]:
            score += 1
        if product["colour"] == query_vector["colour"]:
            score += 1
        if product["material"] == query_vector["material"]:
            score += 1
        if product["brand"] == query_vector["brand"]:
            score += 1

        if score > min(score_list):
            score_list[score_list.index(min(score_list))] = score
            response_product_list.append(product)

            if len(response_product_list) > 3:  # max 3
                response_product_list.pop(0)

    # print(score_list)
    # print(response_product_list)

    return response_product_list


# product_search("පිරිමි ඇඳුම්", None, None, None, None, None)


def format_string(product):
    product_string = "\n"
    product_string += "නිෂ්පාදන කාණ්ඩය : " + product["product_category"] + "\n"
    product_string += "නිෂ්පාදන නාමය : " + product["product_name"] + "\n"
    product_string += "ප්‍රමාණය : " + product["size"] + "\n"
    product_string += "පාට : " + product["colour"] + "\n"
    product_string += "අමුද්‍රව්‍ය : " + product["material"] + "\n"
    product_string += "වෙළඳනාමය : " + product["brand"] + "\n"
    product_string += "මිල : " + product["price"] + "\n"
    product_string += "හඳුනාගැනීමේ කේතය : " + product["sku"] + "\n"

    return product_string
