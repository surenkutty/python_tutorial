class Item:
    def __init__(self, id, pname, price):
        self.id = id
        self.pname = pname
        self.price = price
    
    def display(self, l, customerName, Address):
        total = 0
        print("\n\n\n")
        print("\t   Surend Departmental Store   ")
        print("\t ----------------------------------------")
        print(f"Name:{customerName}\t Address:{Address}")
        print('\n')
        for obj in l:
            print(f"Id : {obj.id}\t ItemName : {obj.pname}\t Price:{obj.price}")
            print("-----------------------------------------------------------------")
            total += obj.price
        print(f"\t\tTotal : {total}")
        print("\n")
        print("\t Thanks for Visiting Shop")
    
    def perform(self, totalItems):
        datas = []
        for i in range(0, totalItems):
            id = (i + 1)
            pname = input("Enter the Product Name: ")
            price = int(input("Enter the Price: "))
            datas.append(Item(id, pname, price))
        return datas

if __name__ == "__main__":
    customerName = input("Enter Your Name: ")
    Address = input("Enter Your Address: ")
    print("\n\n")

    totalItems = int(input("Enter the Total Items: "))
    print("\n\n")

    item_obj = Item(0, '', 0)  # Create an instance to call instance methods
    datas = item_obj.perform(totalItems)  # Get the list of items
    item_obj.display(datas, customerName, Address)  # Display the items
