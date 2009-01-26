#!/usr/bin/env python
########################################################################
#
# pyobjcryst        by DANSE Diffraction group
#                   Simon J. L. Billinge
#                   (c) 2009 trustees of the Michigan State University
#                   All rights reserved.
#
# File coded by:    Chris Farrow
#
# See AUTHORS.txt for a list of people who contributed.
# See LICENSE.txt for license information.
#
########################################################################

"""Test the converters.

This verifies results from tests built into the _registerconverters module.
"""

if __name__ == "__main__":

    import pyobjcryst.registerconverters as converters
    import numpy

    tv = numpy.array(range(3), dtype=float)
    tm = numpy.array(range(6), dtype=float).reshape(3,2)

    # Check to see if the above arrays are equal to the test arrays
    assert( numpy.array_equal(tv, converters.getTestVector()) )
    assert( numpy.array_equal(tm, converters.getTestMatrix()) )

    print "Tests passed!"