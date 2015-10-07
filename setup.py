# -*- coding: utf-8 -*-
__author__ = 'wushuyi'
import os
from setuptools import setup, find_packages
import wsy_captcha


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def get_requirements(suffix=''):
    with open('requirements%s.txt' % suffix) as f:
        rv = f.read().splitlines()
    return rv


def get_data(path):
    _ROOT = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(_ROOT, path)


setup(
    name="wsy_captcha",
    version=wsy_captcha.__version__,
    url='https://github.com/wushuyi/wsy_captcha',
    author=wsy_captcha.__author__,
    author_email=wsy_captcha.__author_email__,
    description='A library that generates image captcha.',
    long_description=read('README.rst'),
    license='BSD',
    packages=find_packages(),
    install_requires=get_requirements(),
    tests_require=get_requirements('-dev'),
    include_package_data=True,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
