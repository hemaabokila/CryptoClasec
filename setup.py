from setuptools import setup, find_packages

setup(
    name="CryptoClasec",
    version="1.0.0",
    description="A library for various cryptography algorithms (Caesar, Hill Cipher.)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Ibrahem Abo kila",
    author_email="ibrahemabokila@gmail.com",
    url="https://github.com/hemanamo/CryptoClasec",
    packages=find_packages(),
    install_requires=[
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
