a = [1,2,3,4]

# working with lists to make it easier to work with


def rec_pset(x):   
    if len(x) == 0:
        return [[]] #list of empty list

    smaller = rec_pset(x[:-1])
    extra = x[-1:]
    new = []
    for small in smaller:
        new.append(small + extra)

    # concatenate together
    return smaller + new

print(rec_pset(a))