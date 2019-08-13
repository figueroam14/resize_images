from PIL import Image
import os
import sys

# Path to images you wish to resize
path = "images/"
dirs = os.listdir(path)

# Final image size in pixels
final_size = 244


def resize_image():
    for img in dirs:
        if img == '.DS_Store':
            continue
        if os.path.isfile(path+img):
            im = Image.open(path+img)
            f, e = os.path.splitext(path+img)
            size = im.size
            ratio = float(final_size) / max(size)
            new_image_size = tuple([int(x*ratio) for x in size])
            im = im.resize(new_image_size, Image.ANTIALIAS)
            new_im = Image.new("RGB", (final_size, final_size))
            new_im.paste(
                im, ((final_size-new_image_size[0])//2, (final_size-new_image_size[1])//2))
            new_im.save(f + '_resized.jpg', 'JPEG', quality=90)


resize_image()
