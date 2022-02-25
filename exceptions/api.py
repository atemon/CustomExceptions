"""API Exceptions."""
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


from .exceptions import BasicException

from .http import (
    BadRequest,
    Unauthorized,
    Forbidden,
    ResourceNotFound,
    MethodNotAllowed,
    InternalServerError,
    NotImplemented as http_NotImplemented,
    # PaymentRequired
)


class APIException(BasicException):
    """Base class for all API exceptions."""

    pass


# HTTP 500 errors

class InvalidJSONKey(APIException, http_NotImplemented):
    """Invalid JSON Key."""

    api_code = 501
    api_message = 'Invalid key for JSON field.'


class InvalidAttribute(APIException, InternalServerError):
    """Invalid JSON Key."""

    api_code = 502
    api_message = 'Invalid attribute for modal object.'


# HTTP 400 errors
class InputValidationError(APIException, BadRequest):
    """Input validation errors."""
    api_code = 400
    api_message = 'Input Validation Error'


class OutOfTokenError(APIException, BadRequest):
    """Out Of Token errors."""

    api_code = 400
    api_message = 'Out of Token Error'


class AuthenticationRequired(APIException, Unauthorized):
    """Authentication required."""

    api_code = 401
    api_message = 'Authentication required'


class APIResourceNotFound(APIException, ResourceNotFound):
    """API resourse not found."""

    api_code = 204
    api_message = "API resource not found"


class APIMethodNotAllowed(APIException, MethodNotAllowed):
    """API Methodnot allowed."""

    api_code = 103
    api_message = "API method not allowed"


class InvalidOutput(APIException, InternalServerError):
    """Invalid ourput."""

    api_code = 505
    api_message = "Invalid output format"


class APIForbiddenRequest(APIException, Forbidden):
    """Forbidden output."""

    api_code = 403
    api_message = "You are forbidden from accessing the resource"
