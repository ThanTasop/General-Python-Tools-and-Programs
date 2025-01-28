import json


class Teacher:
    def __init__(self, first_name="", last_name="", teacher_id=-1):
        self.first_name = first_name
        self.last_name = last_name
        self.teacher_id = teacher_id

    def from_dict(self, dictio):
        self.first_name = dictio["Name"]
        self.last_name = dictio["Surname"]
        self.teacher_id = dictio["id"]

    def to_dict(self):
        dictio = {"Name": self.first_name,
                  "Surname": self.last_name,
                  "id": self.teacher_id}
        return dictio

    def __str__(self):
        st = ""
        for key, value in self.to_dict().items():
            st += f"{key} : {value}\n"
        return st


class Teachers:
    def __init__(self):
        try:
            with open("Teachers.json", "r") as f:
                teachers = json.load(f)
            self.teachers = []
            for teacher_dict in teachers:
                t = Teacher()
                t.from_dict(teacher_dict)
                self.teachers += [t]
        except FileNotFoundError:
            self.teachers = []

    def save_teachers_data(self):
        list_to_write = []
        for teacher in self.teachers:
            list_to_write += [teacher.to_dict()]
        with open("Teachers.json", "w") as f:
            json.dump(list_to_write, f)

    def next_id(self):
        if not self.teachers:
            return 1001
        else:
            ids = []
            for teacher in self.teachers:
                ids.append(teacher.teacher_id)
            m = max(ids)
            return m+1

    def create_teacher(self, name, surname):
        for teacher in self.teachers:
            if name == teacher.first_name and surname == teacher.last_name:
                print("There is already a teacher with these information")
                return None
        t = Teacher(name, surname, self.next_id())
        self.teachers.append(t)
        print("Account created successfully!\n")
        return t

    def read_teacher(self, teacher_id):
        for teacher in self.teachers:
            if teacher_id == teacher.teacher_id:
                return teacher
        else:
            print("\nThere is no teacher with this id")
            return None

    def update_teacher(self, teacher_id):
        for teacher in self.teachers:
            if teacher_id == teacher.teacher_id:
                print(teacher)
                choice = int(input("Update 1-name, 2-surname: "))
                if choice == 1:
                    teacher.first_name = input("Give new name: ")
                elif choice == 2:
                    teacher.last_name = input("Give new surname: ")
                return teacher

    def delete_teacher(self):
        teacher_id = int(input("\nGive teacher's ID: "))
        for teacher in self.teachers:
            if teacher_id == teacher.teacher_id:
                self.teachers.remove(teacher)
                print(f"{teacher.first_name} {teacher.last_name} deleted successfully.")
                return
        else:
            print("There is no teacher with this ID")


def print_teachers_menu():
    print("--------------------")
    print("   TEACHERS MENU    ")
    print(f"{1}. Create Account")
    print(f"{2}. Print")
    print(f"{3}. Update Account")
    print(f"{4}. Delete Account")
    print(f"{5}. Exit")


def main_teachers():
    t = Teachers()
    while True:
        print_teachers_menu()
        while True:
            choice = input("Choose from 1 to 5: ")
            if choice not in {str(1),str(2),str(3),str(4),str(5)}:
                print(f"You can only choose one of the numbers {1, 2, 3, 4, 5}")
                continue
            if choice in {str(1),str(2),str(3),str(4),str(5)}:
                break
        if choice == str(5):
            t.save_teachers_data()
            print("\nBye Bye")
            break
        if choice == str(1):
            name = input("Give first name: ")
            surname = input("Give surname: ")
            print(t.create_teacher(name, surname))
        if choice == str(4):
            t.delete_teacher()
        if choice == str(2):
            id = int(input("Give teacher's id: "))
            teacher = t.read_teacher(id)
            print("\n")
            if teacher in t.teachers:
                for key, value in teacher.to_dict().items():
                    print(f"{key}: {value}")
        if choice == str(3):
            id = int(input("Give teacher's id: "))
            print(t.update_teacher(id))


main_teachers()



