from setuptools import setup, find_packages

with open("requirements.txt") as requirements_file:
    install_requirements = requirements_file.read().splitlines()

setup(
    name="sundir",
    version="0.3.0",
    description="Sun Direction Calculator.",
    author="Takayuki Matsuda",
    packages=find_packages(exclude=["tests*"]),
    install_requires=install_requirements,
    entry_points={"console_scripts": ["sundir=sundir.sun_dir_calc:main",]},
    classifiers=["Programming Language :: Python :: 3.7",],
)
