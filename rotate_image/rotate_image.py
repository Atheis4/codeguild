from PIL import Image

im = Image.open("../img/008.102.1.2_2768.png")
im.rotate(45).save('rotated.png')
