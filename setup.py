"""
Install script for CodeforcesApiPy module
"""
from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()

setup(
    name="CodeforcesApiPy",
    version="1.0.0",
    description="Implementation of codeforces.com api",
    platforms="any",
    url="https://github.com/VadVergasov/CodeforcesApiPy",
    long_description_content_type="text/markdown",
    long_description=long_description,
    author="VadVergasov",
    author_email="vadim.vergasov2003@gmail.com",
    license="MIT",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="codeforces api python",
    install_requires=["requests"],
)
