file_path = r"C:\Users\sakshi bhosale\Desktop\Task21stDec.txt"
while True:
    operation=input("Enter your choice(R:Read W:Write S:Search): ") 
    if operation == "R":
        print("You have selected : Read Operation ")
        with open(file_path,"r") as file:
            content = file.read()
            print(content)
        print("Read Operation Done Successfully")
        print()
    elif operation == "W":
        print("You have selected: Write Operation")
        text_to_write = input("Enter the text you want to write to the file: ")  
        try:
            with open(file_path, "a") as file:
                file.write('\n' + text_to_write + '\n')  
            print("\nWrite Operation Done Successfully")
        except FileNotFoundError:
            print("The file does not exist at the specified path.")
            print()
    elif operation == "S":
        print("You have selected : Search Operation ")
        keyword=input("Enter the text you want to search: ")
        with open(file_path,"r") as file:
            for line in file:
                if keyword.lower() in line.lower():
                    print(line.strip())
                    print("Search for the keyword ",keyword," completed")
            if keyword.lower() not in line.lower():
                print("Sorry! searched keyword doesn't exist in this file")
        print("\nSearch Operation Done Successfully")
        print()
    else:
        print("\nInvalid Choice!!! , Please enter valid choice")



        
