class Solution:
    def hello(self, message, message_2, message_3):
        print('Hello',message, message_2, message_3, 'years old')


a = Solution()
a.hello('Dima', 'Petrov', 20)#Hello Dima Petrov 20 years old
a.hello('Dima', 'Petrov', 14)#Hello Dima Petrov 14 years old
a.hello('Dima', 'Ivanov', 14)#Hello Dima Ivanov 14 years old
a.hello('Ivan', 'Ivanov', 14)#Hello Ivan Ivanov 14 years old