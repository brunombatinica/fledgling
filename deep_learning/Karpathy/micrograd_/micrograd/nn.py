
#impementation of the nerual netowrk

# follos pytorch in having a parten module class
import random
from micrograd.engine import Value

class Module:
    def zero_grad(self):
        for p in self.parameters():
            p.grad = 0

    def parameters(self):
        return []
    
class Neuron(Module):

    def __init__(self, nin, nonlin = True):
        #nin = number of inputs
        #randomly initializes weights and bias
        self.w = [Value(random.uniform(-1,1)) for _ in range(nin)] 
        self.b = Value(0)
        self.nonlin = nonlin

    def __call__(self,x):
        #funciton() = funciton.__call__()

        #return output = activation(w dot x + b)
        #dot product is essentially pairwise multiplication
        act = sum((wi*xi for wi,xi in zip(self.w,x)),self. b)  #zip combines 2 iterators and iterates over the tuples of hte 2 interators combined 
        #interesting that sum works on Value() objects, second argument = intiial value - for a bit of efficiency
        out =  act.relu() if self.nonlin else act

        return out
    
    def parameters(self):
        #written this way to match pytorch
        #pytorch has a .parameters on every since NN module which does this
        #one subtle difference - in pytorch this returns the parameters tensors
        # for us we return theparamter scalars (actually value objects)
        # ?torch.Tensor is the equivalent to our Value() class hmmmm?
        return self.w + [self.b]


class Layer(Module):
    def __init__(self,nin,nout, **kwargs):
        #initialize "nout" neurons each with "nin" inputs
        self.neurons = [Neuron(nin, **kwargs) for _ in range(nout)]
    
    def __call__(self,x):
        #return forward pass of all neurons in the layer
        #"independently evaluate them"
        outs = [n(x) for n in self.neurons]
        return outs[0] if len(outs) == 1 else outs #THIS IS THE CONDITIONAL RETURN SYNTAX DON'T NEED 2 RETURNS
    
    def parameters(self):
        #layer is also a module so to match pytorch it will lhave parameters - every module has parameters

        # params = []
        # for neuron in self.neurons:
        #     ps = neuron.parameters()
        #     params.extend(ps)
        # return params
        #SHORTEN THIS TO......

        return [p for neuron in self.neurons for p in neuron.parameters()] #nested single list comprehension
 
class MLP(Module):
    def __init__(self,nin,nouts):
        #nin = number of inputs - scalar
        #nout = list of number of neurons in each layer
        sz = [nin] + nouts #concatenante these 2 together
        #self.layers = [Layer(sz[i],sz[i+1]) for i in range(len(nouts))] #itrate through creating multiple layers
        self.layers = [Layer(sz[i], sz[i+1], nonlin=i!=len(nouts)-1) for i in range(len(nouts))]

    def __call__(self,x):
        #need to pass each output as an input into the next layer
        #simple as that
        for layer in self.layers:
            x = layer(x)
        return x
    
    def parameters(self):
        #same format as above
        return [p for layer in self.layers for p in layer.parameters()]







# from micrograd.engine import Value
# import random


# class Neuron:
#     def __init__(self, nin, nonlin = True):
#         #nin = number of inputs
#         #randomly initializes weights and bias
#         self.w = [Value(random.uniform(-1,1)) for _ in range(nin)] 
#         self.b = Value(random.uniform(0))

#     def __call__(self,x):
#         #funciton() = funciton.__call__()

#         #return output = activation(w dot x + b)
#         #dot product is essentially pairwise multiplication
#         act = sum((wi*xi for wi,xi in zip(self.w,x)),self. b)  #zip combines 2 iterators and iterates over the tuples of hte 2 interators combined 
#         #interesting that sum works on Value() objects, second argument = intiial value - for a bit of efficiency
#         out = act.relu()

#         return out
    
#     def parameters(self):
#         #written this way to match pytorch
#         #pytorch has a .parameters on every since NN module which does this
#         #one subtle difference - in pytorch this returns the parameters tensors
#         # for us we return theparamter scalars (actually value objects)
#         # ?torch.Tensor is the equivalent to our Value() class hmmmm?
#         return self.w + [self.b]


# class Layer:
#     def __init__(self,nin,nout):
#         #initialize "nout" neurons each with "nin" inputs
#         self.neurons = [Neuron(nin) for _ in range(nout)]
    
#     def __call__(self,x):
#         #return forward pass of all neurons in the layer
#         #"independently evaluate them"
#         outs = [n(x) for n in self.neurons]
#         return outs[0] if len(outs) == 1 else outs #THIS IS THE CONDITIONAL RETURN SYNTAX DON'T NEED 2 RETURNS
    
#     def parameters(self):
#         #layer is also a module so to match pytorch it will lhave parameters - every module has parameters

#         # params = []
#         # for neuron in self.neurons:
#         #     ps = neuron.parameters()
#         #     params.extend(ps)
#         # return params
#         #SHORTEN THIS TO......

#         return [p for neuron in self.neurons for p in neuron.parameters()] #nested single list comprehension
 
# class MLP:
#     def __init__(self,nin,nouts):
#         #nin = number of inputs - scalar
#         #nout = list of number of neurons in each layer
#         sz = [nin] + nouts #concatenante these 2 together
        
#         #self.layers = [Layer(sz[i],sz[i+1]) for i in range(len(nouts))] #itrate through creating multiple layers

#         self.layers = [Layer(sz[i], sz[i+1], nonlin=i!=len(nouts)-1) for i in range(len(nouts))] #CREATES A FINAL LINEAR LAYER MOTHER FUCKER! #creates a final linear layer

#     def __call__(self,x):
#         #need to pass each output as an input into the next layer
#         #simple as that
#         for layer in self.layers:
#             x = layer(x)
#         return x
    
#     def parameters(self):
#         #same format as above
#         return [p for layer in self.layers for p in layer.parameters()]




