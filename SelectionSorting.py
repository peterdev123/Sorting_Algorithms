class SelectionSorting :

    def __init__(self, array) :
        self.array = array

    def sort(self) :
        
        n = len(self.array)

        for i in range(n):
            #Initialize the i to smallest index
            minIndex = i
            for j in range(i + 1, n) :
                #If current index is lesser than  minIndex then update minIndex
                if(self.array[j] < self.array[minIndex]) :
                    minIndex = j

            #swap the two elements
            #This will bring the minimum element of unsorted part to sorted part
            self.array[i], self.array[minIndex] = self.array[minIndex], self.array[i]
        
        return self.array