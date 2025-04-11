Fields
======

EnvModel provides several field types that can be used to define environment variables. Each field type has its own set of options and behaviors.

### StringField

A string field that can hold any string value.

#### Options

* `name`: The name of the environment variable.
* `required`: Whether the environment variable is required. Defaults to `False`.
* `default`: The default value of the environment variable. Defaults to `None`.
* `allowed_values`: A list of allowed values for the environment variable.
* `error`: The error message to display if the environment variable is not set. Defaults to a generic error message.

#### Example

```python
from envmodel import EnvModel, StringField

class MyConfig(EnvModel): 
    api_key = StringField(name="API_KEY", required=True)
```

### IntegerField

An integer field that can hold any integer value.

#### Options

* `name`: The name of the environment variable.
* `required`: Whether the environment variable is required. Defaults to `False`.
* `default`: The default value of the environment variable. Defaults to `None`.
* `error`: The error message to display if the environment variable is not set. Defaults to a generic error message.
   
#### Example

```python
from envmodel import EnvModel, IntegerField

class MyConfig(EnvModel):
    port = IntegerField(name="PORT", default=8080)
```

### FloatField

A float field that can hold any float value.

#### Options

* `name`: The name of the environment variable.
* `required`: Whether the environment variable is required. Defaults to `False`.
* `default`: The default value of the environment variable. Defaults to `None`.
* `error`: The error message to display if the environment variable is not set. Defaults to a generic error message.

#### Example

```python
from envmodel import EnvModel, FloatField

class MyConfig(EnvModel):
    temperature = FloatField(name="TEMPERATURE", required=False, default=20.0)
```

In this example, `temperature` will default to 20.0 if not set in the environment.

### BooleanField

A boolean field that can hold True or False values.

#### Options

* `name`: The name of the environment variable.
* `required`: Whether the environment variable is required. Defaults to `False`.
* `default`: The default value of the environment variable. Defaults to `False`.
* `error`: The error message to display if the environment variable is not set. Defaults to a generic error message.

#### Example

```python
from envmodel import EnvModel, BooleanField

class MyConfig(EnvModel):
    DEBUG = BooleanField(name="DEBUG", default=True)
```

### JsonField

A JSON field that can hold a JSON value.
  
#### Options
* `name`: The name of the environment variable.
* `required`: Whether the environment variable is required. Defaults to False.
* `default`: The default value of the environment variable. Defaults to `None`.The default value of the environment variable. Defaults to None.
* `error`: The error message to display if the environment variable is not set. Defaults to a generic error message.
  
#### Example

```python
from envmodel import EnvModel, JsonField

class MyConfig(EnvModel): 
    config = JsonField(name="CONFIG", default={"foo": "bar"})
```

### StringListField

A string list field that can hold a list of string values. Each value is separated by a comma.
  
#### Options 

* `name`: The name of the environment variable.
* `required`: Whether the environment variable is required. Defaults to `False`.
* `default`: The default value of the environment variable. Defaults to `None`.
* `error`: The error message to display if the environment variable is not set. Defaults to a generic error message.

#### Example

```python
from envmodel import EnvModel, StringListField

class MyConfig(EnvModel):
    allowed_hosts = StringListField(name="ALLOWED_HOSTS", default=["localhost", "127.0.0.1"])
```
