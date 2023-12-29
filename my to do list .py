tasks = []

def display_menue():
  print("Menue: ")
  print("1. Add")
  print("2. Update")
  print("3. Delete")
  print("4. View")
  print("5. Exit")

def Add():
  task = input("Please enter a task: ")
  tasks.append(task)
  print("Task added successfully!!")

def Update():
  index = int(input("Enter the index of the task to update: "))
  if index >= 0 and index < len(tasks):
    new_task = input("Enter the new task: ")
    tasks[index] = new_task
    print("Task updated successfully!!")
  else:
    print("Invalid index!!")

def Delete():
  index = int(input("Enter the index of the task to delete: "))
  if index >= 0 and index < len(tasks):
    del tasks[index]
    print("Task deleted successfully!!")
  else:
    print("Invalid index!!")

def View():
  print("Tasks: ")
  for index, task in enumerate(tasks):
      print(f"{index}. {task}")

while True:
  display_menue()
  choice = int(input("Enter your choice: "))

  if (choice == 1):
     Add()
  elif (choice == 2):
      Update()
  elif (choice == 3):
      Delete()
  elif (choice == 4):
      View()
  elif (choice == 5):
      exit
  else:
      print("Invalid input. Please try again.")

  print("Goodbye")
