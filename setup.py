import io
import os
import re

from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())


setup(
    name='practice-python',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pyyaml>=1.2b1',
        'numpy<=1.19.3',
    ],
    license='MIT License',
    description='Pythonic code for common coding problems.',
    long_description=read("README.md"),
    long_description_content_type='text/markdown',
    url='https://github.com/deanagan/practice-python',
    author='Dean Agan',
    author_email='agandfr@gmail.com',
    python_requires='>3.8.0',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries"],
    keywords='python testing',
    test_suite='practice-python.test'
)
