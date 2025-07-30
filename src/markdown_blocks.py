from blocktype import BlockType
from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import TextNode, TextType
from converter import text_node_to_html_node
from blocktype import block_to_block_type

def markdown_to_blocks(markdown): # Markdown string representing full document
    block_list = []
    sections = markdown.split("\n\n")
    for sect in sections:
        if sect == "":
            continue
        block_list.append(sect.strip())
    return block_list

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)

def block_to_html_node(block):
    block_type = block_to_block_type(block)

    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html(block)

    if block_type == BlockType.HEADING:
        return heading_to_html(block)
    
    if block_type == BlockType.CODE:
        return code_to_html(block)
    
    if block_type == BlockType.ORDERED_LIST:
        return ordered_list_to_html(block)
    
    if block_type == BlockType.UNORDERED_LIST:
        return unordered_list_to_html(block)

    if block_type == BlockType.QUOTE:
        return quote_to_html(block)
    
    raise ValueError("Block type is invalid")

def paragraph_to_html(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def text_to_children(text):
    nodes = text_to_textnodes(text)
    children = []
    for node in nodes:
        html_node = text_node_to_html_node(node)
        children.append(html_node)
    return children

def heading_to_html(block):
    level = 0
    for _ in block:
        if _ == '#':
            level += 1
        else:
            break
    if level +1 >= len(block):
        raise ValueError("Invalid levels for heading")
    text = block[level+1:]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def code_to_html(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Doesn't having enclosing code ticks")
    text = block[4:-3]
    raw_text = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(raw_text)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])

def ordered_list_to_html(block):
    list_items = block.split("\n")
    html_items = []
    for item in list_items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def unordered_list_to_html(block):
    list_items = block.split("\n")
    html_items = []
    for item in list_items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def quote_to_html(block):
    lines = block.split("\n")
    new_lines = []
    for l in lines:
        if not l.startswith(">"):
            raise ValueError("doesn't have starting > for quote block")
        new_lines.append(l.lstrip(">").strip())
    all_text = " ".join(new_lines)
    children = text_to_children(all_text)
    return ParentNode("blockquote", children)
    
