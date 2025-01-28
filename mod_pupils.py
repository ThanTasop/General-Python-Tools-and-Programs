import json

def init_pupils_data():
    global pupils
    try:
        with open("Pupils.json", "r") as f:
            pupils = json.load(f)
    except FileNotFoundError:
        pupils = []


def save_pupils_data():
    with open("Pupils.json", "w") as f:
        json.dump(pupils, f)
def print_menu():
    print("===============")
    print("   Pupils   Menu    ")
    print(f"{1}. Create Account")
    print(f"{2}. Print")
    print(f"{3}. Update Account")
    print(f"{4}. Delete Account")
    print(f"{5}. Exit")

def createpupil():
    name = input("Name: ") # elegxos gia mia leksh mono me grammata
    surname = input("Surname: ")# to idio
    father_name = input("Father Name: ")#to idio
    a = 0
    for i in range(len(pupils)):
        if name==pupils[i]["Name"] and surname==pupils[i]["Surname"]\
            and father_name==pupils[i]["Father Name"]:
            print("There is already a pupil with these informations")
            a = input("Do you want to continue?")
            while a not in {"Yes","No"}:
                a = input("Press Yes or No: ")
            break
    if a == "No":
        return
    age = input("Age: ") # tha borouse na bei elegxos gia hlikies
    clas = input("Class: ") #episis edw gia 1-6
    identnumb = int(input("ID Number: ")) # edw gia eksapsifio kserw gw h kati
    pupils.append({"id":len(pupils)+1000, "Name":name, "Surname":surname, "Father Name":father_name, "Age":age, "Class":clas, "ID Number":identnumb})
    print("Account created successfully!")
    for key, value in pupils[len(pupils)-1].items():
        print(f"{key} : {value}")


def deletepupil():
    name = input("Give me the name of the pupil: ")
    surname = input("Give me the surname of the pupil: ")  # to idio
    father_name = input("Give me the father's name of the pupil: ")
    age = input("Give me the age of the pupil: ")
    deleteindex=-1
    for i in range(len(pupils)):
        if name == pupils[i]["Name"] and surname == pupils[i]["Surname"]\
            and father_name == pupils[i]["Father Name"] and age == str(pupils[i]["Age"]):
            deleteindex = i
            print("Pupil found")
            break
    if deleteindex == -1:
        print("Pupil not found, repeat process")
        return
    pupils.pop(deleteindex)
    print("Pupil deleted succesfully")



def printpupil():
    while True:
        who = input("Give ID Number of pupil: ")
        if who.isdigit() == False:
            print("You need to give a number (digits): ")
            continue
        who = int(who)
        flag = False
        for i in range(len(pupils)):
            if pupils[i]["ID Number"] == who:
                who = i
                flag = True
                break
        if flag == True:
            break
        else:
            print("You gave wrong ID number, try again please")
    for key, value in pupils[who].items():
        print(f"{key} : {value}")

def listofpupils():
    l = []
    for i in range(len(pupils)):
        l.append(pupils[i])
    return l


def printmenu():
    print("      SUBMENU (Print)       ")
    print("1. Print pupil")
    print("2. Print details of all pupils")
    print("3. Print names of all pupils")
    while True:
        choose = input("Choose from 1 to 3: ")
        if choose not in {str(1), str(2), str(3)}:
            print(f"You can only choose one of the numbers {1, 2, 3}")
            continue
        break
    return choose
def printnamesofpupils():
    for i in range(len(pupils)):
        print("---------------")
        print(pupils[i]["Name"], end=" ")
        print(pupils[i]["Father Name"][0] + ".", end=" ")
        print(pupils[i]["Surname"], end=" ")
        print("")


def printdetailsofpupils():
    for i in range(len(pupils)):
        print("---------------")
        for key, value in pupils[i].items():
            print(f"{key} : {value}")

def search_pupil_by_surname(surname):
    lis = []
    for i in range(len(pupils)):
        if pupils[i]["Surname"] == surname:
            lis.append(pupils[i])
    if len(lis) >= 1:
        return lis
    else:
        return "This Surname does not exist"

def update_pupil(lista):
    choose = input("Give the ID of the pupil")
    while True:
        if choose.isdigit() == False:
            choose = input("ID must be a number, try again")
            continue
        flag = False
        for pupil in lista:
            if int(choose) == pupil["ID Number"]:
                choose = pupil
                flag = True
                break
        if flag:
            break
        else:
            choose = input("You pressed the ID wrong, try again please: ")
    print("=================================")
    print("Pupil's details are the following")
    print("")
    for key, value in choose.items():
        if key != "ID Number":
            print(f"{key} : {value}")
    while True:
        change = input("Which field you want to change?")
        while change not in choose.keys():
            change = input("Press Name, Surname, Father Name, Age or Class: ")
        print("Enter new value")
        new = input(f"{change}: ")
        choose[change]=new
        exitorno = input("Do you want to change anthything else? Press yes if u want to, otherwise press no: ")
        if exitorno == "no":
            break
    print("Changes are done succesfully")
    for key, value in choose.items():
        if key != "ID Number":
            print(f"{key} : {value}")

def update():
    print("----------------------------")
    print("      SUBMENU (Update)      ")
    print("1. Search pupil with Surname")
    print("2. Search pupil with ID")
    while True:
        choose = input("Choose option 1 or 2: ")
        if choose not in {str(1),str(2),str(3)}:
            print(f"You can only choose one of the numbers {1,2,3}")
            continue
        break
    if choose == str(1):
        surname = input("Give Surname: ")
        if type(search_pupil_by_surname(surname)) == str:
            print(search_pupil_by_surname(surname))
        elif len(search_pupil_by_surname(surname)) >= 2:
            print("There are more than one pupils with this Surname")
            print("This is the list of these pupils")
            for pupil in search_pupil_by_surname(surname):
                print("-----------")
                for key, value in pupil.items():
                    print(f"{key} : {value}")
            update_pupil(search_pupil_by_surname(surname))
        elif len(search_pupil_by_surname(surname))==1:
            update_pupil(search_pupil_by_surname(surname))
    if choose == str(2):
        update_pupil(listofpupils())

def main_pupils():
    init_pupils_data()
    while True:
        print_menu()
        while True:
            choice = input("Choose from 1 to 5: ")
            if choice not in {str(1), str(2), str(3), str(4), str(5)}:
                print(f"You can only choose one of the numbers {1, 2, 3, 4, 5}")
                continue
            if choice in {str(1), str(2), str(3), str(4), str(5)}:
                break
        if choice == str(5):
            save_pupils_data()
            print("Bye Bye")
            break
        if choice == str(1):
            createpupil()
        if choice == str(4):
            deletepupil()
        if choice == str(2):
            choose = printmenu()
            if choose == str(1):
                printpupil()
            if choose == str(2):
                printdetailsofpupils()
            if choose == str(3):
                printnamesofpupils()
        if choice == str(3):
            update()


