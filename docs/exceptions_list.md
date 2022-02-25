
### Exceptions

#### HTTP Exceptions
HTTP Status Code | API Status Code | Reason Phrase                                                      | Ticket | File         | Name
-----------------|-----------------|--------------------------------------------------------------------|--------|--------------|------
400              | 4000            | Bad Request                                                        |        |              |
401              | 4001            | Unauthorized                                                       |        |              |
402              | 4002            | Payment Required                                                   |        |              |
403              | 4003            | Forbidden                                                          |        |              |
404              | 4004            | Not Found                                                          | #144   | error4xxx.py | InvalidAPIUsage
405              | 4005            | Method Not Allowed                                                 |        |              |
406              | 4006            | Not Acceptable                                                     |        |              |
407              | 4007            | Not used                                                           |        |              |
408              | 4008            | Request Time-out                                                   |        |              |
409              | 4009            | Conflict                                                           |        |              |
410              | 4010            | Gone                                                               |        |              |
411              | 4011            | Length Required                                                    |        |              |
412              | 4012            | Precondition Failed                                                |        |              |
413              | 4013            | Request Entity Too Large                                           |        |              |
414              | 4014            | Request-URI Too Large                                              |        |              |
415              | 4015            | Unsupported Media type                                             |        |              |
416              | 4016            | Requested range not satisfiable                                    |        |              |
417              | 4017            | Expectation Failed                                                 |        |              |
500              | 5000            | All exceptions if no specific exceptions are registered            | #166   | error5xxx.py | UnhandledException
501              | 5001            | Not Implemented                                                    | #142   | error5xxx.py | CodeNotImplemented




#### 41xx - Input validation exceptions


HTTP Status Code | API Status Code | Reason Phrase                                                      | Ticket | File         | Name
-----------------|-----------------|--------------------------------------------------------------------|--------|--------------|------
400              |4100             | Input validation Error                                             |#171    | error4xxx.py | InputValidationError
400              |4101             | Missing mandatory parameters                                       | #216   | error4xxx.py |
400              |4102             | Can not be empty                                                   |        |              |
400              |4103             | Too short                                                          |        |              |
400              |4104             | Too long                                                           |        |              |
400              |4105             | Too small                                                          |        |              |
400              |4106             | Too big                                                            |        |              |
                 |                 |                                                                    |        |              |
400              |4110             | Invalid data type for Value                                        | #208   | error4xxx.py | InvalidDataFormat
400              |4111             | Value must be string                                               |        |              |
400              |4112             | Value must be integer                                              |        |              |
400              |4113             | Value must be real number                                          |        |              |
400              |4114             | Value must be one of ('Yes','No', ... )                            |        |              |
400              |4115             | value must be a Unicode string                                     |        |              |
                 |                 |                                                                    |        |              |
400              |4120             | Value is not in expected format                                    |        |              |
400              |4121             | Value contains invalid characters                                  |        |              |
400              |4122             | Invalid credit card number                                         |        |              |
400              |4123             | Invalid phone/fax number                                           |        |              |
400              |4124             | Invalid zip code                                                   |        |              |
                 |                 |                                                                    |        |              |
400              |4130             | For future use                                                     |        |              |
400              |4131             | Invalid email address                                              |        |              |
400              |4132             | Invalid a URL                                                      |        |              |
400              |4133             | Invalid domain name                                                |        |              |
400              |4134             | Invalid IP address                                                 |        |              |
                 |                 |                                                                    |        |              |
400              |4140             | Insecure password                                                  |        |              |
400              |4141             | Invalid username/password                                          |        |              |
                 |                 |                                                                    |        |              |
400              |4190             | For future use                                                     |        |              |
400              |4191             | Value already exists (in the database)                             |        |              |
                 |                 |                                                                    |        |              |
400              |4195             | Mixing of input methods (We can put/post to a URI with parameters) |        |              |
400              |4196             | Invalid content headers (Content type doesn\'t match with data)    | #207   | error4xxx.py | InvalidContentHeader
400              |4197             | Mixing of input data type. For example Content type is JSON and found both JSON and non-JSON data )    | #209   | error4xxx.py | MixedRequestContentType



#### 42xx - Database errors/exceptions

HTTP Status Code | API Status Code | Reason Phrase                                                      | Ticket | File         | Name
-----------------|-----------------|--------------------------------------------------------------------|--------|--------------|------
404              | 4204            | Record not Found                                                   | #176   | error4xxx.py | DatabaseRecordNotFound


#### 43xx - OAuth Exceptions/Errors

HTTP Status Code | API Status Code | Reason Phrase                                                      | Ticket | File         | Name
-----------------|-----------------|--------------------------------------------------------------------|--------|--------------|------
400              | 4300            | Authentication error                                               | #212   | error4xxx.py |
400              | 4301            | Expired Timestamp                                                  | #213   | error4xxx.py |
400              | 4302            | Unexpected oauth_signature_method                                  | #214   | error4xxx.py |
400              | 4303            | Invalid Signature                                                  | #215   | error4xxx.py |


#### 52xx - Database errors/exceptions

HTTP Status Code | API Status Code | Reason Phrase                                                      | Ticket | File         | Name
-----------------|-----------------|--------------------------------------------------------------------|--------|--------------|------
500              | 5200            | Database Exceptions                                                |        |              |
500              | 5201            | Unique key violations                                              |        |              |
500              | 5202            | Referential integrity errors                                       |        |              |
