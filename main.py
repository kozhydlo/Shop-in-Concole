import json


with open('products.json', 'r', encoding='utf-8') as file:
    products = json.load(file)


def show_products():
    print("Список товарів:")
    for idx, product in enumerate(products, start=1):
        print(f"{idx}. {product['name']} - {product['price']} грн")


def add_to_cart(product_index):
    selected_product = products[product_index - 1]
    cart.append(selected_product)
    print(f"{selected_product['name']} додано до корзини.")


def remove_from_cart(cart_index):
    if 1 <= cart_index <= len(cart):
        removed_product = cart.pop(cart_index - 1)
        print(f"{removed_product['name']} видалено з корзини.")
    else:
        print("Недійсний номер товару в корзині.")


def show_cart():
    print("Корзина:")
    for idx, product in enumerate(cart, start=1):
        print(f"{idx}. {product['name']} - {product['price']} грн")


cart = []


customer_info = {}
discount = 0

while True:
    print("\nМеню:")
    print("1. Показати товари")
    print("2. Додати товар до корзини")
    print("3. Видалити товар з корзини")
    print("4. Показати корзину")
    print("5. Пошук товарів")
    print("6. Вказати інформацію про покупця")
    print("7. Застосувати знижку")
    print("8. Вийти")

    choice = input("Виберіть опцію: ")

    if choice == '1':
        show_products()
    elif choice == '2':
        show_products()
        product_index = int(input("Виберіть номер товару, щоб додати його до корзини: "))
        if 1 <= product_index <= len(products):
            add_to_cart(product_index)
        else:
            print("Недійсний номер товару.")
    elif choice == '3':
        show_cart()
        cart_index = int(input("Виберіть номер товару в корзині для видалення: "))
        remove_from_cart(cart_index)
    elif choice == '4':
        show_cart()
    elif choice == '5':
        keyword = input("Введіть ключове слово для пошуку товарів: ")
        search_products(keyword)
    elif choice == '6':
        customer_info['name'] = input("Введіть ваше ім'я: ")
        customer_info['email'] = input("Введіть вашу електронну адресу: ")
    elif choice == '7':
        discount = float(input("Введіть розмір знижки (у відсотках): "))
    elif choice == '8':
        break
    else:
        print("Недійсний вибір.")


total_price = sum(product['price'] for product in cart)
total_price_with_discount = total_price * (1 - discount / 100)

# Зберігаємо дані про покупку у  JSON
purchase_info = {
    'customer_info': customer_info,
    'cart': cart,
    'total_price': total_price_with_discount
}

with open('purchase_info.json', 'w') as file:
    json.dump(purchase_info, file)

print("Дякуємо за покупку!")
