# Copyright (c) 2017 TinEye. All rights reserved worldwide.

import os
import sys
import unittest

from tineyeservices import Image

imagepath = os.path.abspath("test/images")
sys.path.append('../')


class TestImage(unittest.TestCase):
    """ Test Image class. """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_image(self):
        # Image upload
        image = Image(filepath='%s/banana.jpg' % imagepath, collection_filepath='folder/banana.jpg')
        self.assertTrue(image.data is not None)
        self.assertEquals(image.url, '')
        self.assertEquals(image.collection_filepath, 'folder/banana.jpg')
        self.assertEquals(image.metadata, None)

        # URL
        image = Image(url='https://tineye.com/images/meloncat.jpg', collection_filepath='meloncat.jpg')
        self.assertEquals(image.data, None)
        self.assertEquals(image.collection_filepath, 'meloncat.jpg')
        self.assertEquals(image.url, 'https://tineye.com/images/meloncat.jpg')
        self.assertEquals(image.metadata, None)

        # Not supplying any information
        try:
            image = Image()
        except ValueError, e:
            self.assertEquals(e.args[0], 'Image object needs either data or a URL.')
