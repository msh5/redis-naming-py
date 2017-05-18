"""Test the naming funcition of redis-naming-py."""

from redisnaming import RedisNamer
from redisnaming import TooManyFieldsError
from redisnaming import TooLessFieldsError
from redisnaming import UnexpectedFieldError

NAMER_0 = RedisNamer(key_field='user', value_field='locale')
NAMER_1 = RedisNamer(key_fields=('user', 'domain'),
                     value_fields=('locale', 'timezone'))


def test_keynaming():
    """Include key field name and value field name in key."""
    EXPECTED = 'user:smith:locale'
    assert NAMER_0.name_key('smith') == EXPECTED
    assert NAMER_0.name_key(user='smith') == EXPECTED


def test_valuenaming():
    """Do not include value field name in value."""
    EXPECTED = 'en-US'
    assert NAMER_0.name_value('en-US') == EXPECTED
    assert NAMER_0.name_value(locale='en-US') == EXPECTED


def test_multifieldkeynaming():
    """Include multiple key field names in key."""
    EXPECTED = 'user:smith:domain:tech0522.tk'
    assert NAMER_1.name_key('smith', 'tech0522.tk') == EXPECTED
    assert NAMER_1.name_key(user='smith', domain='tech0522.tk') == EXPECTED


def test_multifieldvaluenaming():
    """Include multiple value field names in value."""
    EXPECTED = 'locale:en-US:timezone:America/New_York'
    assert NAMER_1.name_value('en-US', 'America/New_York') == EXPECTED
    assert NAMER_1.name_value(
        locale='en-US', timezone='America/New_York') == EXPECTED


def test_toomanykeyfields():
    """Validate that the specified key field values is too many."""
    try:
        NAMER_1.name_key('smith', 'tech0522.tk', 'foo')
    except TooManyFieldsError:
        assert True
    except:
        assert False
    else:
        assert False


def test_toolesskeyfields():
    """Validate that the specified key field values is too less."""
    try:
        NAMER_1.name_key('smith')
    except TooLessFieldsError:
        assert True
    except:
        assert False
    else:
        assert False


def test_toomanyvaluefields():
    """Validate that the specified value field values is too many."""
    try:
        NAMER_1.name_value('en-US', 'America/New_York', 'foo')
    except TooManyFieldsError:
        assert True
    except:
        assert False
    else:
        assert False


def test_toolessvaluefields():
    """Validate that the specified value field values is too less."""
    try:
        NAMER_1.name_value('en-US')
    except TooLessFieldsError:
        assert True
    except:
        assert False
    else:
        assert False


def test_unexpectedkeyfield():
    """Validate that all specified key fields exist."""
    try:
        NAMER_0.name_key(user='smith', foo='bar')
    except UnexpectedFieldError, error:
        assert error.unexpected_field == 'foo'
    except:
        assert False
    else:
        assert False


def test_unexpectedvaluefield():
    """Validate that all specified value fields exist."""
    try:
        NAMER_0.name_value(locale='en-US', foo='bar')
    except UnexpectedFieldError, error:
        assert error.unexpected_field == 'foo'
    except:
        assert False
    else:
        assert False
