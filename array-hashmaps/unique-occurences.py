class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        my_dict = {}
        for num in arr:
            if num in my_dict:
                my_dict[num] += 1
            else:
                my_dict[num] = 1

        ls_check = []
        for num in my_dict:
            if my_dict[num] in ls_check:
                return False
            else:
                ls_check.append(my_dict[num])


        return True