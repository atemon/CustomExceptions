"""Setup.py file for atemon.CustomExceptions package."""
from distutils.core import setup

setup(
    name='Atemon-CustomExceptions',
    version='1.0.0.0',
    packages=['atemon', 'atemon.CustomExceptions'],
    long_description="Check if the given email address is valid or not using nslookup",
    author="Varghese Chacko",
    author_email="varghese@atemon.com",
    url="https://github.com/atemon/CustomExceptions",
    provides=["CustomExceptions"],
    license="MIT License",
)
