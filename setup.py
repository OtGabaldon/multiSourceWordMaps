import setuptools
from setuptools import setup
from setuptools.command.install import install
from distutils.command.build_py import build_py
import os
from multiSourceWordMap.configEditor import ConfigEditor
import sys

class BuildConfiguresScriptDir(build_py):
    def run(self):
        build_py.run(self)
        if self.dry_run:
            return
        ConfigEditor(
            package_path= os.path.realpath(__file__)[:-1]
        )
        

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.readlines()

setuptools.setup(
    name="multiSourceWordMaps",
    version="0.0.4",
    author="Ot Gabaldon Torrents",
    author_email="gabaldonot@gmail.com",
    description="Allows the user to list sources and compile word maps from those sources",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.thisiswhy.biz",
    project_urls={
        "Bug Tracker": "https://www.thisiswhy.biz",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires = requirements,
    entry_points= {
        'console_scripts': [
            'map = multiSourceWordMap.wordMapCreator:main'
        ]
    },
        cmdclass= {
        'build_py': BuildConfiguresScriptDir,
    }
)