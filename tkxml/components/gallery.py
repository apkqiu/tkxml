from .BaseComponent import BaseComponent
COMPONENTS = {}
def register(tag_name):
    def decorator(obj):
        COMPONENTS[tag_name] = obj
        return obj
    return decorator

def get_factory(tag_name) -> type[BaseComponent]:
    if tag_name in COMPONENTS:
        return COMPONENTS[tag_name]
    else:
        print(f"Component {tag_name} not found")
        return BaseComponent