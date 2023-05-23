array=[1,8,7,4,1,2,2,2]
arr=[]
for i in range(0,len(array)):
    for j in range(i+1,len(array)):
        if(array[i]==array[j]):
            arr.append(array[j])
print(max(arr))
