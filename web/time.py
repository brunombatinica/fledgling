import time


while True:
    folder = "C:/Users/bruno/OneDrive - The University of Auckland/Documents/code/python/web/"
    input_name = "input_test.txt"
    file = open(folder + input_name)
    X = file.read()
    
    print(X)
    
    
    time.sleep(1)