def challenge3(key, object):
    print(str(type(key)), str)
    if type(object) != dict:
        raise TypeError("Object must be of dict type")
    if type(key) != str:
        raise TypeError("Key must be of str type")
    subkeys = key.split("/")
    obj = object
    val = None
    for k in subkeys:
        if k not in obj:
            return None
        else:
            val = obj[k]
            obj = val
    return val

## Testing
if _name_ == "_main_":
    object = {"a": {"b" : {"c": "queen"}}}
    key = "a/b/c"
    val = challenge3(key, object)
    print("value", val)
    object = {"x": {"y" : {"z": "king"}}}
    key = "x/y/z"
    val = challenge3(key, object)
    print("value", val)
