inputs = [1,2,3,2.5]

weights = [[0.2,0.8,-0.5,1],
            [0.5,-0.91,0.26,-0.5],
            [-0.26,-0.27,0.17,0.87]]

biases = [2, 3, 0.5]

layeroutputs = [] #layer output
for neuron_weights, neuron_bias in zip(weights,biases):
    neuron_output = 0 #output of given neuron
    for n_input,weight in zip(inputs,neuron_weights):
        neuron_output += n_input*weight
    neuron_output += neuron_bias
    layeroutputs.append(neuron_output)
    
print(layeroutputs)
    