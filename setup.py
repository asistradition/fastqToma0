from setuptools import setup, find_packages

setup(
    name="fastqTomat0",
    version="0.0.0",
    license="MIT",
    description="Processing and manipulation of single-cell data",
    author="Chris Jackson",
    packages=find_packages(exclude=["tests"]),
)