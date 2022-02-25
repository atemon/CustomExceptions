# Custom Exceptions

For APIs, we may need to have custom exceptions raised from server. To keep exception codes and messages consistant across projects will make development faster and easier.

Here is a sample work which could be used as is or canbe used as a model for defining exceptions.

## Usage
```python

from exceptions.api import InputValidationError

```

### Convert standard exceptions
```python

if (request.method == "PUT" or request.method == "POST" or request.method == "PATCH") and request.content_type == "application/json":
    try:
        request.JSON = json.loads(request.body)
    except ValueError as ve:
        return JsonResponse(InputValidationError(exception=ve))
else:
    request.JSON = {}

```

### Custom Exception

```pythonn
try:
    self.offset = int(request.GET.get("offset", '0'))
except Exception:
    raise InputValidationError(message_dict={"offset": "Offset should be an integer(convertible). Received '{0}'".format(request.GET.get("offset"))})

```

### Serialize to JSON

```python

message = exception.jsonify()

```


### Serialize to dict

```python

message = exception.dict()

```
