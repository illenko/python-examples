import random as r

print(r.randrange(10))
print(r.randrange(10, 20))

up_to_ten = list(range(10))

r.shuffle(up_to_ten)
print(up_to_ten)

print(r.choice(up_to_ten))

lottery_numbers = range(60)
winning_numbers = r.sample(lottery_numbers, 6)
print(winning_numbers)
