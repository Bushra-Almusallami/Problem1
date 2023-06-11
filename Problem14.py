from math import pi

def volume(h,r):
    volume= (1/3) * pi * r**2 * h
    return volume
    #return(round(volume,2))
    
result= volume(7,4)
print("{:.2f}".format(result))
