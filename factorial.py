def factorial(x):
    if x <2:
        return x
    else:
        return x * factorial(x-1)
        
        
print factorial(4)