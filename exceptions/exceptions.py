"""Exception handling."""
# -*- coding: utf-8 -*-
#
# Copyright 2016 ATEMON Technology Consultants LLP.
#
# Git Hub: https://github.com/atemon
# Twitter: https://twitter.com/atemontech
#
# This file is part of atemon library and distributed under the MIT license (MIT).
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from django.core.exceptions import ValidationError
from ..lib import FixedDictionary


class BasicException(Exception, FixedDictionary):
    """Create basic dictionary."""

    http_code = 500
    http_message = 'Internal Server Error'
    api_code = 500
    api_message = 'Internal Server Error'
    error_dict = {}
    message_dict = {}

    def __init__(self, message=None, exception=None, count=0, offset=0, limit=100, keyword='', data=[], message_dict={}, *args, **kwargs):
        """Initialize exceptions."""
        self.api_message = message or self.api_message
        if message_dict is {}:
            message_dict = {'error': message}
            self.error_dict = message_dict

        if isinstance(exception, self.__class__):
            self.http_code = exception.http_code
            self.http_message = exception.http_message
            self.api_code = exception.api_code
            self.api_message = exception.api_message
            self.error_dict = exception.error_dict
            self.message_dict = exception.message_dict
        else:
            self.message_dict = message_dict
            self.error_dict = message_dict
            if isinstance(exception, Exception):
                if hasattr(exception, 'messages') and type(exception.messages) is list:
                    self.error_dict['messages'] = exception.messages
                elif hasattr(exception, 'args') and type(exception.args) is tuple:
                    self.error_dict['messages'] = list(exception.args)
                else:
                    self.api_message = exception.messages

                if isinstance(exception, ValidationError):
                    if hasattr(exception, 'message_dict'):
                        for key, value in exception.message_dict.items():
                            self.message_dict.update({key: []})
                            if type(value) is list:
                                self.message_dict[key] += value
                            else:
                                self.message_dict[key].append(str(value))

                    if hasattr(exception, 'error_dict'):
                        for key, value in exception.error_dict.items():
                            self.error_dict.update({key: []})
                            if type(value) is list:
                                for ex in value:
                                    if hasattr(ex, 'messages'):
                                        self.error_dict[key] += ex.messages
                                    else:
                                        self.error_dict[key].append(str(ex))

        Exception.__init__(self, self.api_message)

        FixedDictionary.__init__(self, {
            'code': self.api_code,
            'status': self.api_message,
            "error_dict": self.error_dict,
            "message_dict": self.message_dict,
            'count': count,
            'data': data,
            "offset": offset,
            "limit": limit,
            "keyword": keyword
        })

    def set_http_status(self, code, message=''):
        """Set HTTP Status."""
        self.http_code = code
        self.http_message = message

    def set_response(self, code, message=''):
        """Set API response."""
        self.api_code = code
        self.api_message = message

    def set_message(self, message):
        """Set message."""
        self.api_message = message

    def set_exception(self, exception):
        """Set exception."""
        self.api_message = exception.message
