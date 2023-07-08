a,b,c,d,e,f,g,h,i="","","","","","","","",""
print("Welcome to the restaurant order selecter. \n Log in. \n Enter your email. ")
ema=input()
passw=input("Enter your password. ")
print("\n"*49) #Creates a lot of spaces to hide the password
print("WARNING: This is a test session. No data will be saved.")
for forever in range(0,1000000000000000000000000000000000000000000000000000000000000,1): # This for loop repeats the restaurant menu forever
    if passw=="abcdefg": # The password must be "abcdefg"
        print("You are logged in as",ema+'.' "\n What would you like to do? \n [1] Add order \n [2] Remove order \n [3] View orders \n [4] Information") # Options
        opto=int(input()) # Option Input
        if opto==1:
            dish=input("Enter customer's name, followed by their dish using a space. ") # If you enter 1, which is add, this is what it asks
            if a!="": #this if statement sees where to put each person in which slot
                b=dish
                print("Customer successfully saved as letter b.")
            elif b!="":
                c=dish
                print("Customer successfully saved as letter c.")
            elif c!="":
                d=dish
                print("Customer successfully saved as letter d.")
            elif d!="":
                e=dish
                print("Customer successfully saved as letter e.")
            elif e!="":
                f=dish
                print("Customer successfully saved as letter f.")
            elif f!="":
                g=dish
                print("Customer successfully saved as letter g.")
            elif g!="":
                i=dish
                print("Customer successfully saved as letter h.")
            elif h!="":
                i=dish
                print("Customer successfully saved as letter i.")
            elif i!="":
                exit()
            else:
                a=dish
                print("Customer successfully saved as letter a.")
        elif opto==2:
            rem=input("What customer do you want to remove from the list? (Enter it in the order you added it, in ABC order.) ") #to remove
            if rem=='a': #remove if statement
                a=""
                print("Customer successfully removed.")
            elif rem=='b':
                b=""
                print("Customer successfully removed.")
            elif rem=='c':
                c=""
                print("Customer successfully removed.")
            elif rem=='d':
                d=""
                print("Customer successfully removed.")
            elif rem=='e':
                e=""
                print("Customer successfully removed.")
            elif rem=="f":
                f=""
                print("Customer successfully removed.")
            elif rem=="g":
                g=""
                print("Customer successfully removed.")
            elif rem=="h":
                h=""
                print("Customer successfully removed.")
            elif rem=="i":
                i=""
                print("Customer successfully removed.")
            else:
                print("You didn't enter a valid answer. Try again.")
        elif opto==3: #look at customer list
            print("Customer list:")
            print("A:",a)
            print("B:",b)
            print("C:",c)
            print("D:",d)
            print("E:",e)
            print("F:",f)
            print("G:",g)
            print("H:",h)
            print("I:",i)
        elif opto==4: #information
            print("At the main menu, enter the number using the corresponding choices. Then, follow the choices once you enter a number.")    
    else:
        print("Your email or password is incorrect.")
        exit()

