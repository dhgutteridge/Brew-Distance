.. image:: https://travis-ci.org/dhgutteridge/Brew-Distance.svg?branch=master
    :target: https://travis-ci.org/dhgutteridge/Brew-Distance

.. image:: https://badge.fury.io/py/Brew-Distance.svg
    :target: https://badge.fury.io/py/Brew-Distance

Brew-Distance
=============

A Python module that implements the Brew edit distance algorithm. In
simple terms, it compares two strings and determines the number of edits
required to make the first the same as the second, typically for use
when weighing multiple potentially similar strings in a data set.

This is a mostly faithful remake of
`Perl's Text::Brew <https://metacpan.org/pod/Text::Brew>`_ implementation,
except "INITIAL" matches aren't reported in output, since that isn't
meaningful. (And of course, it's written in a Pythonic idiom.) The Perl
implementation itself states that it varies from the original Brew
version, and I have followed it.

This module isn't intended to be the most efficient determiner of edit
distance; rather, it's concerned with simply offering the Brew
algorithm in pure Python, which provides not just edit distance, but
the edit steps taken to determine it. It also allows each edit type
("MATCH", "DEL", "INS", "SUBST") to be re-weighted, one of its main
points of difference. This implementation is useful for cases where
real-time performance is not a consideration, but re-weighting edit
types or the post-processing evaluation of edit steps is a requirement.
(Also, as it's a simple, pure Python implementation, it could be easily
customized, and it could be used as a sample implementation for
educational purposes.) (`See also`_.)

Installing and uninstalling
---------------------------

The easiest way to install is using pip:

::

    pip install brew-distance

Alternatively you can clone this git repo and install using
setuptools:

::

    git clone git@github.com:dhgutteridge/brew-distance.git
    cd brew-distance
    python setup.py install

To uninstall with pip:

::

    pip uninstall brew-distance

Usage
-----

Interface
~~~~~~~~~

::

    function distance(string1, string2, output='both', cost=[0, 1, 1, 1])
        Determine the Brew edit distance between two strings.

        string1 is the string to be transformed.

        string2 is the transformation target.

        Optional output is a string containing "distance", "edits", or
        "both", which determine results output, see below.

        Optional cost is a four element array of numbers used to adjust
        the costs of matches, insertions, deletions, and substitutions.
        (It is not recommended that match costs be adjusted: the algorithm
        is predicated on match having a lower cost than other operations.)

        The results vary depending on the output option:
            "distance": provides the edit distance as a number.
            "edits": provides an array with the list of edit actions.
            "both: provides a tuple containing the output of both
            previous options.

    class BrewDistanceException(builtins.Exception)
        Brew-Distance-specific exception used with argument validation.

Example
~~~~~~~

::

    import brew_distance

    try:
        print("Determining results for 'four' vs. 'foo':")
        print(str(brew_distance.distance("four", "foo", "both")))
    except brew_distance.BrewDistanceException as error:
        print(str(error))

Notes
~~~~~

Character comparisons are case-sensitive.

There are no special considerations concerning the relatedness of
various Unicode characters, e.g. a German Eszett (double-S) character
is not considered equivalent to two S characters. Characters are dealt
with as raw code points, without any semantic weighting. Such
processing would require extension by the end user.

Under Python 2, all non-Unicode strings are converted to UTF-8 encoding
to try to ensure multi-byte characters are treated correctly.

Compatibility
-------------

Brew-Distance supports Python 2.6, 2.7, and 3.2+. It does not support
Python < 2.6, as it requires **namedtuple** from **collections**. (Its
test script is mostly compatible with Python 2.6 even though it imports
the old version of **unittest**. However, due to
`Python bug 10417 <https://bugs.python.org/issue10417>`_, tests that
include non-ASCII characters are disabled on Python 2.6. They will also
trigger exceptions in Python 2.7 environments that aren't set to a
locale that supports these characters, but the tests have been left
enabled for Python 2.7, to demonstrate it's supported. Also, an
exception handling test is disabled in Python 2.6 due to an
incompatibility with its **unittest**.)

License
-------

Brew-Distance is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation; either version 2 of the License, or (at your
option) any later version.

See the file LICENSE.txt for the full text of GNU General Public License
version 2.

Alternate options
-----------------

There are many alternate options for edit distance calculations, perhaps
most notably `python-Levenshtein <https://github.com/ztane/python-Levenshtein/>`_,
which offers far more features in general, except it does not
(at present) allow for re-weighting edit types.

Another project under development (at the time of writing) is
`weighted-levenshtein <https://github.com/infoscout/weighted-levenshtein/>`_,
which also offers re-weighting of edit types, but (as of version 0.2)
does not support Unicode, and isn't tested on as many Python releases.
However, it allows for re-weighting of individual characters, for more
fine-grained analysis, e.g. to flag typical typing transposition errors.

See also
--------

The original article by Chris Brew that defines this algorithm is archived
here: `Calculating Edit Distance Between Sequences <http://archive.is/20140611111436/www.ling.ohio-state.edu//%7Ecbrew/795M/string-distance.html>`_.

`Perl's Text::Brew`_.

python-Levenshtein_ and weighted-levenshtein_.

The Wikipedia `edit distance <https://en.wikipedia.org/wiki/Edit_distance>`_
article is a good starting point to learn more about edit distance
algorithms in general, and various enhancements that can be made to them.

Another good article that discusses optimizations and character weightings is
`Beyond StringUtils.getLevenstheinDistance <http://bend-ing.blogspot.ca/2008/06/beyond-stringutilsgetlevensteindistance.html?m=1>`_.
It offers ideas for improving the basic Brew edit distance algorithm.

Credits
-------

Credit is due first and foremost to Chris Brew, the creator of the
algorithm. Also, mention should be made of Dree Mistrut and Keith C.
Ivey, who respectively created and maintained the Perl Text::Brew
implementation on which this is based.

Author
------

Copyright (C) 2017 David H. Gutteridge

FAQs
----

*What motivated you to write this?*

I once had occasion to use the Perl Brew implementation as part of a
project to relate data from disparate systems. I needed something that
let me re-weight particular edits depending on the context (e.g. two
strings of unequal length that matched up to the point the shorter one
ended were considered a probable match if the shorter one came from a
legacy system that had limited text fields), and Text::Brew fit the
bill. I thought it would be nice to have a Python version available too,
in part because the Perl implementation didn't support Unicode, and I
was dealing with data in languages other than English.

*Why license it under the GPL?*

Because the Perl implementation on which this was based was offered
either under the Perl Artistic License or the GPL. It didn't make sense
to me to offer Python code under the Perl Artistic Licence, so it seemed
appropriate in spirit to keep it GPL.
