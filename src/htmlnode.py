

class HTMLNode():

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        ret_str = ""
        for key in self.props.keys():
            ret_str+=f' {key}="{self.props[key]}"'
        return ret_str

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        self.value = value

    def to_html(self):
        if self.value == None:
            raise ValueError("Invalid HTML: no value present")
        
        if self.tag == None:
            return self.value
        
        if self.tag == "a":
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        
        return f"<{self.tag}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("Need a tag")
        if self.children == None:
            raise ValueError("Parent needs children")

        child_html = ""
        for child in self.children:
            child_html += child.to_html()

        return f"<{self.tag}>{child_html}</{self.tag}>"        


        