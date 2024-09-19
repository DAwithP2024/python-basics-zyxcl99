

# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

def display_sorted_products(products_list, sort_order):
    if sort_order == "asc":
        return sorted(products_list, key=lambda x: x[1])
    elif sort_order == "desc":
        return sorted(products_list, key=lambda x: x[1], reverse=True)

def display_products(products_list):
    for index, product in enumerate(products_list):
        print(f"{index + 1}. {product[0]} - ${product[1]}")

def display_categories():
    for index, category in enumerate(products):
        print(f"{index + 1}. {category}")

def add_to_cart(cart, product, quantity):
    cart.append((product[0], product[1], quantity))

def display_cart(cart):
    total_cost = 0
    for item in cart:
        print(f"{item[0]} - ${item[1]} x {item[2]} = ${item[1] * item[2]}")
        total_cost += item[1] * item[2]
    print(f"Total cost: ${total_cost}")

def generate_receipt(name, email, cart, total_cost, address):
    print(f"Customer: {name}\nEmail: {email}\nItems Purchased:\n")
    for item in cart:
        print(f"{item[2]} x {item[0]} - ${item[1]} = ${item[1] * item[2]}")
    print(f"Total: ${total_cost}\nDelivery Address: {address}")
    print("Your items will be delivered in 3 days.\nPayment will be accepted upon delivery.")

def validate_name(name):
    return name.replace(" ", "").replace("-", "").isalpha() and " " in name

def validate_email(email):
    return "@" in email and "." in email

def main():
    name = input("Please enter your name: ")
    email = input("Please enter your email address: ")
    
    while not validate_name(name):
        name = input("Invalid name. Please enter a valid name with first and last name: ")
    while not validate_email(email):
        email = input("Invalid email. Please enter a valid email address: ")
    
    display_categories()
    category_choice = int(input("Please select a category (number): ")) - 1
    category = list(products.keys())[category_choice]
    
    products_list = products[category]
    display_products(products_list)
    
    while True:
        choice = input("Select an option: 1. Buy a product, 2. Sort products, 3. Go back, 4. Finish shopping: ")
        if choice == "1":
            product_choice = int(input("Enter the product number: ")) - 1
            if 0 <= product_choice < len(products_list):
                quantity = int(input("Enter the quantity: "))
                add_to_cart(cart, products_list[product_choice], quantity)
            else:
                print("Invalid product number. Please try again.")
        elif choice == "2":
            sort_order = input("Sort by 1. Ascending or 2. Descending: ")
            sorted_products = display_sorted_products(products_list, sort_order)
            display_products(sorted_products)
        elif choice == "3":
            display_categories()
            category_choice = int(input("Please select a category (number): ")) - 1
            category = list(products.keys())[category_choice]
            products_list = products[category]
            display_products(products_list)
        elif choice == "4":
            if cart:
                total_cost = sum(item[1] * item[2] for item in cart)
                address = input("Please enter your delivery address: ")
                generate_receipt(name, email, cart, total_cost, address)
            else:
                print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day")
            break

if __name__ == "__main__":
    main()
#