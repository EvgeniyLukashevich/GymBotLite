import os


def content_write(user_id: str, content_type: str, content_id: str):
    content_list = [content_type, content_id]
    try:
        os.mkdir(f"database/{user_id}")
        os.mkdir(f"database/{user_id}/default")
        with open(f"database/{user_id}/default/content_1.txt", "w+",
                  encoding='UTF-8') as file:
            print(*content_list, file=file, sep="\n")
    except:
        try:
            os.mkdir(f"database/{user_id}/default")
            with open(f"database/{user_id}/default/content_1.txt", "w+",
                      encoding='UTF-8') as file:
                print(*content_list, file=file, sep="\n")
        except:
            flist: list = []
            with os.scandir(f'database/{user_id}/default') as files:
                for file in files:
                    flist.append(int(str(file).replace("<DirEntry 'content_", '').replace(".txt'>", '')))
            flist.sort()
            new_index = flist[-1] + 1
            with open(f"database/{user_id}/default/content_{new_index}.txt", "w+",
                      encoding='UTF-8') as file:
                print(*content_list, file=file, sep="\n")
