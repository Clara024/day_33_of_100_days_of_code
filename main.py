yellow = "\033[33m"
red = "\033[31m"
default = "\033[0m"
list = []
def printList( ):
    print()
    for item in list:
     print(item)
     print( )
while True:
    print("{}TO-DO LIST MANAGER{}".format(yellow,default))
    user = input("Do you wish to add, view or edit from the list?:")
    if user == "add":
        item = input("What do you wish to add?:")
        list.append(item)
        print(item)
    elif user == "view": 
        printList()
    elif user == "edit":
        item = input("What do you wish to remove?:")
        if item in list:
            list.remove(item)
    else:
        print("{}It is not in the to-do list{}".format(red,default))
