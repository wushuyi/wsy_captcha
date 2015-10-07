wsy_captcha
===================

A library that generates image captcha.

.. code:: python
    from captcha.comp import print_
    from captcha.captcha import Captcha
    import captcha.image as image
    captcha = Captcha()
    code = captcha.randomCode()
    print_(code)
    captcha.write('test.png')
    