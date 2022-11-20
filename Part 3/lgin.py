import mysql.connector

#helper funciton to varify existence of a dig display 
def dig_display_exist(serialNo):
    sql = "select serialNo\
           from DigitalDisplay\
           where serialNo = %s;"
           
    val = (serialNo,)
    
    mycursor.execute(sql, val)

    myresult = mycursor.fetchall()
    
    if len(myresult) == 0:
        return False
    else:
        print("   Digital Display with Serial Number", serialNo, "exists")
        print("")
        return True
    
#helper function to varify existence of model
def model_eixst(modelNo):
    sql = "select modelNo\
           from Model\
           where modelNo = %s;"
           
    val = (modelNo,)
    
    mycursor.execute(sql, val)

    myresult = mycursor.fetchall()
    
    if len(myresult) == 0:
        return False
    else:
        return True
    
# function used to create a newe model with the useres model number
def create_model(modelNo):
    
    print("   Following decimal values should not be more than 6 numbres in lengt and no more than two decimal points to the right. Ex: 1234.43 = valid but 12.1234 = not valid")
    print("")
    heigth = float(input("   Height: "))
    width = float(input("   Width: "))
    weight = float(input("   Weight: "))
    depth = float(input("   Depth: "))
    screeenSize = float(input("   Screen Size: "))
    
    sql = "insert into Model\
            values(%s,%s,%s,%s,%s,%s);"
                   
    val = (modelNo, heigth, width, weight, depth, screeenSize)
    
    mycursor.execute(sql, val)

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
        display_dig_disp_model()
    elif(choice == 2):
        #Searches Digital Display Systems
        search_dig_disp()
    elif(choice == 3):
        #Insert a new Digital Display
        create_dig_display()
    elif(choice == 4):
        #Delete a Digital Display
        print("2")
    else:
        #Updates a Digital Display
        update_dig_display()

#1. 1. Display all the digital displays.
############################################################
#This method is for just displaying digital displays and won't ask users if they want to see model info
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

#This method will display digital displays but will also allow user to select a model to display as well.
def display_dig_disp_model():
    #bool to check if digital displays is empty
    empty = False

    search = "SELECT * FROM DIGITALDISPLAY"
    
    mycursor.execute(search)

    #Fetches the rows from the search
    rows = mycursor.fetchall()

    #Prints message to user if search is empty
    if(len(rows) == 0):
        print("   Digital Displays is empty")
        print()
        empty = True
    else:
        print("   All Digital Displays:")
        #Prints returned Digital Displays if search return is not empty
        cnt = 1
        for x in rows:
            print("  ",cnt," ",x)
            cnt = cnt + 1
        print()
    
    if (not empty):

        error=False
        
        while(1):
            print("   Would you like to see more detailed information on a specific model?")
            print("   1. Yes")
            print("   2. No, take me back to the main menu")

            try:
                choice=int(input("   Enter your choice: "))
                print()
            except:
                print()
                print("   ERROR: Must enter a number for your choice (1 or 2)")
                print()
                error=True

            if (not error):
                if (choice > 0 and choice < 3):
                    break
                else:
                    print()
                    print("   ERROR: Choice must be a valid number (1 or 2)")
                    print()
            else:
                error=False
        

        if (choice==1):
            while(1):
                print("   Which Digital Display would you like to see more info on their model number?")
                search = "SELECT * FROM DIGITALDISPLAY"
        
                mycursor.execute(search)

                #Fetches the rows from the search
                rows = mycursor.fetchall()

                #Prints returned Digital Displays if search return is not empty
                cnt = 1
                for x in rows:
                    print("  ",cnt," ",x)
                    cnt = cnt + 1
                print()
                
                #offset for printing the amount of options available to the user
                cnt-=1

                error=False
            
                try:
                    print("   Select digital display ( 1 -",cnt, "): ", end='')
                    choice=int(input(""))
                except:
                    print()
                    print("   ERROR: Must enter a number for your choice (1 - ", cnt, ")")
                    print()
                    error=True

                if (not error):
                    if(choice > 0 and choice < cnt):
                        break
                    else:
                        print()
                        print("   ERROR: Must enter a valid number (1 - ", cnt, ")")
                        print()
                else:
                    error=False

            print()
            print("   Model Information for", rows[choice-1], ":")
            print()

            search = "SELECT * FROM MODEL WHERE modelNo='"+rows[choice-1][2]+"'"

            mycursor.execute(search)

            #Fetches the rows from the search
            rows = mycursor.fetchall()

            #Prints returned Digital Displays if search return is not empty
            for x in rows:
                print("  ",x)
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
############################################################

def create_dig_display():
    validSereialNo = False
    validModelNo = False
    validSchedulSys = False
    validSys = ["Random", "random", "Smart", "smart", "Virtue", "virtue"]
    
    while validSereialNo != True: 
        serialNo = input("   Serial Number for new Digital Display: ")
        if len(serialNo) <= 10:
            validSereialNo = True
        else:
            print("   Serial Number too long...Try Again")
            print("")
            
    while validModelNo != True:
        modelNo = input("   Model Number for new Digital Display: ")
        if len(modelNo) < 10:
            validModelNo = True
            if model_eixst(modelNo) != True:
                #create the new model
                print("   Model with Model Number ", modelNo, " does not exist...moving user to create new model")
                print("")
                create_model(modelNo)
        else:
            print("   Model Number too long...Try again")
            print("")
            
    while not validSchedulSys:
        schedSys = input("   New Scheduler System: ")
         
        if schedSys in validSys:
            validSchedulSys = True
            print("   Valid Scheduler System")
            print("")
        else: 
             print("   Not a valid Sheduler System...Try again")
             print("")
             
    print("   Creating New Digital Display")
    print("")
    sql = "insert into DigitalDisplay\
            values(%s,%s,%s);"
            
    val = (serialNo, schedSys, modelNo)
     
    mycursor.execute(sql, val)

    db.commit()
    
    display_dig_disp()

    

#4. Delete a digital display 
############################################################
def delete_dig_display():
    validInput = ["Random", "random", "Smart", "smart", "Virtue", "virtue"]


#5. Update a digital display 
############################################################

# this is where you started your work
#serialNo
#schedulerSystem
#modelNo

def update_dig_display():
    exist = False
    
    # will keep asking the user to input a serial numer
    # if the current number they inputed is not a valid serial number
    while exist != True:
        display_dig_disp()

        serialNo = input("   Serial Number of Display to update: ")
        if dig_display_exist(serialNo) == True:
            exist = True
            #break
        else:
            print("   Serial Number not found...Try again")
            print("")
    
    # list that is holding the valid 
    # scheduler systems the user can input
    validInput = ["Random", "random", "Smart", "smart", "Virtue", "virtue"]
    goodResponse = False
    
    # checking if the scheduler system 
    # user inputed is one of the available scheduler systems
    # if it is not, program will keep asking user to input 
    # a scheduler system until it's a valid system
    while not goodResponse:
        newSchedSystem = input("   New Scheduler System: ")
        
        if newSchedSystem in validInput:
            goodResponse = True
            print("   Valid Scheduler System")
        else: 
            print("   Not a valid Sheduler System...Try again")
            print("")
    
    print("   Updating Digital Display with Serial Number: ", serialNo)
    print("")
    
    print("   Updated Digital Displays")
    print("")
    
    #sql command used to update stuff
    sql = "update DigitalDisplay\
            set schedulerSystem = %s\
            where serialNo = %s;"
    
    val = (newSchedSystem, serialNo)
    
    mycursor.execute(sql, val)
    
    display_dig_disp()

#6. Logout ")

main()
db.close()