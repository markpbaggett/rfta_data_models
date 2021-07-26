from setuptools import setup, find_packages

with open("README.md", "r") as read_me:
    long_description = read_me.read()


setup(
    name="RFTA Data Model",
    description="a temporary repository for describing the RFTA data model",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    version="0.0.1",
    author="Mark Baggett",
    author_email="mbagget1@utk.edu",
    maintainer_email="mbagget1@utk.edu",
    url="https://github.com/markpbaggett/trace_data_models",
    packages=find_packages(),
    extras_require={
        "docs": [
            "sphinx >= 1.4",
        ]
    },
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    keywords=["libraries", "institutional repositories"],
)