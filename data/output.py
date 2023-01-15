import os


def content_file_read(user_id, content_name):
    component_list = []
    with open(f'database/{user_id}/default/{content_name}.txt', 'r', encoding='UTF-8') as file:
        for line in file.readlines():
            component_list.append(line.strip())
    return component_list


def files_read(user_id):
    files_list: list = []
    with os.scandir(f'database/{user_id}/default/') as files:
        for file in files:
            files_list.append(str(file).replace("<DirEntry '", '').replace(".txt'>", ''))
    for lap in range(len(files_list) - 1):
        for i in range(len(files_list) - 1):
            if int(files_list[i].replace("content_", '')) > int(files_list[i + 1].replace("content_", '')):
                temp = files_list[i + 1]
                files_list[i + 1] = files_list[i]
                files_list[i] = temp
    return files_list
