import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# voeg pryse by
def add_prices(prices):
    total = 0
    for price in prices:
        total += price
    return total

# prys formaat
def format_price(price):
    return f"R{price:.2f}"

def main():
    items = []
    prices = []
    
    while True:
        clear_screen()
        print("=== Point of Sale ===")
        item = input("Enter item name (or type 'done' to finish): ").strip()
        
        # Sentinel
        if item.lower() == 'done':
            break
        
        try:
            price = float(input(f"Enter price for {item}: R"))
            items.append(item)
            prices.append(price)
        except ValueError:
            print("Invalid price. Please enter a number.")
            input("Press Enter to continue...")

    clear_screen()
    print("=== Receipt ===")
    
    for item, price in zip(items, prices):
        print(f"{item:<10} {format_price(price)}")
    
    print("-" * 20)
    total = add_prices(prices)
    print(f"{'Total':<10} {format_price(total)}")

if __name__ == "__main__":
    main()