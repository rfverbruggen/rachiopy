"""Rachiopy setup script."""
from setuptools import setup

version = '0.2.0-dev'

github_username = 'rfverbruggen'
github_repository = 'rachiopy'

github_path = '{}/{}'.format(github_username, github_repository)
github_url = 'https://github.com/{}'.format(github_path)

download_url = '{}/archive/{}.tar.gz'.format(github_url, version)
project_urls = {
    'Bug Reports': '{}/issues'.format(github_url)
}

setup(
    name='RachioPy',
    version=version,
    author='Robbert Verbruggen',
    author_email='rfverbruggen@icloud.com',
    packages=['rachiopy'],
    install_requires=['requests'],
    url=github_url,
    download_url=download_url,
    project_urls=project_urls,
    license='MIT',
    description='A Python module for the Rachio API.',
    platforms='Cross Platform',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
        ]
)
