import random
import datetime

num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
char = ["$", "@", "!", "^", "%", "*", "#", "_", "-"]

a = int(input("How many numbers do you want in your password:-"))
b = int(input("How many letters do you want in your password:-"))
c = int(input("How many symbols do you want in your password:-"))
name = input('A name for that password:-')

p1 = [random.choice(num_list) for i in range(a)]
p2 = [random.choice(letters_list) for r in range(b)]
p3 = [random.choice(char) for k in range(c)]
password = []


def loop(lis):
    for i in lis:
        i = str(i)
        password.append(i)


loop(p1)
loop(p2)
loop(p3)

t = datetime.date.today()
print(*password)
with open('passwords.txt', 'a') as f:
    f.write(f'{name.upper()}- password({"".join(password)})-created on {t}\n')