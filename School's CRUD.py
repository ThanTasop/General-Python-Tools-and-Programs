from mod_pupils import *
from mod_teachers import *

while True:
    print("       MENU      ")
    print(f"{1}. Pupils Details")
    print(f"{2}. Teachers Details")
    print(f"{3}. Exit")
    choice = input("Press 1, 2 or 3: ")
    if choice == str(1):
        main_pupils()
    elif choice == str(2):
        main_teachers()
    else:
        print("Bye Bye")
        break
