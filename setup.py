# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()


setup(
    name='azure webcam uploader',
    version='0.1.0',
    description='webcam uploader to Azure',
    long_description=readme,
    author='LLJ',
    
    
    packages=find_packages(exclude=('tests', 'docs'))
)

