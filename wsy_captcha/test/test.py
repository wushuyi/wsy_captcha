# -*- coding: utf-8 -*-
__author__ = 'wushuyi'
import sys
import os

PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from wsy_captcha.comp import print_
from wsy_captcha.captcha import Captcha
import wsy_captcha.image as image


class MyCaptcha(Captcha):
    def generate_image(self, chars):
        text_drawings = [
            image.warp(),
            image.rotate(),
            image.offset(),
        ]
        fn = image.captcha(
            drawings=[
                image.background(color='#FFFFFF'),
                image.text(fonts=self._fonts, drawings=text_drawings),
                image.curve(width=2),
                image.curve(width=2),
                image.curve(width=2),
                image.noise(number=60, color='#5C87B2', level=2),
                image.smooth(),
            ],
            width=self._width,
            height=self._height,
        )
        return fn(chars)


captcha = MyCaptcha()
code = captcha.randomCode()
img = captcha.generate(code)
print_(code)
f = open('test.png', 'wb')
f.write(img.read())
f.close()
