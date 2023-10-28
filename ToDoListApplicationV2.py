file = input("Enter the name of the file you want to open: ")
try:
    tasks = open(file, "r+")
    print("Opened existing file: {}" .format(file))
except FileNotFoundError:
    tasks = open(file, "w+")
    print("Created new file: {}" .format(file))

def printMenu():
    print("\n1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Quit\n")

def addTask():
    name = input("Enter task name: ")
    dueDate = input("Enter task due date: ")
    tasks.write("{}, {}\n" .format(name, dueDate))
    print("Task \"{}\" added to the list." .format(name))
    
def viewTasks():
    tasks.seek(0)
    count = 1
    line = tasks.readline().rstrip()
    while line != "":
        list = line.split(",")
        print("{}. Task: {}, Due: {}" .format(count, list[0], list[1]))
        count +=  1
        line = tasks.readline().rstrip()
        
def removeTask():
    name = input("Enter the name of the task you want to remove: ")
    tasks.seek(0)
    lines = tasks.readlines()
    tasks.seek(0)
    tasks.truncate()
    for line in lines:
        if not line.startswith(name):
            tasks.write(line)
    
            
    

def main():
    menu = {"1" : addTask, 
        "2" : viewTasks,
        "3" : removeTask,
        "4" :lambda: (tasks.close(), exit())}
    while True:
        printMenu()
        choice = input("Enter your choice: ")
        if choice in menu:
            menu[choice]()
        else:
            print("Invalid input. Please try again.")
             
main()
