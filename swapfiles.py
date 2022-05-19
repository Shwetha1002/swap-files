

def swapFileData():
    filename = input("enter the name of the first file : ")
    filenameTwo = input("now enter the second! : ")
     
    with open(filename, 'r') as a:
        data_a = a.read()

    with open(filenameTwo, 'r') as b:
        data_b = b.read()
    
    with open(filename, 'w') as a:
        a.write(data_b)

    with open(filenameTwo, 'w') as b:
        b.write(data_a)
        
    print("file contents are swapped!")


swapFileData()
