import tkinter as tk
from .Widget import TkWidgetNode
from ..gallery import register
def make(name, cls):
    @register("{tkinter}"+name)
    class TkNode(TkWidgetNode):
        def create(self):
            return super().create(cls)
    return TkNode