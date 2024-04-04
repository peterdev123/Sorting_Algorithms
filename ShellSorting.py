class ShellSorting:

    def __init__(self, array):
        self.array = array

    def sort(self):
        gap = len(self.array) // 2
        while gap > 0:
            for i in range(gap, len(self.array)):
                #Assign temp to current element of the index
                temp = self.array[i]
                j = i
                #Place the element to its sorted position until condition is not met
                while j >= gap and self.array[j - gap] > temp:
                    self.array[j] = self.array[j - gap]
                    j -= gap
                self.array[j] = temp
            #Gap is floor divided by 2
            gap //= 2

        return self.array