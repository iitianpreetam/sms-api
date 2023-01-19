import re

def is_email(field, value, error):
    if not re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$", value):
        error(field, 'Not a valid email')