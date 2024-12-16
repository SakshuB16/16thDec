#Question1
rows = 7
for i in range(rows, 0, -1):  
    print("*" * i)  


#Question2
rows = 5
for i in range(1, rows + 1):  
    spaces = " " * (rows - i)  
    stars = "*" * i  
    print(spaces + stars)  


#Question3
rows = 5
for i in range(1, rows + 1):  
    pattern = ""
    for j in range(i):  
        if j % 2 == 0:
            pattern += "1"  
        else:
            pattern += "0"  
    print(pattern)  


#Question4
rows = 5
for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    pattern = ""
    for j in range(i):
        if j % 2 == 0:
            pattern += "1"
        else:
            pattern += "0"
    print(spaces + pattern)



#Question5
rows = 5
for i in range(rows, 0, -1):  
    dashes = " " * (rows - i)
    stars = "*" * i
    print(dashes + stars)
