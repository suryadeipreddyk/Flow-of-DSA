def printArr(arr, length): #Print array function
    
    for i in range(0, length):
        print(arr[i], end = ' ')
    print("\n")

def insertArr(arr, elem, length, capacity): #Base program for inserting elements into array

    if length >= capacity: #Insert at open position in an array
        print("Array is at full capaity, cannot insert the element \n")
    elif length < capacity:
        arr[length] = elem
        length += 1
    return length

def removeEnd(arr, length): #Remove from end of an array

    if length > 0:
        arr[length - 1] = None
        length -= 1
    else:
        print("Array is empty, Could not remove from end")
    return length

def insertMiddle(arr, length, capacity): #Insert from start to last before position into array

    if length >= capacity:
        print(f'{printArr(arr, length)} , Value index out of range')

    elif length > 0:
        pos = int(input("Enter the position: "))
        if pos > capacity:
            print("Position is greater than capacity")
        else:
            elem = int(input("Enter the element to insert into array: "))
            for i in range(length-1, pos-1, -1): 
                arr[i + 1] = arr[i]
            arr[pos] = elem
            length += 1
    return length

def removeMiddle(arr, pos, length, capacity): #Remove from start to last before position into array
    
    if 0 < pos < capacity:   
        for i in range(pos, length):
            arr[i-1] = arr[i]
        arr[length-1] = None
        length -= 1
    else:
        print("Position out of range")
    return length

def menu():
    print("1. Insert at the next open position") #Insert at open position in an array
    print("2. Remove from the last position in the array") #Remove from end of an array
    print("3. Insert in the middle") #Insert from start to last before position into array, if the array has an open position.  #Right Shift Elements
    print("4. Remove from the middle") #Remove from start to last before position into array                                    #Left Shift Elements
    print("5. Exit")
    print()
    return

def choice():
    global length
    while True:
        menu()
        user_choice = input("Please choose an option from (1-5):")   

        try:
            if not (1 <= int(user_choice) <= 5 ):
                print("Enter an input ranging from 1-5")
                print()
                continue

            user_int =int(user_choice)

            match user_int:
                case 1:
                    elem = int(input("Enter the element at next open position:"))
                    length = insertArr(arr, elem , length, capacity)
                    printArr(arr, length)
                    continue
                    #return length
                    
                case 2:
                    length = removeEnd(arr, length)
                    printArr(arr, length)
                    continue
                    #return length
                    
                case 3:
                    printArr(arr, length)
                    length = insertMiddle(arr, length, capacity)
                    printArr(arr, length)
                    continue
                    #return length
                    
                case 4:
                    printArr(arr, length)
                    pos= int(input("Enter the position to remove from array: "))
                    length = removeMiddle(arr, pos, length, capacity)  
                    printArr(arr, length)
                    continue
                    #return length
                                  
                case 5:
                    print("Exiting the Program.....!")
                    return

                case _:
                    continue  
                   
        except ValueError:
                print('Enter a valid data type')
                print()
                continue
    
capacity = int(input("Allocate the memory to array: "))
arr = [None] * capacity
length = 0

n = int(input("Enter the number of elements: "))

if 1 <= n <= capacity:
    elements_array = [int(input(f'Elements at {i + 1} position: ')) for i in range(n)]

    for elem in elements_array:
        length = insertArr(arr, elem, length, capacity)
    printArr(arr, length)
else:
    print("Elements out of range")
    raise SystemExit

if __name__ == "__main__":
    choice()