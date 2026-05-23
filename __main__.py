import tkxml

if __name__ == "__main__":
    root, exposed = tkxml.parse_xml(open("test.xml").read())
    exposed["my_label"].configure(text="I Changed!")
    root.mainloop()