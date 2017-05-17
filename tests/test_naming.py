"""Test the naming funcition of redis-naming-py."""

from redisnaming import RedisNamer

NAMER_0 = RedisNamer(key_field='user', value_field='locale')
NAMER_1 = RedisNamer(key_fields=('user', 'domain'),
                     value_fields=('locale', 'timezone'))


def test_keynaming():
    """Include key field name and value field name in key."""
    assert NAMER_0.name_key(user='smith') == 'user:smith:locale'


def test_valuenaming():
    """Do not include value field name in value."""
    assert NAMER_0.name_value(locale='en-US') == 'en-US'


def test_multifieldkeynaming():
    """Include multiple key field names in key."""
    key = NAMER_1.name_key(user='smith', domain='tech0522.tk')
    assert key == 'user:smith:domain:tech0522.tk'


def test_multifieldvaluenaming():
    """Include multiple value field names in value."""
    value = NAMER_1.name_value(locale='en-US', timezone='America/New_York')
    assert value == 'locale:en-US:timezone:America/New_York'
