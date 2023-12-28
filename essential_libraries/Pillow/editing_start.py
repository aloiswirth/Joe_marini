# Example file for Python Essential Libraries course by Joe Marini
# demonstrates image editing using the Pillow library
from PIL import Image, ImageDraw, ImageFont

infile = "c:/SAPDevelop/git_extern/Joe_marini/essential_libraries/Pillow/ImagesArchive/Connections.jpeg"
# TODO: use the ImageDraw routines to modify an image
with Image.open(infile) as img:
    draw = ImageDraw.Draw(img)
    # draw.line((0, 0) + img.size, width= 40, fill=128)
    # draw.line((0, img.size[1], img.size[0], 0), width = 40,  fill=128)
    # draw.rectangle((100, 100, 400, 400), fill=128)
    # draw.ellipse((100, 100, 400, 400), fill=128)
    # txtfont = ImageFont.truetype("c:/Windows/Fonts/Arial.ttf", 80)
    txtfont = ImageFont.truetype("arial.ttf", 75)  
    textstr = "Hello World"  
    txtsize = draw.textlength(textstr, font=txtfont)
    location = (20, img.height - int(txtsize))
    draw.text(location, textstr, fill=(255, 255, 255), font=txtfont)
    img.show()
    # img.save('c:/SAPDevelop/git_extern/Joe_marini/essential_libraries/PillowImagesArchive/Connections2.jpeg')
    # img.save('c:/SAPDevelop/git_extern/Joe_marini/essential_libraries/PillowImagesArchive/Connections2.png')
    # img.save('c:/SAPDevelop/git_extern/Joe_marini/essential_libraries/PillowImagesArchive/Connections2.bmp')
    # img.save('c:/SAPDevelop/git_extern/Joe_marini/essential_libraries/PillowImagesArchive/Connections2.tiff')
    # img.save('c:/SAPDevelop/git_extern/Joe_marini/essential_libraries/PillowImagesArchive/Connections2.gif')
    # img.save('c:/SAPDevelop/git_extern/Joe_marini/essential_libraries/PillowImagesArchive/Connections2.ico')
    # img.save('c:/SAPDevelop/git_extern/Joe_marini/essential_libraries/PillowImagesArchive/Connections2.webp')
    # img.save('c:/SAPDevelop/git_extern/Joe_marini/essential_libraries/PillowImagesArchive/Connections2.ppm')
    # img.save('c:/SAPDevelop/git_extern/Joe_marini/essential_libraries/PillowImagesArchive/Connections2.pgm')
    # img.save('c:/SAPDevelop/git_extern/Joe_marini/essential_libraries/PillowImagesArchive/Connections2.pbm')
    # img.save('c:/SAPDevelop/git_extern/Joe_marini/essential_libraries/PillowImagesArchive/Connections2.eps')
    # img.save('c:/SAPDevelop/git_extern/Joe_marini/essential_libraries/PillowImagesArchive/Connections2.pdf')
    # img.save('


# TODO: use the ImageDraw routines to modify an image
