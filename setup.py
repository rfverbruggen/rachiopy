"""Rachiopy setup script."""
from setuptools import setup

setup(
    name='RachioPy',
    version='0.1.1',
    author='Robbert Verbruggen',
    author_email='rfverbruggen@icloud.com',
    packages=['rachiopy'],
    install_requires=['httplib2'],
    url='https://github.com/rfverbruggen/rachiopy',
    download_url='https://github.com/rfverbruggen/rachiopy/archive/0.1.1.tar.gz',
    license='MIT',
    description='A Python module for the Rachio API.',
    long_description=open('README.md').read(),
    platforms='Cross Platform',
    classifiers=[
        'Development Status :: 0.1.1 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
        ]
)
