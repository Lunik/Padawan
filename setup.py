#!/usr/bin/env python

from distutils.core import setup

setup(name='PadawanV6',
      version='0.1.0',
      description='Reverse DNS resolver for IPv6',
      author='Guillaume Lunik',
      author_email='contact@lunik.xyz',
      url='https://github.com/Lunik/PadawanV6',
      packages=['padawanv6', 'padawanv6/lib'],
      scripts=['scripts/padawanv6'],
      data_files=[
          ('/etc/padawanv6', ['config.yml.dist'])
      ]
)
