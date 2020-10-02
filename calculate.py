import random
n=int(input("Accuracy:"))
inside=0
for i in range(n):
    x=random.randint(1,1000)
    y=random.randint(1,1000)
    if (x**2 + y**2)**0.5 <=1000:
        inside=inside+1
print((inside/n)*4)
