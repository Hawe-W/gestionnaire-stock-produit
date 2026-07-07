stock = []

product_number = int(input("Combien de produit voulez vous ajouté ? : "))

for product in range(product_number):
    name = input("Le nom de votre produit : ")
    quantity = int(input("La quantité : "))
    product_list = {
        "product": name,
        "quantity": quantity
    }
    stock.append(product_list)

print(stock)

for product in stock:
    if product["quantity"] > 0:
        print(product["product"], "-", product["quantity"])