def main():

    # HOME WORK

    jeans = [

        # [Brand, Rate, Popularity Rating]
        ["HRX", 900, 4],
        ["Raymond", 1500, 3.5],
        ["Costco", 1300, 5],
        ["Ajink", 800, 2]
    ]


    # price list sorted in increasing order of price
    print(sorted(jeans, key=keyPrice))

    # Popular list - sorted in desceding order / decreasing order of popularity
    print(sorted(jeans, reverse=True, key=keyRating))

    # Catalogue list - sorted in increasing order of brand name  [A-Z]
    print(sorted(jeans, key=keyBrand))

def keyPrice(item):
    return item[1]

def keyRating(item):
    return item[2]

def keyBrand(item):
    return item[0]