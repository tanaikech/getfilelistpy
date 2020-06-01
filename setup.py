#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

__author__ = 'Kanshi TANAIKE'

with open('README.md') as f:
    readme = f.read()

setup(
    name='getfilelistpy',
    version='1.0.6',
    description='This is a python library to retrieve the file list with the folder tree from the specific folder of Google Drive.',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Kanshi TANAIKE',
    author_email='tanaike@hotmail.com',
    install_requires=['google-api-python-client'],
    url='https://github.com/tanaikech/getfilelistpy',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
    ],
    packages=find_packages(),
    keywords=['google drive', 'drive api', 'folder structure', 'folder tree', 'folder hierarchy', 'file list'],
    license='MIT License',
    test_suite='tests'
)
