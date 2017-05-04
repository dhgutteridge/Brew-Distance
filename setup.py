from setuptools import find_packages, setup

long_description = """\
Brew-Python implements the Brew edit distance algorithm. This provides
not only the edit distance between two strings, but also (optionally) a
list of the edits required to equalize them. It also allows for the
optional re-weighting of each edit type ("MATCH", "DEL", "INS",
"SUBST"), for customization of edit distance calculations.
"""

setup(
    name='Brew-Python',
    version='1.0.0',
    author='David H. Gutteridge',
    author_email='dhgutteridge@hotmail.com',
    url='http://github.com/dhgutteridge/brew-python',
    packages=find_packages(),
    license='LICENSE.txt',
    description='A Python module that implements the Brew edit distance algorithm.',
    long_description=long_description,
    keywords=['edit', 'distance', 'editdistance', 'levenshtein', 'brew', 'string', 'comparison'],
    test_suite='brew.test',
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development",
        "Topic :: Text Processing",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)"
    ],
    install_requires='setuptools'
)