from redisnaming import RedisNamer

NAMER_0 = RedisNamer(key_field="user", value_field="locale")
NAMER_1 = RedisNamer(key_fields=("user", "domain"), value_fields=("locale", "timezone"))

def test_keybuild():
    """Include key field name and value field name in key"""
    assert NAMER_0.build_key(user="smith") == "user:smith:locale"

def test_valuebuild():
    """Do not include value field name in value"""
    assert NAMER_0.build_value(locale="en-US") == "en-US"

def test_multifieldkeybuild():
    """Include multiple key field names in key"""
    assert NAMER_1.build_key(user="smith", domain="tech0522.tk") == "user:smith:domain:tech0522.tk"

def test_multifieldvaluebuild():
    """Include multiple value field names in value"""
    assert NAMER_1.build_value(locale="en-US", timezone="America/New_York") == "locale:en-US:timezone:America/New_York"

