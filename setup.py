import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='print',  
     version='0.1',
     author="Anders Jürisoo",
     author_email="jurisoo@hotmail.com",
     description="Custom print with superpowers",
     url="https://github.com/ajthinking/print",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )