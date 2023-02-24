height = int(input('height:'))
sign=input('sign:')

class Solution:
    def tree(self, height, sign):
        for line in range(1, height + 2, 2):
            for space in range(height + 1, 1, -7):
                print(' ' * space, sign * line)

people = Solution()

people.tree(height,sign)





