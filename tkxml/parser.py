import tkinter as tk
import xml.etree.ElementTree as XmlTree
from . import components

def xml2element(element: XmlTree.Element,expose_dict, parent_element=None):
    tag = element.tag
    factory = components.gallery.get_factory(tag)()
    expose_name = element.attrib.pop("{extensions}expose", None)
    for key, value in element.attrib.items():
        factory.set_value(key.split("."), value)
    factory.set_parent(parent_element)
    if element.text:
        factory.set_innerText(element.text.strip())
    object = factory.create()
    for child in element:
        element = xml2element(child, expose_dict, object)
        factory.add_child(element)
    object = object or factory.late_create()
    if expose_name:
        expose_dict[expose_name] = object
    return object

def parse_xml(string):
    expose_dict = {}
    root = XmlTree.fromstring(string)
    root_object = xml2element(root,expose_dict)
    return root_object, expose_dict

def parse_xml_file(file):
    return parse_xml(open(file,encoding="utf-8").read())
