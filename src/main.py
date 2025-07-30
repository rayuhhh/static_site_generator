from textnode import TextNode
import sys
import os
import shutil
import logging
from copydirtodir import copy_dir_contents_clean
from markdown_blocks import markdown_to_html_node
from htmlnode import HTMLNode, LeafNode
from pathlib import Path


logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        if line.strip().startswith('# ') and not line.strip().startswith("##"):
            return line.strip()[2:].strip()
    raise Exception("No header present")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from: {from_path} to {dest_path} using {template_path}")
    file_dict = {}

    with open(from_path, 'r')as f:
        file_dict[from_path] = f.read()

    with open(template_path, 'r') as f:
        file_dict[template_path] = f.read()

    new_html_node = markdown_to_html_node(file_dict[from_path])
    html_string = new_html_node.to_html()
    title = extract_title(file_dict[from_path])

    file_dict[template_path] = file_dict[template_path].replace("{{ Title }}", title)
    file_dict[template_path] = file_dict[template_path].replace("{{ Content }}", html_string)
    file_dict[template_path] = file_dict[template_path].replace('href="/', f'href="{basepath}')
    file_dict[template_path] = file_dict[template_path].replace('src="/', f'src="{basepath}')

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(file_dict[template_path])
    # with open(dest_path, "w") as f:
    #     f.write(file_dict[template_path])
    

def generate_page_recursive(dir_path_content, template_path, dest_dir_path, basepath):

    list_dir = os.listdir(dir_path_content)

    for item in list_dir:
        from_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path, basepath)
        else:
            generate_page_recursive(from_path, template_path, dest_path, basepath)



        
def main():
    basepath = "/"
    if len(sys.argv) == 2:
        basepath = sys.argv[1]
    template = "/home/rayn/workspace/github.com/rayuhhh/static_site_generator/template.html"
    source = "/home/rayn/workspace/github.com/rayuhhh/static_site_generator/static"
    destination = "/home/rayn/workspace/github.com/rayuhhh/static_site_generator/docs"
    dest = "/home/rayn/workspace/github.com/rayuhhh/static_site_generator/public/index.html"
    content = "/home/rayn/workspace/github.com/rayuhhh/static_site_generator/content"
    
    # logging.info(f"hello")
    copy_dir_contents_clean(source, destination)

    #### changing generate_page to gen_page_recursive
    #generate_page(content, template, dest)
    generate_page_recursive(content, template, destination, basepath)

    # print("\n--- Verification ---")
    # print(f"Contents of 'public_test': {os.listdir('../public_test')}")
    # print(f"Contents of 'public_test/img': {os.listdir('../public_test/img')}")
    # print(f"Contents of 'public_test/sub': {os.listdir('../public_test/sub')}")
    # print(f"Contents of 'public_test/sub/nested_sub': {os.listdir('../public_test/sub/nested_sub')}")



if __name__ == "__main__":
    main()
    # Create dummy source and destination directories for testing
    # if os.path.exists("../static_test"):
    #     shutil.rmtree("../static_test") # Ensure a fresh start for the test source.
    # os.makedirs("../static_test/img")
    # os.makedirs("../static_test/sub")
    # os.makedirs("../static_test/sub/nested_sub")
    # os.makedirs("../static_test/css")
    # with open("../static_test/index.html", "w") as f:
    #     f.write("<html><body><h1>Hello from static!</h1></body></html>")
    # with open("../static_test/css/style.css", "w") as f:
    #     f.write("body { background-color: lightblue; }")
    # with open("../static_test/img/logo.png", "w") as f:
    #     f.write("This is a dummy image file content.")
    # with open("../static_test/sub/test.txt", "w") as f:
    #     f.write("A file in a subdirectory.")
    # with open("../static_test/sub/nested_sub/deep.txt", "w") as f:
    #     f.write("A file in a deeply nested subdirectory.")

    # Create an initial 'public_test' to see it get deleted
    # if not os.path.exists("../public_test"):
    #     os.makedirs("../public_test/old_files")
    #     with open("../public_test/old_files/old.txt", "w") as f:
    #         f.write("This file should be deleted.")
    
    # copy_directory_contents_clean("static_test", "public_test")

    # print("\n--- Verification ---")
    # print(f"Contents of 'public_test': {os.listdir('public_test')}")
    # print(f"Contents of 'public_test/img': {os.listdir('public_test/img')}")
    # print(f"Contents of 'public_test/sub': {os.listdir('public_test/sub')}")
    # print(f"Contents of 'public_test/sub/nested_sub': {os.listdir('public_test/sub/nested_sub')}")