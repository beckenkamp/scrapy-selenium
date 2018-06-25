"""This module contains the packaging routine for the pybook package"""

from setuptools import setup, find_packages


setup(
    packages=find_packages(),
    install_requires=[
        'scrapy>=1.0.0',
        'selenium>=3.9.0',
    ]
)


