class RadixSorting :
    #This needs work especially the array passed is float and has a negative value in it
    #Only works with whole numbers and non-negative integers
    def __init__(self, array):
        self.array = array

    def countingSort(self, exp):
        n = len(self.array)

        output = [0] * n

        count = [0] * 10

        for i in range (0, n):
            index = int(self.array[i] // exp)
            count[index % 10] += 1

        for i in range (1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = int(self.array[i] // exp)
            output[count[index % 10] -  1] = self.array[i]
            count[index % 10] -= 1
            i -= 1

        i = 0
        for i in range (0, n):
            self.array[i] = output[i]


    def sort(self):
        maximum = max(self.array)

        exp = 1
        while maximum > exp:
            self.countingSort(exp)
            exp *= 10

        return self.array
        