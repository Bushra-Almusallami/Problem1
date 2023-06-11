array=[[1,2,3],
       [4,5,6],
       [9,8,9]]

fe1=array[0][0]
fe5=array[1][1]
fe9=array[2][2]
se3=array[0][2]
se5=array[1][1]
se9=array[2][0]

sum1= fe1+fe5+fe9
sum2= se3+se5+se9

total= abs(sum1-sum2)
print(fe1,"+",fe5,"+",fe9,"=",sum1)
print(se3,"+",se5,"+",se9,"=",sum2)
print("|",sum1,"-",sum2,"| =",total)
