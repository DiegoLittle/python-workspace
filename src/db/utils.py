import json


def isJsonSerializable(obj):
    """Returns True if the object is JSON serializable."""
    try:
        json.dumps(obj)
        return True
    except TypeError:
        return False


def isJsonDeserializable(obj):
    """Returns True if the object is JSON deserializable."""
    try:
        json.loads(obj)
        return True
    except json.decoder.JSONDecodeError:
        return False


from sqlalchemy import inspect


def object_as_dict(obj):
    return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}


def deserialize_sql_model(sql_model):
    return_dict = {}

    for key, value in object_as_dict(sql_model).items():
        if isJsonDeserializable(value):
            return_dict[key] = json.loads(value)
        else:
            return_dict[key] = value
    return return_dict
