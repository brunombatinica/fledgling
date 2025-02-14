from urllib.request import urlopen

#url = "http://olympus.realpython.org/profiles/aphrodite"
#url = "http://localhost:8000/MNIST_input_test.html"
url = "http://localhost:8000/html_test.html"

page = urlopen(url)

print(page.read())

print("\n")

print(page.read().decode("utf-8"))

