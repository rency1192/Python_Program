from product_list import ProductList
from shopping_cart import ShoppingCart
from clothing_product import ClothingProduct
def main():
    product_list = ProductList()
    shopping_cart = ShoppingCart()

    product_list.add_product("L001", "Laptop", 1200, "electronics")
    product_list.add_product("P001", "Smartphone", 500, "electronics")
    product_list.add_product("S001", "Men's Shirt", 30, "clothing")
    product_list.add_product("S002", "Women's Dress", 50, "clothing")
    product_list.add_product("E001", "Headphones", 100, "electronics")

    product_list.display_all_products()
   
    shopping = True
    while shopping:
        print("\nSelect a Category:")
        print("1. Male")
        print("2. Female")
        print("3. Electronics")
        print("4. View Cart")
        print("5. Remove any product")
        print("6. Empty cart")
        print("7. Update")
        print("8. Finish Shopping")
        choice = input("Enter your choice (1-5): ")
        if choice in ['1', '2', '3']:
            product_id = product_list.get_valid_product_id()
            quantity = int(input("Enter quantity: "))
            selected_product = product_list.get_product(product_id)
            if selected_product:
                shopping_cart.add_item(selected_product, quantity)
            else:
                print("Invalid product ID.")
        elif choice == '4':
            shopping_cart.view_cart()
        elif choice == '5':
            id=input("Enter product Id that you want remove from cart...")
            shopping_cart.remove_item(id)
        elif choice == '6':
            shopping_cart.clear_cart()
        elif choice == '7':
            product_id = input("Enter product ID to update in cart: ")
            new_quantity = input("Enter new quantity (press Enter to skip): ")
            selected_product = product_list.get_product(product_id)
            if selected_product:
                if isinstance(selected_product, ClothingProduct):
                    new_size = input("Enter new size (press Enter to skip): ")
                    new_color = input("Enter new color (press Enter to skip): ")
                    shopping_cart.update_item(product_id, new_quantity, new_size, new_color)
                else:
                    shopping_cart.update_item(product_id, new_quantity)
            else:
                print("Invalid product ID.")
        elif choice == '8':
            shopping_cart.generate_bill()
            continue_shopping = input("Do you want to continue shopping? (yes/no): ").lower()
            if continue_shopping != 'yes':
                shopping = False
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
