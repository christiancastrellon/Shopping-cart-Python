#Name: Christian Castrellon
#Date: Oct 4, 2026
#Purpose: Create an online shopping cart program

#TODO: ItemToPurchase class
class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    def print_item_cost(self):
        totalCost = self.item_quantity * self.item_price
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price:.0f} = ${totalCost:.0f}')

#TODO: ShoppingCart class
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2025"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []



    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        found = False
        for i in self.cart_items:
            if i.item_name == item_name:
                found = True 
                self.cart_items.remove(i)
        if found == False:
            print('Item not found in cart. Nothing removed.')

    def modify_item(self, item):
        found = False
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == item.item_name:
                found = True
                self.cart_items[i].item_quantity = item.item_quantity
        if found == False:
            print("Item not found in cart. Nothing modified.")
    
    def print_total(self):
        total_num_items =0
        total_cost=0
        print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
        if len(self.cart_items) >0:
            for i in self.cart_items:
                total_num_items += i.item_quantity
                total_cost += i.item_price * i.item_quantity
                i.print_item_cost()
            print(f'Number of Items: {total_num_items}\n')
            print(f'Total: ${total_cost:.0f}')
        else:
            print("SHOPPING CART IS EMPTY")




#TODO: print_menu function
def print_menu():
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("o - Output shopping cart")
    print("q - Quit\n")
#TODO: implement menus in execute_menu()

def execute_menu(menuOp, theCart):
    if menuOp == 'a':
        print('ADD ITEM TO CART')
        name = input("Enter the item name: ")
        price = float(input("Enter the item price: "))
        quantity = int(input("Enter the item quantity: "))

        new_item = ItemToPurchase()
        new_item.item_name = name
        new_item.item_price = price 
        new_item.item_quantity = quantity
        
        theCart.add_item(new_item)
        print()


    elif menuOp == 'r':
        print('REMOVE ITEM FROM CART')
        name = input("Enter name of item to remove:\n")
        theCart.remove_item(name)
        print()


    elif menuOp == 'c':
        print('CHANGE ITEM QUANTITY')
        name = input("Enter the item name:\n")
        quantity = int(input("Enter the new quantity:\n"))

        item= ItemToPurchase()
        item.item_name = name
        item.item_quantity = quantity
        theCart.modify_item(item)
        print() 


    elif menuOp == 'o':
        print('OUTPUT SHOPPING CART')
        theCart.print_total()
        print()

                
if __name__ == "__main__":
    menu_choice = ' '
    #TODO: Prompt user for name and date
    cust_name = input("Enter customer's name: ")
    day_date = input("Enter today's date: ")

    print(f'\nCustomer name: {cust_name}')
    print(f'Today\'s date: {day_date}')
    print()
    my_cart = ShoppingCart(cust_name, day_date)

    print_menu()

    while menu_choice != 'q':
        menu_choice = input('Choose an option:\n')
        if menu_choice in ['a', 'r', 'c', 'o']:
            execute_menu(menu_choice, my_cart)
            print_menu()