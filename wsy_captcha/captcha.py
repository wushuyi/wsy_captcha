# -*- coding: utf-8 -*-
__author__ = 'wushuyi'

import os
import random
from wsy_captcha.comp import BytesIO
import wsy_captcha.image as image

FONTS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'fonts')
DEFAULT_FONTS = [os.path.join(FONTS_DIR, 'CoasterShadow.ttf')]
DEFAULT_LIST = [
    "A", "B", "C", "E", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "T", "U", "V", "W", "X", "Y", "Z",
    "2", "3", "4", "6", "7", "8", "9"
]

__all__ = ['Captcha', 'DEFAULT_LIST']


class _Captcha(object):
    def generate(self, chars, format='png'):
        """Generate an Image Captcha of the given characters.
        :param chars: text to be generated.
        :param format: image file format
        """
        im = self.generate_image(chars)
        out = BytesIO()
        im.save(out, format=format)
        out.seek(0)
        return out

    def write(self, chars, output, format='png'):
        """Generate and write an image CAPTCHA data to the output.
        :param chars: text to be generated.
        :param output: output destionation.
        :param format: image file format
        """
        im = self.generate_image(chars)
        return im.save(output, format=format)

    def randomCode(self, length=4):
        """ Generate random code """
        return random.sample(DEFAULT_LIST, length)


class Captcha(_Captcha):
    """Create an image CAPTCHA with wheezy.captcha."""

    def __init__(self, width=200, height=75, fonts=None):
        self._width = width
        self._height = height
        self._fonts = fonts or DEFAULT_FONTS

    def generate_image(self, chars):
        text_drawings = [
            image.warp(),
            image.rotate(),
            image.offset(),
        ]
        fn = image.captcha(
            drawings=[
                image.background(),
                image.text(fonts=self._fonts, drawings=text_drawings),
                image.curve(),
                image.noise(),
                image.smooth(),
            ],
            width=self._width,
            height=self._height,
        )
        return fn(chars)
