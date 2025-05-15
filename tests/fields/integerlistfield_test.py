import pytest

from envmodel import IntegerListField


class IntegerListFieldTest:
    def test_get_env_variable_with_valid_list(self, monkeypatch):
        # Set up
        env_var_name = "TEST_INT_LIST"
        env_var_value = "1, 2, 3, 4, 5"
        monkeypatch.setenv(env_var_name, env_var_value)

        # Execute
        field = IntegerListField(name=env_var_name)
        result = field.get_env_variable()

        # Verify
        assert result == [1, 2, 3, 4, 5]

    def test_get_env_variable_with_empty_string(self, monkeypatch):
        # Set up
        env_var_name = "TEST_INT_LIST"
        env_var_value = ""
        monkeypatch.setenv(env_var_name, env_var_value)

        # Execute
        field = IntegerListField(name=env_var_name)
        result = field.get_env_variable()

        # Verify
        assert result == []

    def test_get_env_variable_with_default_value(self, monkeypatch):
        # Set up
        env_var_name = "TEST_INT_LIST"
        default_value = [10, 20, 30]

        # Execute
        field = IntegerListField(name=env_var_name, default=default_value)
        result = field.get_env_variable()

        # Verify
        assert result == default_value

    def test_get_env_variable_with_invalid_integer(self, monkeypatch):
        # Set up
        env_var_name = "TEST_INT_LIST"
        env_var_value = "1, 2, not_an_integer, 4, 5"
        monkeypatch.setenv(env_var_name, env_var_value)

        # Execute and Verify
        field = IntegerListField(name=env_var_name)
        with pytest.raises(Exception) as excinfo:
            field.get_env_variable()
        
        assert "must contain valid integers separated by commas" in str(excinfo.value)

    def test_get_env_variable_with_spaces(self, monkeypatch):
        # Set up
        env_var_name = "TEST_INT_LIST"
        env_var_value = " 1,  2 , 3,4 , 5 "
        monkeypatch.setenv(env_var_name, env_var_value)

        # Execute
        field = IntegerListField(name=env_var_name)
        result = field.get_env_variable()

        # Verify
        assert result == [1, 2, 3, 4, 5]

