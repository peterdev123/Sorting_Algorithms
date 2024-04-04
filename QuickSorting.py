class QuickSorting:

    def __init__(self, array):
        self.array = array

    def sort(self, low, high):
        if low < high:
            index = self.partition(low, high)
            a = self.sort(low, index - 1)
            b = self.sort(index + 1, high)
        return self.array

    def partition(self, low, high):

        pivot = self.array[high]
        i = low - 1

        for j in range(low, high):
            if self.array[j] <= pivot:
                i += 1

                self.array[i], self.array[j] = self.array[j], self.array[i]

        self.array[i + 1], self.array[high] = self.array[high], self.array[i + 1]

        return i + 1
