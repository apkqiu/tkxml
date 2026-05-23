class BaseComponent:
    def __init__(self):
        self.attributes = {}
        self.children = []
        self.parent = None
        self.text = ""
    def set_value(self, key_path: list[str], value:str):
        current_node = self.attributes
        for key in key_path[:-1]:
            if key not in current_node:
                current_node[key] = {}
            current_node = current_node[key]
        current_node[key_path[-1]] = value
    def add_child(self, child: "BaseComponent"):
        self.children.append(child)
    def set_innerText(self,text):
        self.text = text
    def set_parent(self, parent: "BaseComponent"):
        self.parent = parent
    def late_create(self):
        pass
    def create(self):
        pass