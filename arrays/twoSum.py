"""
    Author: Lucky Adogun (zen_coder)
    License: MIT
    Date: 26-10-2020


    PROBLEM: Given an array of integers and a target integer, find the position of the
    integers that make up the target.

    Example:

    array = [1,2,3,4]
    target = 7
    result = [2,3]

"""
def solution_one(nums, target):

    compliments = {}
    result = []

    for index, num in enumerate(nums):
        if compliments.get(num) is None:
            compliments[target-num] = index
        else:
            result = [compliments[num], index]
    return result


def solution_two(nums, target):
    """
        - Loop through the array with its index
        - find the compliment by subtracting the target from the iterated items:
            eg: 
                items = [1,2,3,4], target = 7
                 => 7-1 = 6
                 => 7-2 = 5
                 => 7-3 = 4
                 => 4-4 = 3

        - check if the compliment is already in the array. 
        
        If YES:
            - store the index of the item that produces it and the item in the hashmap (dictionary)
            In the case of array with elements [1,2,3,4] and target 7

                => 7-3 is 4 which is already present in the list, therefore, the index of 3 needs to be stored.
                => 7-4 is 3 which is already present in the list, therefore, the index of 4 needs to be stored.
        if NO:
            - Don't store the index of the item in the hashmap (dictionary)

        Return a list of the hashmap keys.

        This algorithm runs on O(n) time complexity.

    """
    myHash = {}
    for index, item in enumerate(nums):
        if target - item in nums:
            myHash[index] = item

    return list(myHash.keys())



solution_one([0,12,15,3, 1], 18)
solution_two([0,12,15,3, 1], 18)
