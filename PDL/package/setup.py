from setuptools import setup, find_packages

VERSION = '1.0' 
DESCRIPTION = 'A package for extracting data from pdl librarys in python'
LONG_DESCRIPTION = '''
A python package for extracting and handling data from `.pdl` librarys more on github.

        https://github.com/itzCozi/Python-Data-Library
'''

# Setting up
setup(
    name="pdlparse", 
    version=VERSION,
    author="Cooper ransom",
    author_email="Cooperransom08@outlook.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[], 
    
    keywords=['python', 'data', 'library', 'minimalistic', 'data', 'like-toml'],
        classifiers= [
            "Development Status :: 1 - Beta",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3",
            "Operating System :: Microsoft :: Windows :: Linux :: Unix",
        ]
)