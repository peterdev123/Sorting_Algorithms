class BubbleSorting :

    def __init__(self, array):
        self.array = array

    def sort(self):
        for i in range(len(self.array)-1):
            for j in range(0, len(self.array)-i-1):
                if self.array[j] > self.array[j+1]:
                    # Swapping the elements
                    if self.array[j] >  self.array[j+1]:
                        temp = self.array[j]
                        self.array[j] = self.array[j + 1]
                        self.array[j + 1] = temp
        return self.array

    