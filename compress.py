from PIL import Image
crustiness = 0
print("type file name")
filename = input(">")
try:
    img = Image.open(filename)
except:
    exit()
print("quality(0-100)")
print("if you want to mess it up, type something less than ten")
crustiness = int(input(">"))
for i in range(5):
    img.convert("1")
    img.save("1_" + filename, quality=crustiness)
    img = Image.open("1_" + filename)

img.show()