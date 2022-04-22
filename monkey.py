import random
import string
import sys

try:
	target = sys.argv[1]
except:
	target = input(">")
randomLetter = ""
tries = []

for index in range(len(target)):
	tries.append(0)

for _ in range(len(target)):
	randomLetter = (random.choice(string.ascii_letters+" ")) # those 2 linex fix double letter error
	tries[_]+=1												 # idk how and why 
	while (randomLetter!=target[_]):
		# possible charsets: string.printable for every character, string.ascii_letters+" " for english letters and string.digits for digits
		randomLetter = (random.choice(string.printable))
		# print(randomLetter)
		tries[_]+=1

print(tries)
print(sum(tries), "monkey keybashes needed to type", target)
