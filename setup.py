"""
Install script for CodeforcesApiPy module
"""
from setuptools import setup
import re

with open(
    "codeforces_api/version.py", "r", encoding="utf-8"
) as f:  # Credits: LonamiWebs
    version = re.search(
        r"^__version__\s*=\s*'(.*)'.*$", f.read(), flags=re.MULTILINE
    ).group(1)

setup(
    name="CodeforcesApiPy",
    version=version,
    description="Implementation of codeforces.com API",
    platforms="any",
    url="https://github.com/VadVergasov/CodeforcesApiPy",
    long_description_content_type="text/markdown",
    long_description=open("README.md").read(),
    author="VadVergasov",
    author_email="vadim.vergasov2003@gmail.com",
    license="MIT",
    packages=["codeforces_api"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="codeforces api python",
    install_requires=["requests", "lxml"],
)
