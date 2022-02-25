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


class HTTPException(BasicException):
    pass


class BadRequest(HTTPException):
    http_code = 400
    http_message = 'Bad request'


class Unauthorized(HTTPException):
    http_code = 401
    http_message = 'Unauthorized'


class PaymentRequired(HTTPException):
    http_code = 402
    http_message = 'Payment Required'


class Forbidden(HTTPException):
    http_code = 403
    http_message = 'Forbidden'


class ResourceNotFound(HTTPException):
    http_code = 404
    http_message = 'Resource not found'


class MethodNotAllowed(HTTPException):
    http_code = 405
    http_message = 'Method not allowed'


class InternalServerError(HTTPException):
    pass


class NotImplemented(HTTPException):
    http_code = 501
    http_message = 'Not implemented'
