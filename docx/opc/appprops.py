# encoding: utf-8

"""
The :mod:`pptx.packaging` module coheres around the concerns of reading and
writing presentations to and from a .pptx file.
"""

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)


class AppProperties(object):
    """
    Corresponds to part named ``/docProps/app.xml``, containing the app
    document properties for this document package.
    """

    def __init__(self, element):
        self._element = element
        print(self._element)

    @property
    def company(self):
        return self._element.company_text

    @company.setter
    def company(self, value):
        self._element.company_text = value