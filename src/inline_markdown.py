import re

from textnode import TextNode, TextType



def split_nodes_delimiter(old_nodes, delimiter, text_type):
    node_list = []
    # dict_text_type= {"**": TextType.BOLD, "_": TextType.ITALIC, "`": TextType.CODE}
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_list.append(node)
            continue
        
        split_parts = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown format, fromatted parts not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2==0:
                split_parts.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_parts.append(TextNode(sections[i], text_type))
        node_list.extend(split_parts)
    return node_list
        # else:
        #     count_delim = node.text.count(delimiter)
        #     if node.text.count(delimiter) != 2:
        #         raise Exception("No ending delimiter found / Invalid Markdown")
        #     splitted = node.text.split(delimiter)

        #     if node.text.startswith(delimiter):
        #         node_list.append(TextNode(splitted[0], dict_text_type[delimiter]))
        #         node_list.append(TextNode(splitted[1], TextType.TEXT))
        #     elif  node.text.endswith(delimiter):
        #         node_list.append(TextNode(splitted[0], TextType.TEXT))
        #         node_list.append(TextNode(splitted[1], dict_text_type[delimiter]))
        #     else:
        #         node_list.append(TextNode(splitted[0], TextType.TEXT))
        #         node_list.append(TextNode(splitted[1], dict_text_type[delimiter]))
        #         node_list.append(TextNode(splitted[2], TextType.TEXT))
            
    
def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches
    # matches = re.findall(r"!\[.*?\)", text)
    # return_list = []
    # for match in matches:
    #     alt_text = re.findall(r"\[(.*)\]", match)
    #     url = re.findall(r"\((.*?)\)", match)
    #     return_list.append((alt_text[0], url[0]))
    # return return_list

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches
    # matches = re.findall(r"\[.*?\)", text)
    # return_list = []
    # for match in matches:
    #     alt_text = re.findall(r"\[(.*)\]", match)
    #     url = re.findall(r"\((.*?)\)", match)
    #     return_list.append((alt_text[0], url[0]))
    # return return_list

def split_nodes_image(old_nodes):
    node_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_list.append(node)
            continue
        node_text = node.text
        tuples_in_node = extract_markdown_images(node.text)
        if len(tuples_in_node)==0:
            node_list.append(node)
            continue
        for tup in tuples_in_node:
            node_text = node_text.split(f"![{tup[0]}]({tup[1]})", maxsplit=1)
            if len(node_text) !=2:
                raise ValueError("Invalid markdown, no enclosing image delim")
            if node_text[0] != "":
                node_list.append(TextNode(node_text[0], TextType.TEXT))
            node_list.append(TextNode(tup[0], TextType.IMAGE, tup[1]))
            
            node_text = node_text[1]
        if node_text != "":
            node_list.append(TextNode(node_text, TextType.TEXT))    
    return node_list

def split_nodes_link(old_nodes):
    node_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_list.append(node)
            continue
        node_text = node.text
        tuples_in_node = extract_markdown_links(node.text)
        if len(tuples_in_node)==0:
            node_list.append(node)
            continue
        for tup in tuples_in_node:
            node_text = node_text.split(f"[{tup[0]}]({tup[1]})", maxsplit=1)
            if len(node_text) !=2:
                raise ValueError("Invalid markdown, no enclosing link delim")
            if node_text[0] != "":
                node_list.append(TextNode(node_text[0], TextType.TEXT))
            node_list.append(TextNode(tup[0], TextType.LINK, tup[1]))
            
            node_text = node_text[1]
        if node_text != "":
            node_list.append(TextNode(node_text, TextType.TEXT))    
    return node_list

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_image(nodes)
    return nodes




