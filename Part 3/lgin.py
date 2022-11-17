import mysql.connector

############################################################
def database_controller(usrname, pswrd):
    db = mysql.connector.connect(host="localhost", user=usrname,
                                 password=pswrd, database="proj_1",
                                 auth_plugin='mysql_native_password')
    mycursor = db.cursor() 
    Salesmen = ("SELECT * FROM Salesman;")
    
    mycursor.execute(Salesmen)
  
    for x in mycursor:
        print(x)
    print()
############################################################
def search_dig_disp():
    #2. Search digital displays given a scheduler system 
    db = mysql.connector.connect(host="localhost", user="root",
                                 password="11006nekk", database="proj_1",
                                 auth_plugin='mysql_native_password')
    s = input("enter schedular sytem you want to search: ")
    sCursor = db.cursor() 
    search = ("SHOW" , s,"FROM DigitalDisplay;")
    
    sCursor.execute(search)
    cnt = 1
    for x in sCursor:
        print(cnt," ",x)
        cnt = cnt + 1
    print()


def selection(): 
    print("Database Selection".center(20))
    print("\n1. Display all the digital displays.")
    x = int(input("Enter option here: "))
   
    if x == 1: 
        print("sum")
    if x == 2: 
        search_dig_disp()
        #if x == 3: 
            #insert_New_digDisp()
        #if x == 4: 
            #del_DigDisp()
        #if x == 5: 
            #update_digDisp()
        #x = int(input("press 6 to logout:"))
            
#• 2. Search digital displays given a scheduler system 
#• 3. Insert a new digital display 
#• 4. Delete a digital display 
#• 5. Update a digital display 
# 6. Logout ")



if __name__ == "__main__":
    users = ["root"]
    pswrd = ["11006nekk"]


    title = "Database Login"
    print(title.center(20),"\n")
    
    username = input("input username: ")
    password = input("input password: ")

    if username in users and password in pswrd:
        selection()
        #database_controller(username,password)
    else: 
        print("Try again")
    