from PIL import Image
import random

def random_augmentation(image: Image):
    augmentations = [rotate, fliplr, do_nothing, do_all,skew]
    func = random.choice(augmentations)
    return func(image)

def do_nothing(image: Image):
    return image

def fliplr(image: Image):
    return image.transpose(Image.FLIP_LEFT_RIGHT)

def rotate(image: Image):
    return image.rotate(random.randint(0,365))

def skew(image: Image):
    width, height = image.size
    m = -0.5
    xshift = abs(m) * width
    new_width = width + int(round(xshift))
    image = image.transform((new_width, height), Image.AFFINE,
    (1, m, -xshift if m > 0 else 0, 0, 1, 0), Image.BICUBIC)
    return image

def do_all(image: Image):
    return skew(rotate(fliplr(image)))
