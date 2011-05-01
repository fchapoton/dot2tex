# -*- coding: Latin-1 -*-
"""Convert graphviz graphs to LaTeX-friendly formats

Various tools for converting graphs generated by the graphviz library
to formats for use with LaTeX.

Copyright (c) 2006-2009, Kjell Magne Fauske

"""

# Copyright (c) 2006-2009, Kjell Magne Fauske
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

__author__ = 'Kjell Magne Fauske'
__version__ = '2.8.7dev'
__license__ = 'MIT'


import dot2tex as d2t
from pyparsing import ParseException

def get_logstream():
    return d2t.logstream


def dot2tex(dotsource,**kwargs):
    """Process dotsource and return LaTeX code

    Conversion options can be specified as keyword options. Example:
        dot2tex(data,format='tikz',crop=True)

    """
    return d2t.convert_graph(dotsource,**kwargs)


testgraph = """
digraph G {
    a_1-> a_2 -> a_3 -> a_1;
}
"""
  


