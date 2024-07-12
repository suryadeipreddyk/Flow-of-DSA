class dynamicArray():

    def __init__(self):
        self.capacity = 1 #initial allocated memory to the array
        self.arr = [None] * self.capacity 
        self.length = 0

    def reSize(self):
        self.capacity *= 2
        new_arr = [None] * self.capacity
        for i in range(self.length):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
    
    def printArr(self):
        for i in range(self.length):
            print(self.arr[i], end = ' ')
        print()

    def insertArr(self, elem): #Insert array at the next open position
        for i in elem:
            if self.length >= self.capacity:
                self.reSize()
            self.arr[self.length] = i
            self.length += 1
        self.printArr()
        return self.length
    
    def removeEnd(self): #Remove from the end of an array
        if self.length > 0:
            self.arr[self.length - 1] = None
            self.length -= 1
        self.printArr()
        return self.length

    def insertMiddle(self, elem, pos): #Making space at a specific positing by shifting elements to the right and inserting in the middle
        if self.length + 1 >= self.capacity:
            self.reSize()
        for i in range(self.length - 1, pos -1 , -1):
            self.arr[i + 1] = self.arr[i]
        self.arr[pos] = elem    
        self.length += 1
        self.printArr()
        return self.length
    
    def removeMiddle(self, pos): #Removing from the middle of an array and shifting the elemnts to the left
        
        for i in range(pos, self.length - 1):
            self.arr[i] = self.arr[i + 1]
        self.arr[self.length - 1] = None
        self.length -= 1
        self.printArr()
        return self.length
    
    def menu(self):
        print("Welcome to Dynamic Array")
        print()
        print("1. Insert the array at the next open position")
        print('2. Remove from the last open position')
        print("3. Insert in the middle") #Make space by shifting the elements to the right
        print("4. Remove from middle") #Remove the element from middle and shift the elements to the left
        print("5. Exit")
        print("\n")
    
    def choice(self):
        while True:
            self.menu()
            try: 
                user_choice = int(input("Choose option from (1 - 5): "))
                if 1 <= user_choice <= 5:
                    match user_choice:
                        case 1:
                            self.elem = list(map(int, input("Enter the elements into array separated by spaces: ").split()))
                            self.length = self.insertArr(self.elem)
                            continue

                        case 2:
                            self.length = self.removeEnd()
                            continue

                        case 3:
                            self.elem = int(input("Enter the element: "))
                            self.pos = int(input("Enter the position: "))
                            self.length = self.insertMiddle(self.elem, self.pos)
                            continue
                        case 4:
                            self.pos = int(input("Enter the position to remove from array: "))
                            self.length = self.removeMiddle(self.pos)
                            continue
                        case 5:
                            print("Exiting the progam.....!")
                            return SystemExit
            except ValueError:
                print("Please choose an option from 1 - 5")

Darr = dynamicArray()
n = int(input("Enter the number of elements: "))
elements_array = [int(input(f"Enter the elements into array {i + 1}: ")) for i in range (n)]
Darr.length = Darr.insertArr(elements_array)
Darr.choice()