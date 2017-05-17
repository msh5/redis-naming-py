"""The main script of redis-naming-py."""

DELIMITER = ':'


class TooManyFieldsError(Exception):
    """The error should be raised when the field values are too many."""

    pass


class TooLessFieldsError(Exception):
    """The error should be raised when the field values are too less."""

    pass


class UnexpectedFieldError(Exception):
    """The error should be raised when the unexpected field value exists."""

    pass


class RedisNaming(object):
    """Manage the field settings of key and value."""

    def __init__(self, key_field=None, key_fields=None, value_field=None,
                 value_fields=None):
        """Set the field settings of key and value."""
        # TODO: validate the parameter values

        self.key_fields = key_fields
        if self.key_fields is None:
            self.key_fields = [] if key_field is None else [key_field]
        self.value_fields = value_fields
        if self.value_fields is None:
            self.value_fields = [] if value_field is None else [value_field]

    def build_key(self, **kwargs):
        """Build the key name."""
        # TODO: validate the parameter values
        # TODO: support args param

        key = ''
        for key_field in self.key_fields:
            if key != '':
                key += DELIMITER
            key += key_field
            key += DELIMITER
            key += kwargs[key_field]
        if len(self.value_fields) == 1:
            key += DELIMITER
            key += self.value_fields[0]
        return key

    def build_value(self, **kwargs):
        """Build the value name."""
        # TODO: validate the parameter values
        # TODO: support args param

        if len(self.value_fields) == 1:
            value_field = self.value_fields[0]
            return kwargs[value_field]
        value = ''
        for value_field in self.value_fields:
            if value != '':
                value += DELIMITER
            value += value_field
            value += DELIMITER
            value += kwargs[value_field]
        return value
