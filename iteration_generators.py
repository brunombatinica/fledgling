class countdown(object):
    def __init__(self,start):
        self.count = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= 0:
            raise StopIteration
        r = self.count
        self.count -= 1
        return r

    def __str__(self):
        return str(self.count)

a = countdown(10)

for i in a:
    print(a)


def gencountdown(n):
    while n > 0:
        yield n
        n -=1

b = gencountdown(10)
c = list()

d = [i for i in gencountdown(20)]

for i in b:
    c.append(i)

print(c)
print(d)