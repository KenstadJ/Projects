class Item:  
    def __init__(self,name, price, weight):  #<<finish this
        self.name = name
        self.price = float(price)
        self.weight = float(weight)

        #add attributes for price & weight
        
    def getTotal(self):
        total=0.0
        shipping = 1.5 * self.weight
        total = self.price + shipping
        #finish this with the correct calculation for price & shipping
        return total

class ImportedItem(Item):
    def getTotal(self): 
             #overrides getTotal from superclass Item
        total=0.0
        shipping = 3.0 * self.weight
        total = self.price + shipping
        #finish this with the correct calculation for price & shipping for Imported items
        return total
        

if __name__ == "__main__":   #<<< do not remove or modify this line of code, it is required to test your objects/methods.
#all code for your main program should exist below this line, and be indented 1 additional level
    Cart = []
    print("Welcome to eBuy!!")
    print("*****")
    T = "0"
    while T == "0":
        choice = input("Do you want to add an item to your order?")
        print("yes = add item.....no = checkout")
        if choice == 'yes':
            n = input("What is the name of the item?")
            p = input("What is the price of the item?")
            w = input("What is the weight of the item?")
            i = input("Does it need to be imported? yes or no")
            if i == 'yes':
                Cart.append(ImportedItem(n, p, w))
                T = "0"
            else:
                Cart.append(Item(n, p , w))
                T = "0"
        else:
            T = "1"

    print("*****")
    h = 1
    total = 0.0
    for O in Cart:
        print(str(h)+ ":" + O.name)
        print("Unit price: $"+ str(O.price))
        print("*****")
        h+=1
        total = O.getTotal() + total
    print("Total with shipping: $"+ str(total))
    print("Your order will be shipped shortly.")
    print("Thank you for choosing eBuy!")

        


    
    #finish the rest of your program!

        
    

