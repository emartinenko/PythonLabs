numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

INDEX_BEFORE_NONE = 4
numSum = sum(numbers[0:INDEX_BEFORE_NONE]) + sum(numbers[5:])
numCount = len(numbers)

none = numSum / numCount
numbers[4] = none

print("Измененный список:", numbers)
