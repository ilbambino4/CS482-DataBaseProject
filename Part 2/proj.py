import mysql.connector
import sys

#connects to the sql database
mydb = mysql.connector.connect(
host="localhost",
user="dbuser",
password="Iwilldowell",
database="cs482502"
)


#Takes qeustion number to be solved as a parameter and calls appropriate function to solve the question
def main(num, ques):
    if(num == '1'):
        if (ques == ""):
            print("A further parameter is needed for this question")
        else:
            question1(ques)
    elif(num == '2'):
        if (ques == ""):
            print("A further parameter is needed for this question")
        else:
            question2(ques)
    elif(num == '3'):
        if (ques != ""):
            print("No further parameter needed for this question")
        else:
            question3()
    elif(num == '4'):
        if (ques == ""):
            print("A further parameter is needed for this question")
        else:
            question4(ques)
    elif(num == '5'):
        if (ques != ""):
            print("No further parameter needed for this question")
        else:
            question5()
    elif(num == '6'):
        if (ques == ""):
            print("A further parameter is needed for this question")
        else:
            question6(ques)
    elif(num == '7'):
        if (ques != ""):
            print("No further parameter needed for this question")
        else:
            question7()
    elif(num == '8'):
        if (ques != ""):
            print("No further parameter needed for this question")
        else:
            question8()
    else:
        print("Invalid question number provided, must be 1-8")


#solves question 1
def question1(streetName):
    mycursor = mydb.cursor()
    query="SELECT * FROM SITE WHERE ADDRESS LIKE '%"+streetName+"%'"
    mycursor.execute(query)

    myresult = mycursor.fetchall()

    if (len(myresult) != 0):
        print("{:<16} {:<15} {:50} {:10}".format('Site Code', 'Type', 'Address', 'Phone Number'))
        print("------------------------------------------------------------------------------------------------------------")

        for x in myresult:
            print("{:<16} {:<15} {:50} {:10}".format(x[0], x[1], x[2], x[3]))
    else:
        print("No Results Found...")
    print()


#solves question 2
def question2(SchedSystem):
    models=[]
    
    mycursor = mydb.cursor()
    query="SELECT * FROM DIGITALDISPLAY WHERE SCHEDULERSYSTEM='"+SchedSystem+"'"
    mycursor.execute(query)

    myresult = mycursor.fetchall()

    if (len(myresult) != 0):
        print("{:<16} {:<15}".format('Serial Number', 'Model Number'))
        print("--------------------------------")

        for x in myresult:
            print("{:<16} {:<15}".format(x[0], x[2]))

            if (x[2] not in models):
                models.append(x[2])
        
        print()

        print("{:<15} {:<15}".format('Model Number', 'Available Tech Support Employees'))
        print("--------------------------------------------------")

        for x in models:
            query="SELECT EMPID FROM SPECIALIZES WHERE MODELNO='"+x+"'"
            mycursor.execute(query)
            myresult = mycursor.fetchall()
            
            temp=str(myresult[0])
            temp=temp[1:len(temp)-2]
            
            print("{:<16}".format(x), end='')
            
            query="SELECT NAME FROM TECHNICALSUPPORT WHERE EMPID='"+temp+"'"
            mycursor.execute(query)
            myresult = mycursor.fetchall()
            for i in myresult:
                print(i[0], end=',')
            print()

        print()
        
    else:
        print("No Results Found...")
    print()


#solves question 3
def question3():
    #arrays to keep track of names, and repeating names pulled from the database
    names=[]
    namesRepeat=[]
    #bool to keep track of needed spacing
    spacing=False

    #query to pull names from salesman table
    mycursor = mydb.cursor()
    query="SELECT NAME FROM SALESMAN"
    mycursor.execute(query)

    #assigns names from DB to arrays
    for x in mycursor:
        #stringifies each name
        name=str(x)

        #splices string to get rid of parenthesis and commas
        name=name[2:len(name)-3]

        #appends names to appropriate arrays
        if name not in names:
            names.append(name)
        else:
            namesRepeat.append(name)

    
    print("{:<16} {:<4}".format('Names', 'cnt'))
    print('---------------------')

    #loops through names printing as it goes
    for i in names:
        #checks to see if name repeats
        if i in namesRepeat:
            #pulls all versions of the repeated name from the DB
            query="SELECT * FROM SALESMAN WHERE NAME='"+i+"'"
            mycursor.execute(query)

            #keeps track of how many times a name repeats
            n=1

            #finds out how many times a name is repeated
            for j in namesRepeat:
                if j == i:
                    n+=1

            #prints name and its repeat count
            print("{:<16} {:<4}".format(i, n),end='')

            #prints all the versions of the name
            for x in mycursor:
                if n!=1:
                    print(x, end=',')
                    n-=1
                else:
                    print(x)
        else:
            #prints non repeating names
            print("{:<16} {:<8}".format(i, '1'))



#solves question 4
def question4(PhoneNo):
    mycursor = mydb.cursor(buffered = True)
    num = input("enter client number: ")

    sql = ("select * \
        from Client \
        where phone = %s;")

    val = (num,)

    mycursor.execute(sql, val)
    myresult =  mycursor.fetchall()

    if(len(myresult) == 0): 
        print("No result found...")
    for x in myresult: 
        print(x)

#solves question 5
def question5():
    mycursor = mydb.cursor(buffered = True)
    sql = "select amd.empId, amd.name, admW.hours\
       from AdmWorkHours as admW, Administrator as amd\
       where amd.empId = admW.empId\
       order by hours asc;"
       
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    print("empID\t empNames\t\t total_working_hours")
    print("----------------------------------------------")

    for x in myresult:
        print(x[0], "\t\t", x[1], "\t\t", x[2])
        
    print()


#solves question 6
def question6(ModelNo):
    mycursor = mydb.cursor(buffered = True)
    userModelNo = ModelNo
    print()

    sql = "select name\
        from TechnicalSupport as ts, Specializes as s\
        where s.modelNo = %s and ts.empID = s.empID;"
        
    val = (userModelNo,)

    mycursor.execute(sql, val)

    myresult = mycursor.fetchall()

    print("Name")
    print("--------------")
    if len(myresult) == 0:
        print("No Results Found...")
    for x in myresult:
        if not x:
            print("No result")
        else:
            print(x[0])
    print()


#solves question 7
def question7():
    mycursor = mydb.cursor(buffered = True)
    sql = "select s.name, avg(p.comissionRate) as avg\
       from Salesman as s, Purchases as p\
       where s.empID = p.empID\
       group by s.name;"
       
    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    print("Name\t\tAvgComissionRate")
    print("--------------")
    for x in myresult:
        print(x[0], "\t\t", x[1])
    print()


#solves question 8
def question8():
    mycursor = mydb.cursor(buffered = True)
    adminCnt = ("SELECT count(empID) FROM Administrator;")
    mycursor.execute(adminCnt)
    myresult1 = mycursor.fetchall()

    Salesmen = ("SELECT count(empID) FROM Salesman;")
    mycursor.execute(Salesmen)
    myresult2 = mycursor.fetchall()

    Technicians = ("SELECT count(empID) FROM TechnicalSupport;")
    mycursor.execute(Technicians)
    myresult3 = mycursor.fetchall()

    print("Role             cnt")
    print("------------------")
    print("Administrator:\t", myresult1[0][0])
    print("Salesman:     \t", myresult2[0][0])
    print("Technicians:  \t",myresult3[0][0]) 



#pulls arguments and calls main
questionNumber = str(sys.argv[1])
questionParam = ""

#pulls second argument after question number
if (len(sys.argv) > 2):
    for i in range(len(sys.argv)):
        if i > 1:
            if (i != len(sys.argv)-1):
                questionParam+=sys.argv[i]+" "
            else:
                questionParam+=sys.argv[i]
    
main(questionNumber, questionParam)

if(mydb.is_connected()):
    mydb.close()
    #mycursor.close()
    print("MySQL connection is closed")
