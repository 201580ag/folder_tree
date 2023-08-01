import os

def create_tree(folder_path, txt_file_path):
    with open(txt_file_path, 'w', encoding='utf-8') as file:
        file.write(folder_path + '\n')
        write_tree(folder_path, '', file)

def write_tree(folder_path, indent, file):
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            file.write(indent + '|-- ' + item + '\n')
            write_tree(item_path, indent + '    ', file)
        else:
            file.write(indent + '|-- ' + item + '\n')

folder_path = input(r"Enter image file path: ")
txt_file_path = './output.txt'

create_tree(folder_path, txt_file_path)