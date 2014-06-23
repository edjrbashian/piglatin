# takes in a list and removes elements of the list that are the same.

def remove_duplicates(x):
    new = []
    for i in x:
        if i not in new:
            new.append(i)
    return new