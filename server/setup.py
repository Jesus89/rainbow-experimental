#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='Rainbow',
      version='0.0.0',
      description='Web wrapper for Python modules',
      long_description=open('README.md').read(),
      author='Jesús Arroyo Torrens',
      author_email='jesus.arroyo@bq.com',
      url='https://github.com/bqlabs/rainbow-server',
      license='GPLv2',
      packages=['rainbow', 'rainbow.app'],
      install_requires=['bottle==0.12.9'],
      entry_points={
          'console_scripts': [
              'rainbow = rainbow:main'
          ]
      })
