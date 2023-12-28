# Example file for Python Essential Libraries course by Joe Marini
# demonstrates simple image operations using the Pillow library
from PIL import Image
import os
print(os.getcwd())

# TODO: read an image and examine some basic attributes using the Image class
image = Image.open('c:/SAPDevelop/git_extern/Joe_marini/essential_libraries/Pillow/ImagesArchive/Data.jpeg')
# print(image.filename)
# print(image.format)
# print(image.size)
# print(image.mode)
# print(image.height)
# print(image.width)

# for k, v in image.info.items():
#     print(f'key: {k}  value: {v}')

# print(image.info)
# print(image.is_animated) # does not exist for jpeg
# TODO: use the save function to convert an image to a new type

# outfile = 'c:/SAPDevelop/git_extern/Joe_marini/essential_libraries/Pillow/ImagesArchive/Data2.png'
# image.save(outfile, 'png')
# with Image.open(outfile) as im:
#     print(f'image format is {im.format}')    

# TODO: show the image using the platform viewer app

image.show()
