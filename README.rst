wsy_captcha
===================

A library that generates image captcha.

.. image:: https://raw.githubusercontent.com/wushuyi/wsy_captcha/master/test.png

Installation
------------

Install wsy_captcha with pip::

    $ pip install wsy_captcha
    
Usage
-----
.. code:: python

    from captcha.comp import print_
    from captcha.captcha import Captcha
    import captcha.image as image
    
    captcha = Captcha()
    code = captcha.randomCode()
    print_(code)
    captcha.write('test.png')
    