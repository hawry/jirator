import setuptools
import re
import os
from jirator.constant import VERSION

with open("README.md","r") as fh:
    long_desc = fh.read()

setuptools.setup(
    name="jirator",
    version=VERSION,
    author="hawry",
    entry_points = {
        "console_scripts": ["jirator=jirator.jirator:main"]
    },
    author_email="hawry@hawry.net",
    description="Fetch your assigned JIRA issues and checkout new branches with their ID",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/hawry/jirator",
    packages=setuptools.find_packages(),
    install_requires=[
        "console-menu",
        "jira",
        "click"
    ],
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Development Status :: 3 - Alpha"
    ]
)
