class QuickSorting:

    def __init__(self, array):
        self.array = array

    def sort(self, low, high):
        #Recursive call for left and right array until all are sorted
        if low < high:
            #Finding the index after the pivot is sorted at its right position
            index = self.partition(low, high)
            a = self.sort(low, index - 1)
            b = self.sort(index + 1, high)
        return self.array

    def partition(self, low, high):
        #Initializing the pivot to the last element of the array
        pivot = self.array[high]
        #Reference for swapping
        i = low - 1
        #Go through each element in the array from start to end
        for j in range(low, high):
            #If current element is lesser than  or equal to the pivot then increase "i" and swap else j is only incremented
            if self.array[j] <= pivot:
                i += 1

                self.array[i], self.array[j] = self.array[j], self.array[i]
        #Swapping the element of index i and pivot
        #The pivot is now placed at its sorted position
        self.array[i + 1], self.array[high] = self.array[high], self.array[i + 1]

        #Returns the index of the sorted pivot
        return i + 1
