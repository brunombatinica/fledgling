#coding a very simple recursive search tree
import random 

class item(object):
    def __init__(self,name,v,c):
        self.name = name
        self.v = v
        self.c = c
        
    def getv(self):
        return self.v
    
    def getc(self):
        return self.c
    
    def getd(self):
        return self.v/self.c
    
    def getname(self):
        return self.name
    
    def __str__(self):
        return "{}".format(self.getname())
        return "{}: value = {}, cost = {}".format( \
                self.getname(),self.getv(),self.getc())
            

def buildset(names,values,calories):
    itemset = []
    for i in range(len(values)):
        itemset.append(item(names[i],values[i],calories[i]))
    return itemset

def generateset(n, maxv, maxc):
    itemset = []
    for i in range(n):
        itemset.append(item(i,
                            random.randint(1, maxv),
                            random.randint(1,maxc)))
    return itemset

def greedy(items, avail):
    options = items
    budget = avail
    tval = 0
    sset = ()
    
    
    while budget > 0:
        #temp variable to ahndel when all items are too big
        maxind = -1
        
        #tests DENSITY getd()
        maxd = 0
        for i,x in enumerate(options):
            if x.getd() > maxd and x.getc() < budget:
                maxind = i
                maxd = x.getd()
        
        if maxind != -1:
            sset = sset + (options[maxind],)
            tval += options[maxind].getv()
            budget -= options[maxind].getc()
            del options[maxind]
        else:
            break
        
    return (tval, sset)

def searchtree(items, avail):
    #items is a list of "item" objects
    #avail is a constraint to the cost
    #returns a tuple of the total value of a solution to 
    # 0/1 knapsack problem and the items of that solution
    
    
    #BEAUTIFUL!!!! - my implementation was okay
    
    #if empty
    if items == [] or avail == 0:
        result = (0, ())
    elif items[0].getc() > avail:
        #if left item costs too much
        #only explore right branch i.e not taking leftmost object
        result = searchtree(items[1:],avail)
        
    else:
        #left item can be included
        
        #test which path maximises value
        
        #include left item
        #explore left with budget constrained by taking i[0]
        lval, lknap = searchtree(items[1:], avail - items[0].getc())
        #add value of left item
        lval = lval + items[0].getv() 
        #add left item to list of values
        lknap = lknap + (items[0],)
        
        #Explore right without taking i[0]
        rval, rknap = searchtree(items[1:], avail)
        
        #If event of a tie return that one take less items
        if lval > rval:
            result = (lval, lknap)
        else:
            result = (rval, rknap)
        
    return result



def dst(items, avail, memo = {}):
    #dynamic search tree
    
    #items is a list of "item" objects
    #avail is a constraint to the cost
    #returns a tuple of the total value of a solution to 
    # 0/1 knapsack problem and the items of that solution
    
    
    #BEAUTIFUL!!!! - my implementation was okay
    
    #if empty
    if items == () or avail == 0:
        result = ((),0)
    else:
        
        #easy to use exceptions
        try:       
            result = memo[(items,avail)]
            print("WOW THAT WAS DYNAMIC")
            print(*items)
            
        except:
            # print(*items)
            # print(items[0].getc())
            if items[0].getc() > avail:
                #if left item costs too much
                #only explore right branch i.e not taking leftmost object
                result = dst(items[1:],avail,memo)
            
            else:
                #left item can be included
                
                #test which path maximises value
                
                #include left item
                #explore left with budget constrained by taking i[0]
                lknap, lval = dst(items[1:], avail - items[0].getc())
                #add value of left item
                lval = lval + items[0].getv() 
                #add left item to list of values
                lknap = lknap + (items[0],)
                
                #Explore right without taking i[0]
                rknap, rval = dst(items[1:],avail,memo)
                
                #If event of a tie return that one take less items
                if lval > rval:
                    result = (lknap, lval)
                else:
                    result = (rknap, rval)
            
            
    memo[ (items,avail) ] = result
    
    return result


#manually create items
# a = item("wine",89,123)
# b = item("b",40,90)
# c = item("c",20,30)
# options = [a,b,c]

#MIT example
# names = ['wine', 'beer', 'pizza', 'burger', 'fries',
#          'cola', 'apple', 'donut', 'cake']
# values = [89,90,95,100,90,79,50,10]
# calories = [123,154,258,354,365,150,95,195]
# options = buildset(names, values, calories)

#options = generateset(20,150,100)

#dynamic test
names = ["a", "b", "c", "d"]
values = [6,7,8,9]
calories = [3,3,2,5]
options = buildset(names, values, calories)

#randomly generate items - TO DO
print("SEARCHTREE:")
val, bestsubset = searchtree(options,750)
print(val)
for i in bestsubset:
    print(i)
    
print("DST:")
bestsubset, val = dst(tuple(options),750)
print(val)
for i in bestsubset:
    print(i)
   
print("GREEDY:")
val, bestsubset = greedy(options,750)
print(val)
for i in bestsubset:
    print(i)



