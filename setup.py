# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pywebcrawler',
    version='0.1',
    description='Python Web Crawler',
    long_description=readme,
    author='Potier Thomas',
    author_email='theswagman@gmx.fr',
    url='https://github.com/TheSwagMan/WebCrawler',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

