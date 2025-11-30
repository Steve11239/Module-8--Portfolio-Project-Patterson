# Student:  Steve Patterson
# Contact Phone: 248.783.6493
# Contact Personal E-mail: hybridcalibratorsrule@gmail.com
# Contact Student E-mail: steven.patterson@csuglobal.edu
# Course Section: 25FD-CSC500-1 – Principles of Programming
# Course Module: Module 8: Portfolio Milestone Final Submission

# this is the class created from step one of module 4 portfolio milestone exact descriptions followed from instructions
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description
    # prints out the item name wth the quantity and piece cost and the total cose per step one instruction
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")
    # prints out the item name with its description
    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")

# this is the shopping cart class created from step 4 in module 6.  This is the customers shopping cart
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []  # list of cart items
    # method to add an item to purchase by appending the item to the cart items
    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)
    # method to remove an item from the cart and if the item is not found remove nothing
    def remove_item(self, item_name):
        item_found = False
        for i, item in enumerate(self.cart_items):
            if item.item_name == item_name:
                del self.cart_items[i]
                item_found = True
                break
        if not item_found:
            print("Item not found in cart. Nothing removed.")
    # modifies an item that already exists in the cart matched by item name
    def modify_item(self, item_to_purchase):
        item_found = False
        for cart_item in self.cart_items:
            if cart_item.item_name == item_to_purchase.item_name:
                item_found = True
                # update the description only if changed
                if item_to_purchase.item_description != "none":
                    cart_item.item_description = item_to_purchase.item_description
                # update the price only if changed
                if item_to_purchase.item_price != 0.0:
                    cart_item.item_price = item_to_purchase.item_price
                # update the quantity only if changed
                if item_to_purchase.item_quantity != 0:
                    cart_item.item_quantity = item_to_purchase.item_quantity
                break
        if not item_found:
            print("Item not found in cart. Nothing modified.")
    # returns the quantity of all items in the cart and take no parameters
    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity
    # returns the total cost of all items in the cart and take no parameters
    def get_cost_of_cart(self):
        total_cost = 0.0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost
    # prints the shopping carts items with the total cost
    def print_total(self):
        print(f"{self.customer_name}'s shopping cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        if len(self.cart_items) == 0:
            print("\nYour shopping cart is empty, feel free to add an item")
        else:
            for item in self.cart_items:
                item.print_item_cost()
            total = self.get_cost_of_cart()
            print(f"\nTotal: ${total:.2f}")
    # prints each item in the shopping cart
    def print_descriptions(self):
        print(f"{self.customer_name}'s shopping cart - {self.current_date}")
        print("Item Descriptions")
        if len(self.cart_items) == 0:
            print("\nYour shopping cart is empty, feel free to add an item")
        else:
            for item in self.cart_items:
                item.print_item_description()

# print the menu and them processes the user input to update the shopping cart
def print_menu(cart):
    option = ""
    while option != "q":
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity, description, and price")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        option = input("Please choose an option to modify your shopping cart: ").lower()
        # Validate input
        while option not in ["a", "r", "c", "i", "o", "q"]:
            option = input("Choose an option: ").lower()
        if option =="q":
            print("\n Thank you for shopping and have a great day")
            break
        if option == "a":
            print("\nAdd item to the cart?")
            name = input("Enter the item name: ")
            description = input("Enter the item description: ")
            price = float(input("Enter the item price: "))
            quantity = int(input("Enter the item quantity: "))
            item = ItemToPurchase(name, price, quantity, description)
            cart.add_item(item)
        # remove item
        elif option == "r":
            print("\nRemove item from the cart?")
            name = input("Item name to be removed: ")
            cart.remove_item(name)
        # change quantity of item, description or price
        elif option == "c":
            print("\nYou requested to change the quantity of an item, price or description?")
            name = input("Enter the item name you would like to modify: ")
            print("Press Enter to leave the price, quantity, or description unchanged.")

            # INPUT the new quantity, price or description.
            update_quantity = input("Enter the new quantity: ")
            update_price = input("Enter the new price: ")
            update_description = input("Enter the new description: ")

            # init the values
            description = "none"
            price = 0.0
            quantity = 0

            # Only update if user actually typed something, check to see if enter was pressed otherwise update
            # strip the white space
            if update_description.strip() != "":
                description = update_description

            if update_price.strip() != "":
                price = float(update_price)

            if update_quantity.strip() != "":
                quantity = int(update_quantity)

            # Build a temporary item with the fields we want to change from above inputs
            temp_item = ItemToPurchase(
                item_name=name,
                item_price=price,
                item_quantity=quantity,
                item_description=description
            )

            # update the cart!
            cart.modify_item(temp_item)

        # display the descriptions
        elif option == "i":
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
        # display the shopping cart
        elif option == "o":
            print("\nOUTPUT SHOPPING CART")
            cart.print_total()

# main function to input customer name and date then display the shopping cart
def main():
    customer_name = input("Enter your name: ")
    current_date = input("Enter today's date: ")
    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}")
    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)

# standard Python code entry point
if __name__ == "__main__":
    main()