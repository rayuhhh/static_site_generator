import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_text(self):
        node = TextNode("This is a text", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_eq_type(self):
        node = TextNode("This", TextType.BOLD)
        node2 = TextNode("This", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This", TextType.BOLD, url="www.google.com")
        node2 = TextNode("This", TextType.BOLD, url=None)
        self.assertNotEqual(node, node2)




if __name__ == "__main__":
    unittest.main()