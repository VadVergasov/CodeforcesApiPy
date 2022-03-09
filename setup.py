"""
Install script for CodeforcesApiPy module
"""
import re

from setuptools import setup

with open("codeforces_api/version.py", "r", encoding="utf-8") as f:
    version = re.search(
        r"^__version__\s*=\s*\"(.*)\".*$", f.read(), flags=re.MULTILINE
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
    license="GPLv3",
    packages=["codeforces_api"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    keywords="codeforces api python",
    install_requires=["requests", "lxml"],
    python_requires=">=3.7",
)
