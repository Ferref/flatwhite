from setuptools import setup, find_packages

setup(
    name='flatwhite',
    version='0.3.8',
    packages=find_packages(),
    install_requires=[
        'requests',  # for web scraping
        're',  # for regex validation (built-in module, so this line is optional)
        'smtplib',  # for sending emails (built-in module, so this line is optional)
        'datetime',  # for date and time handling (built-in module, so this line is optional)
        'os',  # for file and directory handling (built-in module, so this line is optional)
        'shutil',  # for file operations (built-in module, so this line is optional)
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
