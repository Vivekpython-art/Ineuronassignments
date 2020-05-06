''''''
Write a program which will find all such numbers which are divisible by 7 but are not a multiple
of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a
comma-separated sequence on a single line.
''''''
l = []

for x in range(2000,3201):
    if (x%7 == 0) and (x%5 != 0):
        l.append(str(x))
print(','.join(l))               


''''''
Write a Python program to accept the user's first and last name and then getting them printed in
the the reverse order with a space between first name and last name
''''''

fname = input("Enter First name:  ")
lname = input("Enter First name:  ")
print(lname+' '+fname )


''''''
Write a Python program to find the volume of a sphere with diameter 12 cm.
Formula: V=4/3 * π * r^3
''''''

pi = 3.1415926535897931
d = 12
r = d/2

V = (4.0/3.0)* pi* r**3
print("Volume of the Spehere is: ", V)


''''''
Write a program which accepts a sequence of comma-separated numbers from console and
generate a list.
''''''

lis=input("From a comma-separated list of numbers get:\n")
lis=lis.split(",")
print(lis)

''''''
Create the below pattern using nested for loop in Python.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
''''''
n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')
for i in range(n,0,-1):
    for j in range(i):
        print ('* ', end="")
    print('')

''''''
Write a Python program to reverse a word after accepting the input from the user.
Sample Output:
Input word: AcadGild
Output: dilGdacA
''''''

user = input('Enter the word:\n')
print(user[::-1])


''''''


string = "WE, THE PEOPLE OF INDIA,{}having solemnly resolved to constitute India into a SOVEREIGN,{}SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC{}and to secure to all its citizens{}"
print(string.format('\n\t','!\n\t\t','\n\t\t',':'))


print("WE, THE PEOPLE OF INDIA,\n\thaving solemnly resolved to constitute India into a SOVEREIGN,! \n\t\tSOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \n\t\t and to secure to all its citizens")

'''''''''''