
import math


class Value:

    def __init__(self,data, _children = (), _op = (), label = (), parent_grad = ()):
        self.data = data
        self._prev = set(_children)
            # _children will be a tuple but will be held as a set in the class _prev - just done for efficiency
        self._op = _op
        self.label = label

        #derivative
        self.grad = 0 # initialized at 0 - assume that value does not effect output at the start
        
        #backpop funciton
        self._backward = lambda: None

    def __repr__(self):
        #python interally uses this repr function to return this string when the object is called on its own
        return f"Value(data={self.data})"
        
    #need to define addition
    def __add__(self,other):
        #check if other is a value object and make it one if not
        other = other if isinstance(other, Value) else Value(other)

        #use special underscore emthods to define operators in pytho
        # e.g. if we od a + b, python will interally do a.__add__(b)
        out = Value(self.data + other.data, _children = (self,other), _op = "+" )#this operator works as it is operating on self.data which is jsut a python number rather than our value class, second part is feeding in the _children expression to the new value obejct
        
        # definint g the function that propgates the gradient
        def _backward():
            # we want to propogate outs.grad and change self.grad and other.grad
            self.grad += 1.0 * out.grad
            other.grad += 1.0 * out.grad

            # #recursive call ?not implemented
            # self._backward()
            # other._backward()
        out._backward = _backward

        return out
    
    #same for multiplication
    def __mul__(self, other):
        #check if other is a value object and make it one if not
        other = other if isinstance(other, Value) else Value(other)

        out = Value(self.data * other.data, (self,other), "*") #this operator works as it is operating on self.data which is jsut a python number rather than our value class
        
        def _backward():
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad

            # #recursive calls - think abotu variable scope it makes ense
            # self._backward()
            # other._backward()
        out._backward = _backward
        
        return out
    
    # def exp(self):
    #     # app exponentiation
    #     x = self.data
    #     out = Value(math.exp(x), (self,), "exp") #only 1 child

    #     def _backward():
    #         #same pointer trickery as before
    #         self.grad += out.grad * out.data

    #     out._backward = _backward

    #     return out

    # def __pow__(self,k):
    #     #other must be a int/float for now
    #     #otherwise math wont work for  aspecific case ??? cant backprop to the k value - makes sense
    #     assert isinstance(k, (int,float))

    #     out = Value(self.data**k, (self,), "**{}".format(k))

    #     def _backward():
    #         #calculus baby x**k = k*x**(k-1)
    #         # remember out.grad is the reverse chain rule component
    #         self.grad += out.grad * (k * ((self.data)**(k-1)) )

    #     out._backward = _backward

    #     return out
    
    def __pow__(self, other):
        assert isinstance(other, (int, float)), "only supporting int/float powers for now"
        out = Value(self.data**other, (self,), f'**{other}')

        def _backward():
            self.grad += (other * self.data**(other-1)) * out.grad
        out._backward = _backward

        return out


    # #defined activation function
    # def tanh(self):
    #     x = self.data
    #     t = (math.exp(2*x) -1) / (math.exp(2*x) + 1)
    #     out = Value(t, (self, ), "tanh") #only 1 child

    #     def _backward():
            
    #         self.grad += out.grad * (1 - t**2)
            
    #     out._backward = _backward
        
    #     return out
    
    def relu(self):
        out = Value(0 if self.data < 0 else self.data, (self,), 'ReLU')

        def _backward():
            self.grad += (out.data > 0) * out.grad
        out._backward = _backward

        return out

    
    def backward(self):
        #actaul backprop function - builds topolical tree and applies _backward attribute on it
    
        # building a topological graph
        topo = []
        visited = set()
        def build_topo(v):
            if v not in visited:
                visited.add(v)
                for child in v._prev:
                    build_topo(child)       
                topo.append(v) #only adds itself after all the children are processed
        build_topo(self)

        self.grad = 1
        for node in reversed(topo):
            node._backward()


    ###

    def __neg__(self): # -self
        return self * -1

    def __radd__(self, other): # other + self
        return self + other

    def __sub__(self, other): # self - other
        return self + (-other)

    def __rsub__(self, other): # other - self
        return other + (-self)

    def __rmul__(self, other): # other * self
        return self * other

    def __truediv__(self, other): # self / other
        return self * other**-1

    def __rtruediv__(self, other): # other / self
        return other * self**-1
    


    # def __neg__(self): #-self
    #     return self * -1
    
    # def __radd__(self,other): #other + self reverse addition
    #     #this is a fallback - if __add__ doesnt work - so python will then check if the second term has a rmul
    #     # this seems super ineficient but i guess that is the point (python is clever and nice but slow)
    #     return self + other  

    # def __sub__(self,other): #self - other
    #     return self + (-other) #saves us rewriting addition #wowowowo
    
    # def __rsub__(self,other): #other - self reverse multiplication
    #     #this is a fallback - if __sub__ doesnt work - so python will then check if the second term has a rmul
    #     # this seems super ineficient but i guess that is the point
    #     return other + (-self)

    # def __rmul__(self,other): #other * self reverse multiplication
    #     #this is a fallback - if __mul__ doesnt work - so python will then check if the second term has a rmul
    #     # this seems super ineficient but i guess that is the point
    #     return self * other

    # def __truediv__(self,other):
    #     #division is a special case of exponentiation x**k a/b = a * b**-1
    #     return self * other**-1
    
    # def __rtruediv__(self,other):
    #     return other * self**-1 #not sure why this one is hte other way around - actaully makes sens haha






######################################################################



# #defining the value class
# import math

# class Value:

#     def __init__(self,data, _children = (), _op = (), label = (), parent_grad = ()):
#         self.data = data
#         self._prev = set(_children)
#             # _children will be a tuple but will be held as a set in the class _prev - just done for efficiency
#         self._op = _op
#         self.label = label

#         #derivative
#         self.grad = 0.0 # initialized at 0 - assume that value does not effect output at the start
        
#         #backpop funciton
#         self._backward = lambda: None

#     def __repr__(self):
#         #python interally uses this repr function to return this string when the object is called on its own
#         return f"Value(data={self.data})"
    
#     #need to define addition
#     def __add__(self,other):
#         #check if other is a value object and make it one if not
#         other = other if isinstance(other, Value) else Value(other)

#         #use special underscore emthods to define operators in pytho
#         # e.g. if we od a + b, python will interally do a.__add__(b)
#         out = Value(self.data + other.data, _children = (self,other), _op = "+" )#this operator works as it is operating on self.data which is jsut a python number rather than our value class, second part is feeding in the _children expression to the new value obejct
        
#         # definint g the function that propgates the gradient
#         def _backward():
#             # we want to propogate outs.grad and change self.grad and other.grad
#             self.grad += 1.0 * out.grad
#             other.grad += 1.0 * self.grad

#             # #recursive call ?not implemented
#             # self._backward()
#             # other._backward()
#         out._backward = _backward

#         return out
    
#     #same for multiplication
#     def __mul__(self, other):
#         #check if other is a value object and make it one if not
#         other = other if isinstance(other, Value) else Value(other)

#         out = Value(self.data * other.data, (self,other), "*") #this operator works as it is operating on self.data which is jsut a python number rather than our value class
        
#         def _backward():
#             self.grad += other.data * out.grad
#             other.grad += self.data * out.grad

#             # #recursive calls - think abotu variable scope it makes ense
#             # self._backward()
#             # other._backward()
#         out._backward = _backward
        
#         return out

#     def __neg__(self): #-self
#         return self * -1

#     def __sub__(self,other): #self - other
#         return self + (-other) #saves us rewriting addition #wowowowo
    
#     def __rsub__(self,other): #other - self reverse multiplication
#         #this is a fallback - if __sub__ doesnt work - so python will then check if the second term has a rmul
#         # this seems super ineficient but i guess that is the point
#         return self - other

#     def __rmul__(self,other): #other * self reverse multiplication
#         #this is a fallback - if __mul__ doesnt work - so python will then check if the second term has a rmul
#         # this seems super ineficient but i guess that is the point
#         return self * other

#     def __radd__(self,other): #other + self reverse addition
#         #this is a fallback - if __add__ doesnt work - so python will then check if the second term has a rmul
#         # this seems super ineficient but i guess that is the point (python is clever and nice but slow)
#         return self + other  
    
#     def __truediv__(self,other):
#         #division is a special case of exponentiation x**k a/b = a * b**-1
#         return self * other**-1
    
#     def __rtruediv__(self,other):
#         return self * other**-1


#     def exp(self):
#         # app exponentiation
#         x = self.data
#         out = Value(math.exp(x), (self,), "exp") #only 1 child

#         def _backward():
#             #same pointer trickery as before
#             self.grad += out.grad * out.data

#         out._backward = _backward

#         return out

#     def __pow__(self,k):
#         #other must be a int/float for now
#         #otherwise math wont work for  aspecific case ??? cant backprop to the k value - makes sense
#         assert isinstance(k, (int,float))

#         out = Value(self.data**k, (self,), "**{}".format(k))

#         def _backward():
#             #calculus baby x**k = k*x**(k-1)
#             # remember out.grad is the reverse chain rule component
#             self.grad += out.grad * k*((self.data)**(k-1))

#         out._backward = _backward

#         return out

#     # def relu(self):
#     #     x = self.data
#     #     t = x if x >= 0 else 0
#     #     out = Value(t, (self, ), "ReLU") 

#     #     def _backward():
#     #         self.grad += out.grad * (out.data > 0)
        
#     #     out._backward = _backward

#     #     return out

#     #defined activation function
#     def tanh(self):
#         x = self.data
#         t = (math.exp(2*x) -1) / (math.exp(2*x) + 1)
#         out = Value(t, (self, ), "tanh") #only 1 child

#         def _backward():
            
#             self.grad += out.grad * (1 - t**2)
            
#             #having a bit of trouble figuring out the variable scope here
#             #this function is not kept as a string but insted references the object pointers used when initializing it
#             # when we "set" the function below
#             # the function references self from the current variable scope - inside the tanh funciton where self refers not to the out Value but to the value which will create out

#             # some simple debugging
#             # print whatever self is when reference - when we call out._backwards we will see it prints the current self rather than out itself
#             # This sounds schizophrenic but makes sense if you think about it enough
#             # when you 

#             # I have read the docs and returned wiser
#             # when you define the function you bind the function tot he local namespace and the function object 
#             # containes reference tot eh current global namespace as the flobal namespace tot be used when the 
#             # function is called
#             # so when we define the function ehre it remembers this tanh() function as the namespace and within
#             # this space self refers to the object that is to create out
#             # MAEKS SESNE
#             # https://docs.python.org/3/reference/compound_stmts.html#function
#             # print(self)
            
#             # recusrive call not implemented
#             # self._backward()


#         out._backward = _backward
        
#         return out
    

#     #also want to make the connective tissue of the expression - keep expression graphs simple pointers
#     #_children argument added

#     #also need to know what operation created each value
#     #_op


#     #also want a way to visualize these expressions
#     #see cell below

#     # add labels _label

#     #add another variable which keeps track of the derivative of L with respect to that value

#     # #my attempt at writing it - to compare with the GOAT
#     # def backprop(self, _parent_grad = (), _op = (), _sibling = ()):
        
#     #     # Dont use unnecesary parent grad variable
#     #     # can convey all the information reqiured for recursive function in the function call
#     #     # previuosly used self.parent_grad function - uneccesary

#     #     print(self.label, _parent_grad, _op, _sibling)
        
#     #     if _parent_grad == ():
#     #         #base case
#     #         self.grad = 1 
#     #         #derivative with respect to itself will be 1 always

#     #     else:
#     #         # apply chain rule using the parent grad
#     #         if _op == "*":
#     #             self.grad = _parent_grad * _sibling.data # parent = c1 * c2 ; dparent/dc1 = c2
#     #         elif _op == "+":
#     #             self.grad = _parent_grad * 1 # parent = c1 + c2 ; dparent/dc1 = 1 + 0 = 1

#     #     if self._prev != set():
#     #         #each nodes is assumed to have 2 children
#     #         child1 , child2 = self._prev
            
#     #         #unnecessarily pass sibling node even if addition
#     #         child1.backprop(_parent_grad = self.grad, _op = self._op, _sibling = child2)
#     #         child2.backprop(_parent_grad = self.grad, _op = self._op, _sibling = child1)

#     # Kaprpathy backpopogates through each operation
#     # ?just changes the childern directly and hten backprops through - makes way more sense as can handle larger sums :)
#     # ?still need to check base case 
#     # Karpathy getting fucking clever and using almbda functions
#     # written into the code of building a network he specifies how to backprop over it 
#     # seems weird but we will trust the GOAT
    
#     def backward(self):
#         #actaul backprop function - builds topolical tree and applies _backward attribute on it
    
#         # building a topological graph
#         topo = []
#         visited = set()
#         def build_topo(v):
#             if v not in visited:
#                 visited.add(v)
#                 for child in v._prev:
#                     build_topo(child)       
#                 topo.append(v) #only adds itself after all the children are processed
#         build_topo(self)

#         self.grad = 1
#         for node in reversed(topo):
#             node._backward()
        
            

 
    



