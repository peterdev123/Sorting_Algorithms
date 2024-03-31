class InsertionSorting:

    def __init__(self, array) :
        self.array = array

    def sort(self) :

        n = len(self.array)

        for i in range(1, n) :
            #Initialize key to index i
            key = self.array[i]
            j = i - 1
            #Swap the element to its sorted position until it doesn't meets its condition
            while j >= 0 and self.array[j] > key :
                self.array[j + 1] = self.array[j]
                j -= 1
            #Place the element at its correct position
            self.array[j + 1] = key

        return self.array