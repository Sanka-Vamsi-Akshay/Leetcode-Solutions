class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            if i < 0:
                while stack:
                    val = stack.pop()
                    if val < 0:
                        stack.append(val)
                        stack.append(i)
                    elif val + i > 0:
                        stack.append(val)
                    elif val + i != 0:
                        continue
                    break
                else:
                    stack.append(i)
            else:
                stack.append(i)
        return stack