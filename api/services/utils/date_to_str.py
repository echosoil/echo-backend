def date_to_str(dt):
    """
    Convert a datetime object to a string.
    
    Parameters
    ----------
    dt : datetime
        The datetime object to convert.
    """
    return dt.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
