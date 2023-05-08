
a = int(input('Enter first number: '))
b = int(input('Enter Second number: '))
c = int(input('Enter third number: '))


if (a>b) and (a>c):
    print(a,"is the largest")
elif(b>a) and (b>c):
    print(b,"is the largest")
elif(c>a) and (c>b):
    print(c,"is the largest")

else:
    print("entered numbers are equal.")