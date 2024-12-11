"""
190: 10 19

+ or *

10 * 19 = 190
output -> True

83: 17 5
17 + 5
17 * 5
output -> False

input: "190: 10 19"


----
MORE EXAMPLES
----
7290: 6 8 6 15

161011: 16 10 13
21037: 9 7 18 13
"""

# 83: 17 5
def targetNumber(str1):
    # Split input to extract the target and the numbers
    arr = str1.split()
    temp = arr[0].split(":")
    target = int(temp[0])

    nums = list(map(int, arr[1:]))

    # Recursive Depth-First Search (DFS)
    def dfs(index, total):
        # Base case: If total matches target
        if total == target:
            return True
        
        # Base case: If index is out of bounds
        if index >= len(nums):
            return False

        # Get the current number
        number = nums[index]

        # Recursive case: Try addition
        if dfs(index + 1, total + number):
            return True

        # Recursive case: Try multiplication
        if dfs(index + 1, total * number):
            return True

        # If neither addition nor multiplication works, return False
        return False

    # Start the DFS with the first number (no operations yet)
    for i in range(len(nums)):
        if dfs(i + 1, nums[i]):
            return True

    return False

# Test Cases
print(targetNumber("190: 10 19"))         # True
print(targetNumber("83: 17 5"))           # False
print(targetNumber("7290: 6 8 6 15"))     # False
print(targetNumber("161011: 16 10 13"))   # True
print(targetNumber("21037: 9 7 18 13"))   # False






