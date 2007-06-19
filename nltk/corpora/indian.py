# Natural Language Toolkit: Indian Language POS-Tagged Corpus Reader
#
# Copyright (C) 2001-2007 University of Pennsylvania
# Author: Steven Bird <sb@ldc.upenn.edu>
#         Edward Loper <edloper@gradient.cis.upenn.edu>
# URL: <http://nltk.sf.net>
# For license information, see LICENSE.TXT

"""
Indian Language POS-Tagged Corpus
Collected by A Kumaran, Microsoft Research, India
Distributed with permission

Contents:
- Bangla: IIT Kharagpur
- Hindi: Microsoft Research India
- Marathi: IIT Bombay
- Telugu: IIIT Hyderabad
"""       

from util import *
from nltk import tokenize
from nltk.tag import string2tags, string2words
import os

items = list(['bangla', 'hindi', 'marathi', 'telugu'])

def _read(files, conversion_function):
    if type(files) is str: files = (files,)

    for file in files:
        path = os.path.join(get_basedir(), "indian", file + ".pos")
        f = open_corpus(path)
        for sent in tokenize.line(f.read()):
            if sent and sent[0] != "<":
                yield conversion_function(sent)

def xreadlines(files = items):
    if type(files) is str: files = (files,)
    for file in files:
        path = os.path.join(get_basedir(), "indian", file + ".pos")
        f = open_corpus(path)
        for line in f:
            yield line

def raw(files = items):
    return _read(files, lambda s: string2words(s, sep="_"))

def tagged(files = items):
    return _read(files, lambda s: string2tags(s, sep="_"))


def sample(language):
    from nltk.corpora import indian
    from nltk import extract
    print language.capitalize() + ":",
    for word, tag in extract(8, indian.tagged(language)):
        print word + "/" + `tag`,
    print

def demo():

    sample('bangla')
    sample('hindi')
    sample('marathi')
    sample('telugu')

if __name__ == '__main__':
    demo()