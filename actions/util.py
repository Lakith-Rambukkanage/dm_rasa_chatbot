def format_prod_string(product):
    product_string = "\n"
    product_string += "නිෂ්පාදන කාණ්ඩය : " + product["product_category"] + "\n"
    product_string += "නිෂ්පාදන නාමය : " + product["product_name"] + "\n"
    product_string += "ප්‍රමාණය : " + product["size"] + "\n"
    product_string += "පාට : " + product["colour"] + "\n"
    product_string += "අමුද්‍රව්‍ය : " + product["material"] + "\n"
    product_string += "වෙළඳනාමය : " + product["brand"] + "\n"
    product_string += "මිල : " + str(product["price"]) + "\n"
    product_string += "හඳුනාගැනීමේ කේතය : " + product["sku"] + "\n"

    return product_string

def query_to_string(query_vector):
    q_string = "විමසුම : "
    for key,value in query_vector.items():
        if value!=None:
            q_string+="| " + value
    q_string+=" |"
    return q_string
