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
            result = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            # Appending remaining elements
            while i < len(left):
                result.append(left[i])
                i += 1

            while j < len(right):
                result.append(right[j])
                j += 1

            return result
        else:
            return self.array
