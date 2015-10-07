wsy_captcha
===================

A library that generates image captcha.

.. image:: https://raw.githubusercontent.com/wushuyi/wsy_captcha/master/test.png

Installation
------------

Install wsy_captcha with pip::

    $ pip install wsy_captcha
    
Base Usage
-----
.. code:: python

    from wsy_captcha.comp import print_
    from wsy_captcha.captcha import Captcha

    captcha = Captcha()
    code = captcha.randomCode()
    print_(code)
    captcha.write(code, 'test.png')

Advanced Usage
-----
.. code:: python

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
