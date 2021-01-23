"""
Install script for CodeforcesApiPy module
"""
from setuptools import setup, find_packages

setup(
    name="CodeforcesApiPy",
    version="1.5.1",
    description="Implementation of codeforces.com API",
    platforms="any",
    url="https://github.com/VadVergasov/CodeforcesApiPy",
    long_description_content_type="text/markdown",
    long_description=open("README.md").read(),
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
    install_requires=["requests", "lxml"],
)
