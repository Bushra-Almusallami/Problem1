#Determine if the list can be devided into two parts.
#The sum of each part of the list is equal.
#Print the two lists


my_array=[2,6,1,9]
array_sum=sum(my_array)

if array_sum % 2 != 0:
    print(False)
else:
    half_sum = array_sum/2
    current_sum = 0
    firstArr=[]
    secondArr=[]
    for num in my_array:
        current_sum += num
        
        if current_sum == half_sum:
            firstArr = my_array[:my_array.index(num)+1]
            secondArr = my_array[my_array.index(num)+1:]
            break
        elif current_sum > half_sum:
            firstArr = my_array[:my_array.index(num)]
            secondArr = my_array[my_array.index(num):]
            
    print(True)
    print(firstArr,"and",secondArr)
            
