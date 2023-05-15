#Print the first non-repeating element in the list

Arr=[1,2,7,5,8,2,1]

for num in Arr:
    if Arr.count(num)==1:
        print(num)
        break
