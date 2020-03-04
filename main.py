import os
from PIL import Image

# path = D:\code\python\pic2asc\pic\dedsec.png
# pic2.jpeg
path = ".\\pic\\"


def main(path):
    img = Image.open(path)
    f = open("D:\\code\\python\\pic2asc\\pic\\out.txt", "w")
    W, H = img.size
    print("W = ", W, "\nH = ", H)

    for j in range(0,H):
        if j % 4 == 0:
            for i in range(0,W):
                if i % 2 == 0:
                   pix = img.getpixel((i,j))
                   if type(pix) == int:
                       pix = int(pix / 100 * 25)
                   else:
                       pax = int((pix[0] + pix[1] + pix[2])/3)
                       pax = int(pax / 100 * 25)
                       pix = pax
                   if pix >= 0 and pix < 25:
                       f.write(" ")
                   elif pix >= 25 and pix < 50:
                       f.write(".")
                   elif pix >= 50 and pix < 75:
                       f.write("-")
                   elif pix >= 75 and pix < 100:
                       f.write("/")
            f.write("\n")


if __name__ == '__main__':
    print("enter full name of image ")
    tmp = input()
    path += tmp
    if os.path.exists(path):
        main(path)
    else:
        print("smt goes wrong")

