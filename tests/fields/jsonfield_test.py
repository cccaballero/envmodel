import os

from envmodel import JsonField


class JsonFieldTest:
    def test_valid_json_is_correctly_parsed(self, mocker):
        # Arrange
        test_json = '{"key": "value", "number": 42}'
        expected_dict = {"key": "value", "number": 42}
        mocker.patch.dict(os.environ, {"TEST_JSON": test_json})

        # Act
        json_field = JsonField(name="TEST_JSON")
        result = json_field.get_env_variable()

        # Assert
        assert result == expected_dict
        assert json_field._config_value == expected_dict

    def test_invalid_json_falls_back_to_default(self, mocker):
        # Arrange
        invalid_json = "{invalid json}"
        default_value = {"default": "value"}
        mocker.patch.dict(os.environ, {"TEST_JSON": invalid_json})
        mock_logger = mocker.patch("logging.exception")

        # Act
        json_field = JsonField(name="TEST_JSON", default=default_value)
        result = json_field.get_env_variable()

        # Assert
        assert result == default_value
        assert json_field._config_value == default_value
        mock_logger.assert_called_once()

    def test_exception_handling_logs_and_returns_default(self, mocker):
        # Arrange
        default_value = {"default": "config"}
        warning_message = "JSON parsing failed, using default"
        mocker.patch.dict(os.environ, {"TEST_JSON": "{invalid}"})
        mock_exception_logger = mocker.patch("logging.exception")
        mock_warning_logger = mocker.patch("logging.warning")

        # Act
        json_field = JsonField(name="TEST_JSON", default=default_value, warning=warning_message)
        result = json_field.get_env_variable()

        # Assert
        assert result == default_value
        assert json_field._config_value == default_value
        mock_exception_logger.assert_called_once()
        mock_warning_logger.assert_called_once_with(warning_message)
