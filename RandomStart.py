import random

a1 = int(input("Lower bound for random number 1: "))
b1 = int(input("Upper bound for random number 1: "))
a2 = int(input("Lower bound for random number 2: "))
b2 = int(input("Upper bound for random number 2: "))
a3 = int(input("Lower bound for random number 3: "))
b3 = int(input("Upper bound for random number 3: "))

RNG1 = random.randint(a1, b1)
RNG2 = random.randint(a2, b2)
RNG3 = random.randint(a3, b3)
RNGlist = [RNG1, RNG2, RNG3]
print(RNG1, RNG2, RNG3)

Amount = int(input("How many floats? "))
for i in range(Amount):
    RngFloat = random.random()
    RNGlist.append(RngFloat)
    print(RngFloat)

mu = int(input("How big should mu be? "))
sigma = int(input("How big should sigma be? "))

GaussNormal = random.gauss(mu, sigma)
print("Normal order:", GaussNormal)
RNGlist.append(GaussNormal)

GaussReverse = random.gauss(sigma, mu)
print("Reverse order:", random.gauss(sigma, mu))
RNGlist.append(GaussReverse)

print(RNGlist)
random.shuffle(RNGlist)
print(RNGlist)
