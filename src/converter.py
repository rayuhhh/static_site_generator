from textnode import TextNode, TextType
from htmlnode import LeafNode


def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
        raise Exception("no valid text type")
    
    if text_node.text_type in TextType:

        if text_node.text_type == TextType.TEXT:
            return LeafNode(tag=None, value=text_node.text, props=None)
        if text_node.text_type == TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text, props=None)
        if text_node.text_type == TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text, props=None)
        if text_node.text_type == TextType.CODE:
            return LeafNode(tag="code", value=text_node.text, props=None)
        if text_node.text_type == TextType.LINK:
            return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
        if text_node.text_type == TextType.IMAGE:
            return LeafNode(tag="img", value="", props={"src": text_node.url, "alt" : text_node.text})

# class Test_text_to_html(unittest.TestCase):
#     def test_text(self):
#         node = TextNode("This is a text node", TextType.TEXT)
#         html_node = text_node_to_html_node(node)
#         self.assertEqual(html_node.tag, None)
#         self.assertEqual(html_node.value, "This is a text node")

# node = TextNode("This is a text node", TextType.TEXT)

# html_node = text_node_to_html_node(node)

# print(html_node.tag)