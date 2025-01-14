from pprint import pprint

def introspection_info(obj):
    object_type = type(obj)
    object_attributes =  [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith('__')]
    object_methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    object_module = obj.__class__.__module__ if hasattr(obj, '__class__') else 'built-in'
    return {
        'type': object_type,
        'attributes': object_attributes,
        'methods': object_methods,
        'module': object_module,
    }

number_info = introspection_info(42)
pprint(number_info)