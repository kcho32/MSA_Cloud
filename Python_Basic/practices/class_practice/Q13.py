import random

num = list(range(1,46))
print(num)
hit = []

for i in range(6):
    number = random.choice(num)
    print(number)
    num.remove(number)
    hit.append(number)

print(hit)