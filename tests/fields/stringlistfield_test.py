import os

from envmodel import StringListField


class StringListFieldTest:
    def test_returns_list_from_comma_separated_env_var(self, mocker):
        # Arrange
        mocker.patch.dict(os.environ, {"TEST_LIST": "item1,item2,item3"})
        field = StringListField(name="TEST_LIST")

        # Act
        result = field.get_env_variable()

        # Assert
        assert result == ["item1", "item2", "item3"]

    def test_handles_empty_string_env_var(self, mocker):
        # Arrange
        mocker.patch.dict(os.environ, {"TEST_LIST": ""})
        field = StringListField(name="TEST_LIST")

        # Act
        result = field.get_env_variable()

        # Assert
        assert result == []

    def test_handles_whitespace_only_env_var(self, mocker):
        # Arrange
        mocker.patch.dict(os.environ, {"TEST_LIST": "  ,  ,  "})
        field = StringListField(name="TEST_LIST")

        # Act
        result = field.get_env_variable()

        # Assert
        assert result == []
