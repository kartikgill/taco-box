from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="taco-box",
    version="0.0.1",
    author="Kartik Chaudhary",
    author_email="kartikgill96@gmail.com",
    description="An implementation library of Tiling and Corruption (TACo) Augmentations for OCR/HTR!",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/kartikgill/taco-box",
    packages=find_packages(),
    install_requires=[matplotlib],
    classifiers=["Programming Language :: Python :: 3.7", "License :: Apache 2.0"],
)
