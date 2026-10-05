import time

class_members = ["Matthijs", "Yuri", "Tigo", "Cas B", "Cas H", "Luna", "Daniel", "Max", "Jaiden", "Ensar", "Levi", "Maurits", "Wolf", "Luca"]


def show_class():
    print("Class:")
    for member in class_members:
        print(f"- {member}")


print("Loading program", end="")
for _ in range(3):
    time.sleep(0.5)
    print(".", end="", flush=True)
time.sleep(3)
print("\nKlaar!")

while True:
    choice = input("""
        Choose an option.
        1. Show Class
        2. Add Classmember
        3. Remove classmember
        4. Edit class
        5. Stop
        """).strip()

    if choice == "1":
        show_class()
    elif choice == "2":
        new_member = input("Enter the new classmember: ").strip()
        if new_member:
            class_members.append(new_member)
            print(f"{new_member} has been added.")
        else:
            print("The name cannot be empty.")
    elif choice == "3":
        member_to_remove = input("Enter the classmember to remove: ").strip()
        if member_to_remove in class_members:
            class_members.remove(member_to_remove)
            print(f"{member_to_remove} has been removed.")
        else:
            print("That classmember was not found.")
    elif choice == "4":
        member_to_edit = input("Enter the classmember to edit: ").strip()
        if member_to_edit in class_members:
            edited_member = input("Enter the new name: ").strip()
            if edited_member:
                member_index = class_members.index(member_to_edit)
                class_members[member_index] = edited_member
                print(f"{member_to_edit} has been changed to {edited_member}.")
            else:
                print("The name cannot be empty.")
        else:
            print("That classmember was not found.")
    elif choice == "5":
        print("Program stopped.")
        break
    else:
        print("Invalid choice. Choose a number from 1 to 5.")