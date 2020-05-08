from PIL import Image, ImageEnhance, ImageOps

print ("type file name")
filename = input(">")
try:
    img = Image.open("1_" + filename).convert('RGB')
except:
    exit()
print ("inverted?(y/N)")
temp = input(">")
if temp=="Y":
    invert=True
else:
    invert=False

img.save("1_"+filename)
img = ImageEnhance.Contrast(img).enhance(50)
img = img.resize((204,94))
if invert:
    img = ImageOps.invert(img)
img = img.convert('1')
img.save("1_"+filename,"PNG",optimize=True)

img.show()