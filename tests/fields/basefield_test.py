import pytest

from envmodel import BaseField


class BaseFieldTest:
    def test_non_required_field_returns_default_value(self, monkeypatch):
        # Arrange
        default_value = "default_value"
        field = BaseField(name="TEST_VAR", default=default_value)

        # Ensure the environment variable is not set
        monkeypatch.delenv("TEST_VAR", raising=False)

        # Act
        result = field()

        # Assert
        assert result == default_value

    def test_required_field_raises_exception_with_custom_error(self, monkeypatch):
        # Arrange
        import pytest

        custom_error = "This is a custom error message"
        field = BaseField(name="TEST_VAR", required=True, error=custom_error)

        # Ensure the environment variable is not set
        monkeypatch.delenv("TEST_VAR", raising=False)

        # Act & Assert
        with pytest.raises(Exception) as excinfo:
            field()

        assert str(excinfo.value) == custom_error

    def test_required_field_raises_exception_with_default_error(self, monkeypatch):
        # Arrange
        import pytest

        var_name = "TEST_VAR"
        field = BaseField(name=var_name, required=True)

        # Ensure the environment variable is not set
        monkeypatch.delenv(var_name, raising=False)

        # Act & Assert
        with pytest.raises(Exception) as excinfo:
            field()

        expected_error = f"Environment variable {var_name} is required"
        assert str(excinfo.value) == expected_error

    # add a test for the allowed values
    def test_allowed_values(self, monkeypatch):
        # Arrange
        allowed_values = ["value1", "value2"]
        field = BaseField(name="TEST_VAR", allowed_values=allowed_values)

        # Ensure the environment variable is set to a value not in the allowed values
        monkeypatch.setenv("TEST_VAR", "not_allowed")

        # Act & Assert
        with pytest.raises(Exception) as excinfo:
            field()

        expected_error = f"Environment variable TEST_VAR must be one of {allowed_values}"
        assert str(excinfo.value) == expected_error
