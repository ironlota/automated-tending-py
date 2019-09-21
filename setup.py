#!/usr/bin/env python
import io
import re
from setuptools import setup, find_packages
import sys

with io.open('./emmerich_atm/__init__.py', encoding='utf8') as version_file:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")


with io.open('README.rst', encoding='utf8') as readme:
    long_description = readme.read()


setup(
    name='emmerich_atm',
    version=version,
    description='Automated Tending Machine',
    long_description=long_description,
    author='Ray Andrew',
    author_email='raydreww@gmail.com',
    license='MIT license',
    packages=find_packages(
        exclude=[
            'docs',
            'tests',
            'windows',
            'macOS',
            'linux',
            'iOS',
            'android',
            'django'
        ]
    ),
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT license',
    ],
    install_requires=[
    ],
    options={
        'app': {
            'formal_name': 'Automated Tending Machine',
            'bundle': 'emmerich'
        },

        # Desktop/laptop deployments
        'macos': {
            'app_requires': [
            ]
        },
        'linux': {
            'app_requires': [
            ]
        },
        'windows': {
            'app_requires': [
            ]
        },

        # Mobile deployments
        'ios': {
            'app_requires': [
            ]
        },
        'android': {
            'app_requires': [
            ]
        },

        # Web deployments
        'django': {
            'app_requires': [
            ]
        },
    }
)
