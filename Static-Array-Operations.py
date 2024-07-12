class staticArray:

    def __init__(self):
        self.capacity = int(input("Allocate memory to the array: "))
        self.arr = [None] * self.capacity
        self.length = 0

    def menu(self):
        print("1. Insert at the next open position") #Insert at open position in an array
        print("2. Remove from the last position in the array") #Remove from end of an array
        print("3. Insert in the middle") #Insert from start to last before position into array, if the array has an open position.  #Right Shift Elements
        print("4. Remove from the middle") #Remove from start to last before position into array                                    #Left Shift Elements
        print("5. Exit")
        print()
        return
    
    def choice(self):

        while True:
            self.menu()
            try:
                user_input = int(input("Enter the options from (1-5): "))
                if user_input < 1 or user_input > 5:
                    print("Please enter an input ranging from 1-5")
                    print()
                    continue

                match user_input:
                    case 1:
                        elem = input("Enter the element to insert: ")
                        self.insertArr(elem)
                        self.printArr()
                        continue

                    case 2:
                        self.removeEnd(self)
                        self.printArr
                        continue

                    case 3:
                        pos = int(input("Enter the position to insert: "))
                        elem = input("Enter the element to insert: ")
                        self.insertMiddle(pos, elem)
                        self.printArr()
                        continue

                    case 4:
                        pos = int(input("Enter the position to remove: "))
                        self.removeMiddle(pos, elem)
                        self.printArr()
                        continue

                    case 5:
                        print("Exiting the program....!")
                        break
                    
                    case _:
                        print("Please enter a valid option")
                        print()
                        continue

            except ValueError:
                print("Invalid option")

    def printArr(self):
        for i in range(0 , self.capacity):
            print(self.arr[i], end= ' ')
        print("\n")   

    def elemArr(self):
        n = int(input("Enter the number of elements: "))
        self.elements_array = [input(f'Elements at {i + 1} position: ') for i in range(n)]
        
        for elem in self.elements_array:
            self.length = self.insertArr(elem)
        self.printArr()
        return self.length
    
    def insertArr(self, elem): #Inserting array at the next open position
        if self.length < self.capacity:
            self.arr[self.length] = elem 
            self.length += 1
        else:
            print("Array is full, could not insert data")
        return self.length

    def removeEnd(self): #Remove from end of an array

        if self.length > 0:
            self.arr[self.length - 1] = None
            self.length -= 1
            self.printArr()
        else:
            print("Array is empty, Could not remove from end")

    def insertMiddle(self, pos, elem): #Insert from start to last before position into array

        if pos < 0 or pos >= self.capacity:
            print("Position is greater than capacity")
            return
        
        if self.length >= self.capacity:
            print(f'{self.printArr(self.arr, self.length)} , Value index out of range')
            return
        
        for i in range(self.length-1, pos-1, -1): 
            self.arr[i + 1] = self.arr[i]
        self.arr[pos] = elem
        self.length += 1
    
    def removeMiddle(self, pos): #Remove from start to last before position into array

        if pos < 0 or pos >= self.capacity:   
            print("Position out of range")
            return
        
        for i in range(pos, self.length):
            self.arr[i-1] = self.arr[i]
        self.arr[self.length-1] = None
        self.length -= 1

def main():
    sArr = staticArray()
    sArr.elemArr()
    sArr.choice()
 
if __name__ == "__main__":
    main()