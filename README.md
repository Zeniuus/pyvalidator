# PyValidator

A simple framework-independent input validation tool for python applications

## Usage

```
from pyvalidator import validate, field, InvalidInputError

def handle_signup(request):
    body = request.body
    try:
        validate(body, {
            'email': field.Email(),
            'username': field.String(length=32),
            'password': field.String(length=32),
            'age': field.Integer(positive=True),
            'description': field.String(nullable=True),
            ...
        })
    except InvalidInputError as e:
        raise BadRequestError(str(e))
    if not is_valid:
        raise BadRequestError
    ...
```
