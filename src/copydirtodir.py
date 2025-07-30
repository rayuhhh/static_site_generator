import os
import shutil
import logging


def copy_dir_contents_clean(source_dir, dest_dir):
    # delete old
    if os.path.exists(dest_dir):
            logging.info(f"Delete existing destination directory: {dest_dir}")
            shutil.rmtree(dest_dir)
    # create dest_dir again
    os.mkdir(dest_dir)
    logging.info(f"Creating destination directory: {dest_dir}")

    rec_copy_list_dir(source_dir, dest_dir)

def rec_copy_list_dir(source, dest):
    # copying
    list_paths = os.listdir(source)

    for item in list_paths:
        source_item_path = os.path.join(source, item)
        dest_item_path = os.path.join(dest, item)

        if os.path.isfile(source_item_path):
            shutil.copy(source_item_path, dest_item_path)
            logging.info(f"copied file: {source_item_path} to {dest_item_path}")
        elif os.path.isdir(source_item_path):
            os.mkdir(dest_item_path)
            logging.info(f"created directory: {dest_item_path}")
            rec_copy_list_dir(source_item_path, dest_item_path)