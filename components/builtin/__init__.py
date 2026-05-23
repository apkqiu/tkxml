from ..BaseComponent import BaseComponent
from ..gallery import register
@register("{builtin}int")
class IntNode(BaseComponent):
    def create(self):
        return int(self.text)

@register("{builtin}float")
class FloatNode(BaseComponent):
    def create(self):
        return float(self.text)

@register("{builtin}complex")
class ComplexNode(BaseComponent):
    def create(self):
        return complex(self.text)

@register("{builtin}str")
class StrNode(BaseComponent):
    def create(self):
        return str(self.text)

@register("{builtin}bool")
class BoolNode(BaseComponent):
    def create(self):
        return bool(self.text)

@register("{builtin}list")
class ListNode(BaseComponent):
    def late_create(self):
        return list(self.children)

@register("{builtin}tuple")
class TupleNode(BaseComponent):
    def late_create(self):
        return tuple(self.children)

@register("{builtin}dict")
class DictNode(BaseComponent):
    def late_create(self):
        return dict(self.children)
