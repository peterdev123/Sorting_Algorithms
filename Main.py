import random
from BubbleSorting import BubbleSorting
from SelectionSorting import SelectionSorting
from InsertionSorting import InsertionSorting
from MergeSorting import MergeSorting
from ShellSorting import ShellSorting
from QuickSorting import QuickSorting

array = []
for _ in range(10):
    if random.choice([True, False]): 
        array.append(random.randint(-20, 100)) 
    else:
        array.append(round(random.uniform(-20, 100), 2))

print("Unsorted array: " + str(array))

# myClass = BubbleSorting(array)
# myClass = SelectionSorting(array)
# myClass = InsertionSorting(array)
# myClass = MergeSorting(array)
# myClass = ShellSorting(array)
myClass = QuickSorting(array)
# sorted = myClass.sort()
sortedArray = myClass.sort(0, len(array) - 1)

print("Sorted array: " + str(sortedArray))
