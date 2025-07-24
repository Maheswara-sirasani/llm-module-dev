def fab(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fab(n-1)+fab(n-2)
    
position=6
print("position of faboncci is :",position,"value is",fab(position))    
    