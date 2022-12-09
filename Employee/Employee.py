users = []



def Home():
    option = int(input("""
    1: Add Employee
    2: Get Employee Amount
    3: Get Employees
    4: Exit
    """))
    if option == 1:
        Adduser()
    elif option == 2:
        GetUserAmount()
    elif option == 3:
        GetUsers()
    elif option == 4:
        exit()




def exit():
    quit()

def GetUsers():
    with open("users.txt","r") as i:
        print(i.read())
        i.close()
        Home()

def GetUserAmount():
    with open("users.txt","r") as i:
        for count, line in enumerate(i):
         pass
        print('Total Users: ', count + 1)
        Home()

def Adduser():
    FirstName = input("First Name: ")
    LastName = input("Last Name: ")
    Age = input("Age: ")
    Rank = input("Rank: ")
    user = FirstName + " " + LastName + " " + Age + " " + Rank
    print(f"User added:  {user}")
    users.append(user)
    with open("users.txt","a") as Ia:
        for items in users:
            Ia.write(items)
            Ia.write("\n")
            Ia.close()
    users.clear()
    Home()

if __name__ =="__main__":
    Home()
