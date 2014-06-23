#if x is integer return true if not false
# if statement checks if the number - itself rounded down is greater than 0-- results in false

def is_int(x):
    if abs(x - round(x)) > 0:
        return False
    else:
        return True