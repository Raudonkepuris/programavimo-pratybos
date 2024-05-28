import random
letters = "abcdefghijklmnopqrstuvwxyz "
message = "slapti egzamino uzduociu atsakymai"

code = ''.join(random.sample(letters,len(letters)))
print(code)

new_message = []

for x in message:
    new_message.append(code[letters.find(x)])

new_message = ''.join(new_message)
print(new_message)

old_message = []

for x in new_message:
    old_message.append(letters[code.find(x)])

old_message = ''.join(old_message)
print(old_message)