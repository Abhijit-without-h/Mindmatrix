from setuptools import setup, find_packages

setup(
    name="mindmatrix",
    version="0.1.0",
    author="Abhijit S.R. ",
    author_email="abhijitsr92@gmail.com",
    description="A package for matrix analysis and pattern-based computations.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/abhijit-without-h/mindmatrix",
    packages=find_packages(),
    install_requires=[
        "numpy"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
