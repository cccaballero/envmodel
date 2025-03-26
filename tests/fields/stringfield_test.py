import pytest

from envmodel import StringField


class StringFieldTest:
    def test_inherits_basefield_functionality(self, mocker):
        # Mock os.getenv to return a specific value
        mocker.patch("os.getenv", return_value="test_value")

        # Create a StringField instance with the same parameters as BaseField
        string_field = StringField(
            name="TEST_VAR",
            required=True,
            default="default_value",
            error="Custom error message",
            lazy=True,
            warning="Custom warning message",
        )

        # Verify that StringField behaves like BaseField
        assert string_field.name == "TEST_VAR"
        assert string_field.required is True
        assert string_field.default == "default_value"
        assert string_field.error == "Custom error message"
        assert string_field.lazy is True
        assert string_field.warning == "Custom warning message"

        # Verify that the get_env_variable method works as expected
        assert string_field.get_env_variable() == "test_value"

        # Verify that the __call__ method works as expected
        assert string_field() == "test_value"

    def test_empty_string_env_variable(self, mocker):
        # Mock os.getenv to return an empty string
        mocker.patch("os.getenv", return_value="")

        # Create a StringField instance
        string_field = StringField(name="TEST_VAR")

        # Verify that an empty string is returned as is
        assert string_field.get_env_variable() == ""
        assert string_field() == ""

        # Test with required=True
        required_field = StringField(name="TEST_VAR", required=True)
        # Empty string should not trigger the required check (it's not None)
        assert required_field() == ""

    def test_none_env_variable(self, mocker):
        # Mock os.getenv to return None
        mocker.patch("os.getenv", return_value=None)

        # Create a StringField instance with default=None
        string_field = StringField(name="TEST_VAR", default=None)

        # Verify that None is returned
        assert string_field.get_env_variable() is None
        assert string_field() is None

        # Test with required=True
        required_field = StringField(name="TEST_VAR", required=True)

        # Should raise an exception when required=True and value is None
        with pytest.raises(Exception) as excinfo:
            required_field()
        assert "Environment variable TEST_VAR is required" in str(excinfo.value)

        # Test with warning message
        warning_field = StringField(name="TEST_VAR", warning="Warning: TEST_VAR is not set")
        mock_logger = mocker.patch("logging.warning")
        warning_field()
        mock_logger.assert_called_once_with("Warning: TEST_VAR is not set")
