import myDb as shoedb
class MyShoes:

    def __init__(self, shoe_name, color, price, brand):
        self.color = color
        self.price = price
        self.brand = brand
        self.shoe_name = shoe_name


def get_shoes():
    new_shoes1 = MyShoes("Mamadou 2s", "light gray", 750, "Africanos")
    new_shoes2 = MyShoes("Mamadou 1s","noir",750,"Africanos")
    new_shoes = [new_shoes1,new_shoes2]
    print("\n\nFeel free to checkout out our luxurious African shoe collection:")
    for new_shoe in new_shoes:
     print(f"{new_shoe.shoe_name} for ${new_shoe.price} in {new_shoe.color}")



def list_shoes():
    kyrie1s = MyShoes("Kyrie 1s","blue",150, "Nike")
    jordan1s = MyShoes("Jordan 1s","red", 250, "Jordan")
    lebron12s = MyShoes("Lebron 12s","light blue", 190, "Nike")
    my_shoes = [kyrie1s, jordan1s, lebron12s]
    #my_shoes.append(get_shoes())
    print("These are all shoes currently available")
    for shoes in my_shoes:
        print(f"{shoes.shoe_name} for ${shoes.price} in {shoes.color}")


def new_customer():
     store_name = "KOTD for BALLER$"
     #style = input ("What is the occasion: ")
     prGreen("            Welcome to KOTD for BALLER$")

     print(f"How can I help you? Mr.{name}\n\n")

def prGreen(green):
    print("\033[92m {}\033[00m" .format(green))


name = input("What's your name?  \n")
age = int(input("what's  your age: "))
new_customer()
list_shoes()
get_shoes()


