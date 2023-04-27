# https://www.freecodecamp.org/news/build-your-first-python-package/
from setuptools import setup, find_packages

VERSION = '1.2' 
DESCRIPTION = 'A package for cryptography in python with unique functions'
LONG_DESCRIPTION = '''
A python package for cryptography and data mixing from strings/files more on github.

        https://github.com/itzCozi/HashBrowns-Python
'''

# Setting up
setup(
    name="hashbrowns", 
    version=VERSION,
    author="Cooper ransom",
    author_email="Cooperransom08@outlook.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[], 
    
    keywords=['python', 'crypto', 'cryptograpgy', 'rsa', 'hashing-algo'],
        classifiers= [
            "Development Status :: 1 - Beta",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3",
            "Operating System :: Microsoft :: Windows :: Linux",
        ]
)