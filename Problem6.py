array=[1,2,3,4,5]
left_rotation_time=2

for i in range(left_rotation_time):
    m=array[0]
    for j in range(len(array)-1):
        array[j]=array[j+1]
    
    array[len(array)-1]=m
print(array)
        
