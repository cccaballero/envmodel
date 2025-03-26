Overview
========

EnvModel is a Python library that simplifies the use of environment variables in your projects. It provides a simple 
and intuitive way to define, manage, and access environment variables, making it easier to configure and deploy your 
applications.

## Minimal Example of Usage

Here's a minimal example of how to use EnvModel:

```python
from envmodel import EnvModel, StringField

class MyConfig(EnvModel):
    api_key = StringField(name="API_KEY", required=True)
    database_url = StringField(name="DATABASE_URL", default="sqlite:///example.db")

config = MyConfig()
print(config.api_key)  # prints the value of API_KEY environment variable
print(config.database_url)  # prints the value of DATABASE_URL environment variable or the default value
```

In this example, we define a MyConfig class that inherits from EnvModel. We then define two environment variables, 
`API_KEY` and `DATABASE_URL`, using the StringField class. The `API_KEY` variable is required, while the `DATABASE_URL` 
variable has a default value.

We can then create an instance of the `MyConfig` class and access the environment variables using dot notation.
