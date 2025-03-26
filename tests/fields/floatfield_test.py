import pytest

from envmodel import FloatField


class FloatFieldTest:
    def test_init_with_name_and_default(self):
        # Arrange
        name = "FLOAT_VAR"
        default = 3.14

        # Act
        field = FloatField(name=name, default=default)

        # Assert
        assert field.name == name
        assert field.default == default
        assert field.required is False
        assert field.error == f"Environment variable {name} is required"

    def test_get_env_variable_with_non_float_value(self, monkeypatch):
        # Arrange
        name = "FLOAT_VAR"
        monkeypatch.setenv(name, "not_a_float")
        field = FloatField(name=name)

        # Act & Assert
        with pytest.raises(Exception) as exc_info:
            field.get_env_variable()

        assert str(exc_info.value) == f"Environment variable {name} must be a float"

    def test_get_env_variable_with_none_default(self, monkeypatch):
        # Arrange
        name = "FLOAT_VAR"
        field = FloatField(name=name, default=None)

        # Act & Assert
        # When env var is not set and default is None
        monkeypatch.delenv(name, raising=False)
        with pytest.raises(Exception):
            field.get_env_variable()
