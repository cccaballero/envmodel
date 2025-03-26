from envmodel import BooleanField


class BooleanFieldTest:
    def test_returns_true_when_env_var_is_true(self, monkeypatch):
        # Arrange
        env_var_name = "TEST_BOOL"
        monkeypatch.setenv(env_var_name, "true")
        boolean_field = BooleanField(env_var_name)

        # Act
        result = boolean_field.get_env_variable()

        # Assert
        assert result is True

    def test_handles_uppercase_values_correctly(self, monkeypatch):
        # Arrange
        env_var_name = "TEST_BOOL_UPPER"
        monkeypatch.setenv(env_var_name, "TRUE")
        boolean_field = BooleanField(env_var_name)

        # Act
        result = boolean_field.get_env_variable()

        # Assert
        assert result is True

    def test_handles_mixed_case_values_correctly(self, monkeypatch):
        # Arrange
        env_var_name = "TEST_BOOL_MIXED"
        monkeypatch.setenv(env_var_name, "True")
        boolean_field = BooleanField(env_var_name)

        # Act
        result = boolean_field.get_env_variable()

        # Assert
        assert result is True
