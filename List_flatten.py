#testing list flatten
l = [[1,2],3,[4,5,6]]
l[0]
isinstance(l[0],list)
print(l[0:1])
test = [1,2,3,4,5,6]
print(test[0:1])
test[0:1] = [1,2,3,4]
print(test)


#flatten a list - beautiful code from rightfootinblog 
# http://rightfootin.blogspot.com/2006/09/more-on-python-flatten.html
def flatten(l, ltypes = (list,tuple)):
    ltype = type(l) #tells flatten where we are dealing with a list or a tuple
    l = list(l) #converts into a list
    i = 0
    while i < len(l): #iterates through the list
        while isinstance(l[i], ltypes): #checks that the list element is a list or a tuple
            if not l[i]: #empty list check
                l.pop[i] #removes empty list
                i -= 1 #reset counter to avoid missing elements
                break
            else: #if not empty list
                l[i:i+1] = l[i] #VERY INTERERESTING BEHAVIOUR WITH INDEXIN SYNTAX
                # [i] returns element i
                # [i:i] return empty list
                # [i:i+1] returns the iths element but as a list! 
                
                # so assigning onto this interval we can instert arbitrarily many values 
                # into the list

                #WOWOWOWOWO - nive python underpinnings, must take advantage how how lists
                # are actually defined in python

                # lists are an array of pointers which point to objects (can be other list)

                # I dont really understand how this words in memoery but conveptually it akes sense
                # we replace the list of hte first element with a list which python then unpacks 
                # into elemnts - RESIZING if you add an element python will find a new block in hte memory
                # and copy all of hte "pointers" to that new memory - now we trick python into copying the 
                # pointers of list l[i] rather than the pointer TO list l[i]
            i += 1
        return ltype(l)

