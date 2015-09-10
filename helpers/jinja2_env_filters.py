from dateutil import parser

def datetimeformat(value, format='%m-%d-%Y'):
    """
    Format datetime into m-d-Y if format not specified
    """
    if value:
        return parser.parse(value).strftime(format)
    return ""
