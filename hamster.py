class BitHamster:  #don't change class name.  
    def __init__(self):
        self.hamsterName= "default"
        self.hamsterCoin = 0.0
        self.hamsterHp = 50
        #put class attributes here
    def work(self):
        self.hamsterCoin += .001
        self.hamsterHp -= 20

        
    def rest(self):
        self.hamsterHp += 10

         
        
    #put class functions here
        
if __name__ == "__main__":


    print("Welcome to BitHamster!")
    name = input("What would you like to name your poor hamster?")
    

    

    
    player = BitHamster()
    player.hamsterName = name
    
    print("Great! Lets put"+player.hamsterName+" to work on the wheel of Bitcoin!")
    print("HP: "+ str(player.hamsterHp))
    print("Bitcoin: "+ str(player.hamsterCoin))
    print("*****")
    choice = '0'
    while player.hamsterHp > 0 and choice != 3:
        print("What do you want to do?")
        print("1: Put Hammy to work.")
        print("2: Let Hammy rest.")
        print("3: Cash in Hammy.")
        response = input()

        if choice == '1':
            player.work()

        elif choice == '2':
            player.rest()

        else:
            print("Error, please select 1 or 2")
            
        

        




    
    
    
        

