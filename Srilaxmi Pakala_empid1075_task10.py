# Smart Inventory Management System

inventory = {}

# Add Product
def add_product():
    pid = input("Enter Product ID: ")
    if pid in inventory:
        print("Product ID already exists!")
        return

    name = input("Enter Product Name: ")
    category = input("Enter Category: ")
    qty = int(input("Enter Quantity: "))
    price = float(input("Enter Price: "))
    supplier = input("Enter Supplier: ")

    inventory[pid] = {
        "name": name,
        "category": category,
        "qty": qty,
        "price": price,
        "supplier": supplier
    }
    print("Product Added Successfully!")

# Update Inventory
def update_inventory():
    pid = input("Enter Product ID: ")
    if pid in inventory:
        inventory[pid]["qty"] = int(input("Enter New Quantity: "))
        inventory[pid]["price"] = float(input("Enter New Price: "))
        print("Inventory Updated!")
    else:
        print("Product Not Found!")

# Search Product
def search_product():
    keyword = input("Enter Product ID or Name: ").lower()

    found = False
    for pid, product in inventory.items():
        if keyword == pid.lower() or keyword == product["name"].lower():
            print("\nProduct Found:")
            print(pid, product)
            found = True

    if not found:
        print("Product Not Found!")

# Display Inventory
def display_inventory():
    if not inventory:
        print("Inventory Empty!")
        return

    print("\n--- Inventory ---")
    print("ID\tName\tCategory\tQty\tPrice")
    for pid, product in inventory.items():
        print(f"{pid}\t{product['name']}\t{product['category']}\t{product['qty']}\t{product['price']}")

# Low Stock Alert
def low_stock_alert():
    print("\nLow Stock Products (Qty < 5)")
    found = False
    for pid, product in inventory.items():
        if product["qty"] < 5:
            print(pid, product["name"], "Qty:", product["qty"])
            found = True

    if not found:
        print("No Low Stock Products")

# Out of Stock Alert
def out_of_stock_alert():
    print("\nOut of Stock Products")
    found = False
    for pid, product in inventory.items():
        if product["qty"] == 0:
            print(pid, product["name"])
            found = True

    if not found:
        print("No Out of Stock Products")

# Category Management
def category_management():
    categories = set()

    for product in inventory.values():
        categories.add(product["category"])

    print("\nCategories:")
    print(categories)

# Inventory Report
def inventory_report():
    total_items = len(inventory)

    total_value = 0
    for product in inventory.values():
        total_value += product["qty"] * product["price"]

    print("\nInventory Report")
    print("Total Products:", total_items)
    print("Total Inventory Value:", total_value)

# Delete Product
def delete_product():
    pid = input("Enter Product ID to Delete: ")

    if pid in inventory:
        del inventory[pid]
        print("Product Deleted!")
    else:
        print("Product Not Found!")

# Menu
while True:
    print("\n===== SMART INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. Update Inventory")
    print("3. Search Product")
    print("4. Display Inventory")
    print("5. Low Stock Alert")
    print("6. Out of Stock Alert")
    print("7. Category Management")
    print("8. Inventory Report")
    print("9. Delete Product")
    print("10. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        update_inventory()
    elif choice == "3":
        search_product()
    elif choice == "4":
        display_inventory()
    elif choice == "5":
        low_stock_alert()
    elif choice == "6":
        out_of_stock_alert()
    elif choice == "7":
        category_management()
    elif choice == "8":
        inventory_report()
    elif choice == "9":
        delete_product()
    elif choice == "10":
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")
