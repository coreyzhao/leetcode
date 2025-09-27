class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in range(len(asteroids)):
            a = asteroids[i]
            while stack and stack[-1] > 0 and a < 0:
                if abs(stack[-1]) > abs(asteroids[i]):
                    a = 0
                elif abs(stack[-1]) < abs(asteroids[i]):
                    stack.pop()
                else:
                    stack.pop()
                    a = 0

            if a != 0:
                stack.append(a)

        return stack