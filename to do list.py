# simple to do list app using python

tasks = []

while True:
    print("\n------ TO-DO LIST ------")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")

    choice = input("Choose option (1-5): ")

    if choice == "1":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                status = "Done" if tasks[i][1] else "Not Done"
                print(f"{i+1}. {tasks[i][0]}  - [{status}]")

    elif choice == "2":
        new_task = input("Enter your task: ")
        tasks.append([new_task, False])
        print("Task added!")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to mark.")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i][0]}")
            try:
                done_index = int(input("Enter task number to mark done: ")) - 1
                if 0 <= done_index < len(tasks):
                    tasks[done_index][1] = True
                    print("Marked as done!")
                else:
                    print("Invalid task number.")
            except:
                print("Please enter a number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("Nothing to delete.")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i][0]}")
            try:
                del_index = int(input("Enter task number to delete: ")) - 1
                if 0 <= del_index < len(tasks):
                    removed = tasks.pop(del_index)
                    print(f"Deleted: {removed[0]}")
                else:
                    print("Invalid task number.")
            except:
                print("Please enter a number.")

    elif choice == "5":
        print("Thanks for using To-Do List. Bye!")
        break
    else:
        print("Please choose between 1 to 5.")
