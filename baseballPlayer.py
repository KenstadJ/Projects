class Player:  
    def __init__(self, name, jersey, avg):  #finish constructor..needs more parameters and attributes assigned 
        self.name = name
        self.jersey = jersey
        self.avg = avg  
        

if __name__ == "__main__":   #<<< do not remove or modify this line of code, it is required to test your objects/methods.
#all code for your main program should exist below this line, and be indented 1 additional level

    mylist = []   #I have started a list for you for your objects
    


   
    print("Welcome to Rostermatic!")
    i = '0'
    while i == '0':
        

        
    
        
        print("Please type the number of your selection below.")
        print('''
    
        1: Add Player

        2: Remove Player

        3: Find Best Hitter

        4: Print Players

        5: Exit''')

        choice = input()

        if choice == '1':
            N = input("What is the name of your player?")
            
            J = input("What jersey number is your player?")
            
            B =input("What is the players batting average?")
            
            mylist.append(Player(N, J , B))

        elif choice == '2':
            h = 1
            for pl in mylist:
                print(str(h)+ ":" + pl.name)
                h+=1
            pick = input("Type in the number for the player you want to remove.")
            del mylist[int(pick)-1]
            

        elif choice == '3':
            
            h = 0
            highest = 0
            for high in mylist:
                if high.avg > mylist[highest].name:
                    highest = h
                h += 1
            print("The player with the highest average is",str(mylist[highest].name) ,"with an average of",str(mylist[highest].avg), ".")
            
        elif choice == '4':
            h = 1
            for pl in mylist:
                print(str(h)+ ":" + pl.name + " " +pl.jersey)
                h+=1
            
            
            
        elif choice == '5':
            i = 1
                
    print("Goodbye")



