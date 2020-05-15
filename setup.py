from __future__ import absolute_import
from setuptools import setup, find_packages
from setuptools.command.install import install


setup(
    name="talon",
    version="1.5.1",
    description=("Mailgun library " "to extract message quotations and signatures."),
    long_description=open("README.rst").read(),
    author="Mailgun Inc.",
    author_email="admin@mailgunhq.com",
    url="https://github.com/mailgun/talon",
    license="APACHE2",
    packages=find_packages(exclude=["tests", "tests.*"]),
    include_package_data=True,
    zip_safe=True,
    extras_require={"ml": ["numpy", "scipy", "scikit-learn",]},
    install_requires=[
        "lxml>=2.3.3",
        "regex>=1",
        "chardet>=1.0.1",
        "cchardet>=0.3.5",
        "cssselect",
        "six>=1.10.0",
        "html5lib",
    ],
    tests_require=["mock", "nose>=1.2.1", "coverage"],
)
