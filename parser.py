import tkinter as tk
import xml.etree.ElementTree as XmlTree
import components

def xml2element(element: XmlTree.Element, parent_element=None):
    tag = element.tag
    factory = components.gallery.get_factory(tag)()
    for key, value in element.attrib.items():
        factory.set_value(key.split("."), value)
    factory.set_parent(parent_element)
    if element.text:
        factory.set_innerText(element.text.strip())
    object = factory.create()
    for child in element:
        element = xml2element(child, object)
        factory.add_child(element)
    return object or factory.late_create()
    

def parse_xml(string):
    root = XmlTree.fromstring(string)
    root_object = xml2element(root)
    return root_object

if __name__ == "__main__":
    parse_xml(open("test.xml").read()).mainloop()