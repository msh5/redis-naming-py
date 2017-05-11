DELIMITER = ':'


class TooManyFieldsError(Exception):
    pass


class TooLessFieldsError(Exception):
    pass


class UnexpectedFieldError(Exception):
    pass


class RedisNaming(object):
    def __init__(self, key_field=None, key_fields=None, value_field=None,
                 value_fields=None):
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
