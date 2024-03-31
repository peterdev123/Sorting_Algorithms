class MergeSorting:
    def __init__(self, array):
        self.array = array
        
    def sort(self):
        if len(self.array) > 1:
            mid = len(self.array) // 2
            left = self.array[:mid]
            right = self.array[mid:]

            # Recursive call
            left = MergeSorting(left).sort()
            right = MergeSorting(right).sort()

            # Merging the arrays
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    self.array[k] = left[i]
                    i += 1
                    k += 1
                else:
                    self.array[k] = right[j]
                    j += 1
                    k += 1

            # Appending remaining elements
            while i < len(left):
                self.array[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                self.array[k] = right[j]
                j += 1
                k += 1

            return self.array
        else:
            return self.array
