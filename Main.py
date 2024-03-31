# from BubbleSorting import BubbleSorting
from SelectionSorting import SelectionSorting

array = [21, 15, 8, 12, 102, 5, 3]

# myClass = BubbleSorting(array)
myClass = SelectionSorting(array)
sortedArray = myClass.sort()

print(sortedArray)