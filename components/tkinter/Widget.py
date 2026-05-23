import tkinter as tk
from ..BaseComponent import BaseComponent
from ..gallery import register
@register("{tkinter}Widget")
class TkWidgetNode(BaseComponent):
    def __init__(self):
        super().__init__()
    def create(self, widget=None):
        element = widget(self.parent) if type(widget) is type else tk.Widget(self.parent, self.attributes.pop("widget", widget))
        for k,v in self.attributes.pop("bind", {}).items():
            element.bind(f"<{k}>", v)
        for k,v in self.attributes.pop("nsbind", {}).items():
            element.bind(f"<<{k}>>", v)
        for k,v in self.attributes.pop("call", {}).items():
            getattr(element,k)()
        for func in dir(element):
            if func.startswith("_"): continue  # tkinter 内部函数
            if func.endswith("_configure"):
                name = func[:-10]
                if name in self.attributes:
                    getattr(element, func)(**self.attributes.pop(name))
            else:
                if func in self.attributes:
                    if type(self.attributes.get(func)) is dict:
                        getattr(element, func)(**self.attributes.pop(func))
                    else:
                        getattr(element, func)(self.attributes.pop(func))
        element.configure(self.attributes)
        if self.text:
            element.configure(text=self.text)
        return element