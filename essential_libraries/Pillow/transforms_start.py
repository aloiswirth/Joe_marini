# Example file for Python Essential Libraries course by Joe Marini
# demonstrates image transformations using the Pillow library
from PIL import Image, ImageFilter, ImageOps

# TODO: use the crop function to crop an image
infile = "c:/SAPDevelop/git_extern/Joe_marini/essential_libraries/Pillow/ImagesArchive/Connections.jpeg"
# with Image.open(infile) as image:
#     image.show()
# image.crop((0,0,1000,1000)).show()
# with Image.open(infile) as img:
#     midx = img.width // 2
#     midy = img.height // 2
#     croparea = (midx - 400, midy - 250, midx + 400, midy + 250)
#     cropimg = img.crop(croparea)
#     cropimg.show()

# TODO: perform a simple resize and rotation
# image.resize((200, 200)).rotate(90).show()
# with Image.open(infile) as img:
#     newimg = img.resize((256, 256))
#     newimg = newimg.rotate(45)
#     newimg.show()

# TODO: use the transpose function with a built-in operation
# with Image.open(infile) as img:
#     newimg = img.transpose(Image.FLIP_TOP_BOTTOM)
#     newimg.show()

# TODO: Use an ImageFilter operation
# with Image.open(infile) as img:
#     newimg = img.filter(ImageFilter.GaussianBlur(20))
#     newimg.show()

# TODO: Use ImageOps for built-in image processing
with Image.open(infile) as img:
    # newimg = ImageOps.grayscale(img)
    # newimg.show()
    # newimg = ImageOps.posterize(img, 3)
    # newimg.show()
    # newimg = ImageOps.solarize(img, 128)
    # newimg = ImageOps.equalize(img)
    # newimg = ImageOps.autocontrast(img)
    # newimg = ImageOps.invert(img)
    newimg = ImageOps.autocontrast(img)
    newimg.show()

