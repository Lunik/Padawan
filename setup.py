#!/usr/bin/env python

from distutils.core import setup

setup(name='Padawan',
      version='0.1.0',
      description='Reverse DNS resolver',
      author='Guillaume Lunik',
      author_email='contact@lunik.xyz',
      url='https://github.com/Lunik/PadawanV6',
      packages=['padawan', 'padawan/lib'],
      scripts=['scripts/padawan'],
      data_files=[
          ('/etc/padawan', ['config.yml.dist']),
          ('/lib/systemd/system', ['scripts/service/padawan.service'])
      ]
)
