# encoding: utf-8

"""Custom element classes for app properties-related XML elements"""

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

import re

from datetime import datetime, timedelta

from docx.compat import is_string
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls, qn
from docx.oxml.xmlchemy import BaseOxmlElement, ZeroOrOne


class CT_AppProperties(BaseOxmlElement):
    """
    ``<Properties>`` element, the root element of the App Properties
    part stored as ``/docProps/app.xml``. String elements resolve to an empty string
    ('') if the element is not present in the XML. String elements are
    limited in length to 255 unicode characters.
    """
    company = ZeroOrOne('Company', successors=())

 #   _appProperties_tmpl = (
 #       '<Properties %s/>\n' % nsdecls('ep', 'vt')
 #   )

    _appProperties_tmpl = (
        '<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">'
    )

    @classmethod
    def new(cls):
        """
        Return a new ``<Properties>`` element
        """
        xml = cls._appProperties_tmpl
        appProperties = parse_xml(xml)
        return appProperties
        
    @property
    def company_text(self):
        return self._text_of_element('company')

    @company_text.setter
    def company_text(self, value):
        self._set_element_text('company', value)


    def _get_or_add(self, prop_name):
        """
        Return element returned by 'get_or_add_' method for *prop_name*.
        """
        get_or_add_method_name = 'get_or_add_%s' % prop_name
        get_or_add_method = getattr(self, get_or_add_method_name)
        element = get_or_add_method()
        return element

    @classmethod
    def _offset_dt(cls, dt, offset_str):
        """
        Return a |datetime| instance that is offset from datetime *dt* by
        the timezone offset specified in *offset_str*, a string like
        ``'-07:00'``.
        """
        match = cls._offset_pattern.match(offset_str)
        if match is None:
            raise ValueError(
                "'%s' is not a valid offset string" % offset_str
            )
        sign, hours_str, minutes_str = match.groups()
        sign_factor = -1 if sign == '+' else 1
        hours = int(hours_str) * sign_factor
        minutes = int(minutes_str) * sign_factor
        td = timedelta(hours=hours, minutes=minutes)
        return dt + td

    _offset_pattern = re.compile(r'([+-])(\d\d):(\d\d)')

    def _set_element_text(self, prop_name, value):
        """Set string value of *name* property to *value*."""
        if not is_string(value):
            value = str(value)

        if len(value) > 255:
            tmpl = (
                "exceeded 255 char limit for property, got:\n\n'%s'"
            )
            raise ValueError(tmpl % value)
        element = self._get_or_add(prop_name)
        element.text = value

    def _text_of_element(self, property_name):
        """
        Return the text in the element matching *property_name*, or an empty
        string if the element is not present or contains no text.
        """
        element = getattr(self, property_name)
        if element is None:
            return ''
        if element.text is None:
            return ''
        return element.text
