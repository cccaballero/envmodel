import pytest

from envmodel import IntegerField


class IntegerFieldTest:
    def test_init_with_name_and_default(self):
        # Arrange
        name = "TEST_INT"
        default = 42

        # Act
        field = IntegerField(name=name, default=default)

        # Assert
        assert field.name == name
        assert field.default == default

    def test_get_env_variable_with_non_integer_value(self, monkeypatch):
        # Arrange
        name = "TEST_INT"
        monkeypatch.setenv(name, "not_an_integer")
        field = IntegerField(name=name)

        # Act & Assert
        with pytest.raises(Exception) as excinfo:
            field.get_env_variable()

        assert f"Environment variable {name} must be an integer" in str(excinfo.value)

    def test_init_with_default_none(self, monkeypatch):
        # Arrange
        name = "TEST_INT"
        field = IntegerField(name=name, default=None)

        # Act & Assert
        # When env var is not set and default is None
        with pytest.raises(Exception):
            field.get_env_variable()

        # When env var is set
        monkeypatch.setenv(name, "123")
        assert field.get_env_variable() == 123
