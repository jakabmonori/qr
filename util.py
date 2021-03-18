from PIL import Image


def resize_image(image, size1, size2):
    size = size1, size2
    image.thumbnail(size)
    return image