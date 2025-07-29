def markdown_to_blocks(markdown): # Markdown string representing full document
    block_list = []
    sections = markdown.split("\n\n")
    for sect in sections:
        if sect == "":
            continue
        block_list.append(sect.strip())
    return block_list