

4%3

5%3

6%3

7%3

#偶数都能被2整除， 因此对一个数（number ） 和2执行求模运算的结果为零， 即number % 2 == 0 ， 那么这个数就是偶数； 否则就是奇数。
number = input("Enter a number, and I'll tell you if it's even or odd:")
number = int(number)

if number%2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")