import time

"""
This is a simple To-Do list without using Tkinter 
Four options are there in this program 
 add, delete, view, exit
time library is added to slow down the viewing process

"""
print("Welcome To your To-Do list \n")

def todo(lst):

  print(""" Please Select one :
            1. Add an item
            2. Delete an item
            3. View Items
            4. Exit
          """)
  s1=int(input("Enter your choice-->"))

  while True:

    if s1==1:

      s2=input("Enter the Item to add-->") 
      lst.append(s2)
      todo(lst)

    elif s1==2:
      print("-----------------------")

      for i in range(len(lst)):
        print(f"{i+1}.{lst[i]}")

      print("-----------------------")

      time.sleep(2.5)
      s2=int(input("Which item to delete-->"))

      for j in range(len(lst)):
        if (s2-1)==j:
          lst.remove(lst[j])

        else:
          continue

      print("-----Updated list------")
      print("-----------------------")

      for i in range(len(lst)):
        print(f"{i+1}.{lst[i]}")

      print("-----------------------")
      time.sleep(2.5)

      todo(lst)

    elif s1==3:
      print("-----------------------")

      for i in range(len(lst)):
        print(f"{i+1}.{lst[i]}")

      print("-----------------------")

      time.sleep(2.5)
      todo(lst)

    elif s1==4:
      print("-------LIST------------")

      for i in range(len(lst)):
        print(f"{i+1}.{lst[i]}")

      print("-----------------------")
      print("GET YOUR WORK COMPLETE")
      time.sleep(2.5)
      exit()


lst=[]
todo(lst)