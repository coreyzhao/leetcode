class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        count = 0
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] = digits[i] + 1
                count = 0
                break

            digits[i] = 0
            count = 1

        if count == 1:
            digits.insert(0, 1)

        return digits

