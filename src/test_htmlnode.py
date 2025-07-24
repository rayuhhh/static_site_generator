import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p", "pp", "ppp", {"p" : "p"})
        self.assertEqual(node.props_to_html(), f' {"p"}="{"p"}"')

    def test_props_to_html2(self):
        node = HTMLNode("p", "pp", "ppp", {"t" : "t"})
        self.assertEqual(node.props_to_html(), f' t="t"')

    def test_props_to_html3(self):
        node = HTMLNode("q", "qq", "qqq", {"q": "qq"})
        self.assertEqual(node.props_to_html(), f' q="qq"')

    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click", {"href": "www.google.com"})
        self.assertEqual(node.to_html(), '<a href="www.google.com">Click</a>')

if __name__ == "__main__":
    unittest.main()