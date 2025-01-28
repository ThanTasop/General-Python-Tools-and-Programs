import json



def init_teachers_data():
    global teachers
    try:
        with open("Teachers.json", "r") as f:
            teachers = json.load(f)
    except FileNotFoundError:
        teachers = []


def save_teachers_data():
    with open("Teachers.json", "w") as f:
        json.dump(teachers, f)

def create_teacher(name, surname):
    for teacher in teachers:
        if name == teacher["Name"] and surname == teacher["Surname"]:
            print("There is already a teacher with these informations")
            return None
    t = {"id": len(teachers)+1001, "Name": name, "Surname": surname}
    teachers.append(t)
    print("Account created successfully!")
    for key, value in teachers[len(teachers)-1].items():
        print(f"{key} : {value}")
    return t


def read_teacher(id):
    for teacher in teachers:
        if int(id) == teacher["id"]:
            return teacher
    else:
        print("There is no teacher with this id")
        return None


def update_teacher(id, key, new_value):
    for teacher in teachers:
        if int(id) == teacher["id"]:
            teacher[key] = new_value
            return


def delete_teacher(id):
    for i in range(len(teachers)):
        if int(id) == teachers[i]["id"]:
            teachers.pop(i)
            print("Teacher deleted successfully")
            return
    else:
        print("There is no teacher with this id")
        return None


def print_teachers_menu():
    print("--------------------")
    print("   TEACHERS MENU    ")
    print(f"{1}. Create Account")
    print(f"{2}. Print")
    print(f"{3}. Update Account")
    print(f"{4}. Delete Account")
    print(f"{5}. Exit")


def main_teachers():
    init_teachers_data()
    while True:
        print_teachers_menu()
        while True:
            choice = input("Choose from 1 to 5: ")
            if choice not in {str(1),str(2),str(3),str(4),str(5)}:
                print(f"You can only choose one of the numbers {1,2,3,4,5}")
                continue
            if choice in {str(1),str(2),str(3),str(4),str(5)}:
                break
        if choice == str(5):
            save_teachers_data()
            print("Bye Bye")
            break
        if choice == str(1):
            name = input("Give first name: ")
            surname = input("Give surname: ")
            create_teacher(name, surname)
        if choice == str(4):
            id = input("Give teacher's id: ")
            delete_teacher(id)
        if choice == str(2):
            id = input("Give teacher's id: ")
            teacher = read_teacher(id)
            if teacher in teachers:
                for key, value in teacher.items():
                    print(f"{key}: {value}")
        if choice == str(3):
            id = input("Give teacher's id: ")
            flag = False
            for teacher in teachers:
                if teacher["id"] == int(id):
                    flag = True
                    break
            if flag == False:
                print("There is no teacher with this id")
            else:
                name = input("Give the new name: ")
                surname = input("Give the new surname: ")
                update_teacher(id, "Name", name)
                update_teacher(id, "Surname", surname)
                print("Teacher Updated succesfully")
                for key, value in teacher.items():
                    print(f"{key}: {value}")

