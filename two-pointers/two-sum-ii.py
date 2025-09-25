class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while (numbers[l] + numbers[r] != target):
            if numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1

        return[l + 1, r + 1]
    

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1


        while numbers[l] + numbers[r] != target:

            if numbers[l] + numbers[r] < target:
                l += 1

            else:

                r -= 1

        return [l + 1, r + 1]
    
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            cur = numbers[l] + numbers[r]

            if cur == target:
                return [l + 1,r + 1]
            elif cur < target:
                l += 1
            else:
                r -= 1
        return [l +1,r + 1]