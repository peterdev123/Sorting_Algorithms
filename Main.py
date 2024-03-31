# from BubbleSorting import BubbleSorting
# from SelectionSorting import SelectionSorting
from InsertionSorting import InsertionSorting

array = [21, 15, 8, 12, 102, 5, 3]

# myClass = BubbleSorting(array)
# myClass = SelectionSorting(array)
myClass = InsertionSorting(array)
sortedArray = myClass.sort()

print(sortedArray)