import unittest
from PIL import Image
from io import BytesIO
from image_augmentations import random_augmentation

class TestRandomAugmentation(unittest.TestCase):

    def test_image_creation(self):
        file = BytesIO()
        image = Image.new('RGBA', size=(50, 50), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        actual = random_augmentation(file)
        expected = file
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
