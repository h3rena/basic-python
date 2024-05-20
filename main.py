import random


name = "nta"
print(f"** {name} **")

print("*********************************")

num = 5
if num == 5:
    print("success")
else:
    print("failure")

print('''
***************

******************
''')

print("sinta herena")

print("*********************************")

input("siapa nama kamu?")

print("*********************************")

nameUser = input("siapa nama kamu?")
print(f"hi  {nameUser}")

print("*********************************")

print(f'''

Halo {nameUser}! coba perhatikan kotak di bawah ini.
[ ]-[ ]-[ ]-[ ]
''')


ucil_position = random.randint(1, 4)

answer = int(input(f"menurut kamu ucil ada di kotak nomor berapa ? [1/2/3/4]: "))
print(f"pilihan kamu adalah {answer} ")

if answer == ucil_position:
    print("horayyyyyyy")
else:
    print("huuuuuh, ucil adanya di kotak {ucil_position}.")

print("*********************************")

usia1 = "17"
usia1 = int("17")
usia2 = 17

print(type(usia1))
print(type(usia2))
print("*********************************")
