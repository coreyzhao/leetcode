class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        logs.sort(key=lambda ls: ls[0])

        startyear = logs[0][0]

        logs.sort(key=lambda ls: ls[1])
        endyear = logs[len(logs) - 1][1]


        line = [0] * (endyear - startyear + 1)

        for ls in logs:
            line[ls[0] - startyear] += 1
            line[ls[1] - startyear] -= 1

        count = 0
        my_max = 0
        res = 0
        for i in range(len(line)):
            count += line[i]
            if count > my_max:
                my_max = count
                res = i + startyear

        return res



