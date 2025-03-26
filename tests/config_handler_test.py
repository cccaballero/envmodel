import pytest

from envmodel import EnvModel, IntegerField, StringField


class EnvModelTest:
    def test_eager_loading_loads_all_env_variables(self, mocker):
        # Arrange
        mock_get_env = mocker.patch("os.getenv")
        mock_get_env.return_value = "test_value"

        class TestConfig(EnvModel):
            TEST_VAR1 = StringField("TEST_VAR1")
            TEST_VAR2 = StringField("TEST_VAR2")
            TEST_VAR3 = StringField("TEST_VAR3")

        # Act
        TestConfig(lazy=False)

        # Assert
        assert mock_get_env.call_count == 3
        mock_get_env.assert_any_call("TEST_VAR1", None)
        self.call = mock_get_env.assert_any_call("TEST_VAR2", None)
        mock_get_env.assert_any_call("TEST_VAR3", None)

    def test_required_env_variable_missing(self, mocker):
        # Arrange
        mocker.patch("os.getenv", return_value=None)
        custom_error = "REQUIRED_VAR is mandatory for application to work"

        class TestConfig(EnvModel):
            REQUIRED_VAR = StringField("REQUIRED_VAR", required=True, error=custom_error)

        # Act & Assert
        with pytest.raises(Exception) as exc_info:
            TestConfig(lazy=False)

        assert str(exc_info.value) == custom_error

    def test_invalid_format_for_field_type(self, mocker):
        # Arrange
        def mock_getenv(name, default=None):
            if name == "INT_VAR":
                return "not_an_integer"
            return default

        mocker.patch("os.getenv", side_effect=mock_getenv)

        class TestConfig(EnvModel):
            INT_VAR = IntegerField("INT_VAR")

        # Act & Assert
        with pytest.raises(Exception) as exc_info:
            TestConfig(lazy=False)

        assert "Environment variable INT_VAR must be an integer" in str(exc_info.value)
