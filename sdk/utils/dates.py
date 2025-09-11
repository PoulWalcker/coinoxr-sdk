from datetime import datetime


def ensure_date(date_str: str, format_str: str = "%Y-%m-%d") -> bool:
    """
    Check if a date string matches the given format.
    Default format is YYYY-MM-DD.
    """
    try:
        datetime.strptime(date_str, format_str)
        return True
    except ValueError:
        return False
