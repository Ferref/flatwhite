# setup.py

from setuptools import setup, find_packages

setup(
    name='flatwhite',
    version='0.3.5',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
    entry_points={
        'console_scripts': [
            # If you have command-line scripts, list them here
        ],
    },
    url='https://github.com/Ferref/flatwhite',
    license='MIT',
    author='Ferenc Kovács',
    author_email='kovacsferenc026@gmail.com',
    description='A package for validating formats and handling files.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
