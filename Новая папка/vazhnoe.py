print("-----------Автоматические ворота--------")
is_open = False
while True:
    command = input("Command ").lower()
    if command == "open":
        if is_open:
            print("it is already open")
        else:
            print("Opening")
        is_open = True    
    elif command == "close":
        if is_open:
            print("Closing")
        else:
            print("it is already closed")
        is_open = False              
    elif command == "help":
        print("""Help menu:
        open
        close
        stop """)
    elif command == "stop":
        print("Stopping")
        break
    else:
        print("Incorrect")
print("Stopped")          