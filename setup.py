from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='epicprint',  
    version='0.4',
    author="Anders Jürisoo",
    author_email="jurisoo@hotmail.com",
    description="Custom print with superpowers",
    long_description=long_description,
    url="https://github.com/ajthinking/epicprint",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)