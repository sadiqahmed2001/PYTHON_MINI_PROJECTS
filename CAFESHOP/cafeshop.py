def display_menu():            
    menu = {
        "coffee": 3.00,
        "tea": 2.50,
        "sandwich": 5.00,
        "cake": 4.00
    }  
    
    print("Welcome to Our Cafe")
    print("Menu:")
    for item, price in menu.items():
        print(f"{item.capitalize()}: ${price:.2f}")
    
    return menu

def get_order(menu):
    order = {}
    
    for item in menu:
        while True:
            try:
                quantity = int(input(f"How many {item}s would you like? "))
                if quantity < 0:
                    print("Please enter a positive number.")
                else:
                    order[item] = quantity
                    break
            except ValueError:
                print("Please enter a valid number.")
    
    return order

def calculate_bill(menu, order):
    total = 0
    bill_details = []
    
    for item, quantity in order.items():
        item_total = menu[item] * quantity
        total += item_total
        bill_details.append(f"{item.capitalize()}: {quantity} x ${menu[item]:.2f} = ${item_total:.2f}")
    
    return total, bill_details

def display_bill(total, bill_details):
    print("\nBill:")
    for detail in bill_details:
        print(detail)
    print(f"Total: ${total:.2f}")

def main():
    menu = display_menu()
    order = get_order(menu)
    total, bill_details = calculate_bill(menu, order)
    display_bill(total, bill_details)

if __name__ == "__main__":
    main()
