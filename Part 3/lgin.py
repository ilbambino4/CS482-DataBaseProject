import mysql.connector

#error check variable
error=False

#Initial Title
title = "Database Login"
print(title.center(20),"\n")

#Asks for user info to connect to the database and throws an error if connection fails
#Loops until valid connection is created
while(1):
    host = input("   input database host: ")
    name = input("   input database name: ")
    username = input("   input username: ")
    password = input("   input password: ")
    print()

    try:
        db = mysql.connector.connect(host=host, user=username,
                                    password=password, database=name,
                                    )
        mycursor = db.cursor()
    except:
        print("   ERROR: Could Not Connect to Database")
        print("   ERROR: Try again")
        print()
        error=True

    if (not error):
        break
    else:
        error=False

print("   Database Connection Established")
print()

def main():
    #User's choice
    choice=0

    error=False

    #loops available options for the user to choose from
    while(1):
        print("   Available Options:")
        print("   1. Display all the digital displays.")
        print("   2. Search digital displays given a scheduler system")
        print("   3. Insert a new digital display")
        print("   4. Delete a digital display")
        print("   5. Update a digital display")
        print("   6. Logout")
        print()
        
        #checks to see if user input is a number
        try:
            choice=int(input("   Enter your choice (1-6): "))
            print()
        except:
            print()
            print("   ERROR: Must enter a number for your choice (1-6)")
            print()
            error=True

        if (not error):
            #checks to see if choice is between 1 and 6
            if (choice > 6 or choice < 1):
                print("   ERROR: Must enter a valid number for your choice (1-6)")
                print()
            else:
                #checks for the choice 6 to exit
                if (choice==6):
                    print("   Goodbye")
                    break
                else:
                    #calls function that will execute the user's choice
                    #function uses user's choice and database cursor
                    selection(choice)

        error=False
    

############################################################
def selection(choice):
    if (choice == 1):
        #Displays all Digital Displays
        display_dig_disp()
    elif(choice == 2):
        #Searches Digital Display Systems
        search_dig_disp()
    elif(choice == 3):
        #Insert a new Digital Display
        print("2")
    elif(choice == 4):
        #Delete a Digital Display
        print("2")
    else:
        #Updates a Digital Display
        print("2")

#1. 1. Display all the digital displays.
############################################################
def display_dig_disp():
    search = "SELECT * FROM DIGITALDISPLAY"
    
    mycursor.execute(search)

    #Fetches the rows from the search
    rows = mycursor.fetchall()

    #Prints message to user if search is empty
    if(len(rows) == 0):
        print("   Digital Displays is empty")
        print()
    else:
        print("   All Digital Displays:")
        #Prints returned Digital Displays if search return is not empty
        cnt = 1
        for x in rows:
            print("  ",cnt," ",x)
            cnt = cnt + 1
        print()

#2. Search digital displays given a scheduler system
############################################################
def search_dig_disp(): 
    s = input("   Enter schedular system you want to search: ")
    print()
    search = "SELECT * FROM DIGITALDISPLAY WHERE SCHEDULERSYSTEM='"+s+"'"
    
    mycursor.execute(search)

    #Fetches the rows from the search
    rows = mycursor.fetchall()

    #Prints message to user if search is empty
    if(len(rows) == 0):
        print("   Nothing returned from search")
        print()
    else:
        print("   Returned Digital Displays:")
        #Prints returned Digital Displays if search return is not empty
        cnt = 1
        for x in rows:
            print("  ",cnt," ",x)
            cnt = cnt + 1
        print()

#3. Insert a new digital display 
#4. Delete a digital display 
#5. Update a digital display 
#6. Logout ")

main()
db.close()