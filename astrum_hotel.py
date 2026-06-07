list_guests=[]
def add_guest():
    name=input("Enter the name: ")
    room=input("Enter the number of the room: ")
    type_of_room=input("Choose the type of room: ")
    for guest in list_guests:
        if guest["Room"] == room:
            print("This room is already occupied!")
            return


    guest={
        "Name": name,
        "Room": room,
        "Room type":type_of_room
    }
    list_guests.append(guest)
    print("Guest added successfully.")
def remove_guest():
    name=input("Enter the name: ")
    for guest in list_guests:
        if guest["Name"]==name:
            list_guests.remove(guest)
            print("Guest removed successfully")
            return
    print("Not found such name in list of guests")
def list_of_guests():
    if not list_guests:
        print("List of guests is empty")
        return
    print("\nName\t\tRoom\t\tType of room")
    print("-" * 30)
    for guest in list_guests:
        print(f'{guest["Name"]}\t\t\t{guest["Room"]}\t\t\t{guest["Room type"]}')

while True:
    print("HI! Welcome to Astrum Hotel")
    print("Choose the command: ")
    print("1 - add the guest")
    print("2 - delete the guest from list")
    print("3 - list of guests")
    print("0 - log out")
    choice = input("Choose the command:")
    if choice=="1":
        add_guest()
    elif choice=="2":
        remove_guest()
    elif choice=="3":
        list_of_guests()
    elif choice=="0":
        print("The program is completed")
        break
    else:
        print("Wrong command! Please try again")