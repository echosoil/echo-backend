def data_entity(item):
    """
    Serialize data entity.

    Parameters
    ----------
    item : dict
        Data entity.

    Returns
    -------
    dict
        Serialized data entity.
    """
    return {
        "id": str(item['_id']),
        "name": str(item['name']),
        "age": int(item['age']) if item.get('age') is not None else 0,
        "description": str(item['description']),
        "files": item.get('files', []),
        "created": str(item['created']),
        "modified": str(item['modified'])
    }


def data_collection(data):
    """
    Serialize data collection.

    Parameters
    ----------
    data : list
        Data collection.

    Returns
    -------
    list
        Serialized data collection.
    """
    return [data_entity(item) for item in data]