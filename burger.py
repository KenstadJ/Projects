class Burger:
    def __init__(self):
        self.bName="default"
        self.bMeat="default"
        self.bVeg="default"
        self.bBread="default"
        self.bCondiment= "default"
        self.bPrice= 0.00
        
    def printBurger (self):
      print("Name: "+ self.bName)
      print("Meat: "+ self.bMeat)
      print("Veg: "+ self.bVeg)
      print("Bread: "+ self.bBread)
      print("Condiment: "+ self.bCondiment)
      print("Price: $"+ str("{:.2f}".format(self.bPrice)))

    def doubleMeat(self):
        self.bPrice=self.bPrice *2
        self.bMeat=self.bMeat + " x 2"
       
if __name__ == "__main__":
    
  print("Welcome to BurgerWorld!\n")
  name=input("What type of burger do you want?\n")
  
  myBurger= Burger() #create the burger object
  myBurger.bName=name #mutate name attribute of burger object
  
  print("A "+ myBurger.bName+ " is a great choice!")#access the name attribute of your created burger

  meat=input("What type of meat?\n")
  veg=input("What type of vegetable?\n")
  bread=input("What type of bread?\n")
  condiment=input("What type of condiment?\n")
  price=float(input("How much is your burger?\n"))
  superSize=input("Would you like to make it a double? YES or NO\n")

  #mutate remaining attributes 
  myBurger.bMeat=meat
  myBurger.bVeg=veg
  myBurger.bBread=bread
  myBurger.bCondiment=condiment
  myBurger.bPrice=price

  #..modify program between here... 
  if (superSize == "YES"):
    myBurger.doubleMeat()




  

  #...and here only... to call the doubleMeat method from your myBurger object when appropropriate.
  
  myBurger.printBurger()   #calls the printBurger() method from your myBurger object.
  print("Thank you for choosing BurgerWorld!")
              
        
        
        

