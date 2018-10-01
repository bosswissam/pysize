from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pysize",
    version="1.0",
    description="Use to quickly measure the size of your python objects.",
    py_modules=["pysize"],
    package_dir={"": "src"},
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/bosswissam/pysize",
    author="bosswissam",
    author_email="bosswissam@gmail.com",
)
