import os

aviutl_related_extensions = {'.abc',
                             '.anm',
                             '.auc',
                             '.auf',
                             '.aui',
                             '.aul',
                             '.auo',
                             '.cam',
                             '.conf',
                             '.dll',
                             '.exa',
                             '.exe',
                             '.exo',
                             '.html',
                             '.ini',
                             '.json',
                             '.log',
                             '.lua',
                             '.manifest',
                             '.obj',
                             '.png',
                             '.scn',
                             '.tra',
                             '.txt',
                             '.xml',
                             '.zip'}

aviutl_related_folders = {'plugins', 'script', 'browser'}


def ext_filter(files):
    return [
        file for file in files
        if os.path.splitext(file)[1] in aviutl_related_extensions
    ]


def folder_filter(folders):
    return [
        folder for folder in folders
        if os.path.basename(folder) not in aviutl_related_folders
    ]


def get_files_and_folders(base_dir, relative_path='', depth=1, max_depth=4):
    files = []
    folders = []

    if depth > max_depth:
        return {"files": files, "folders": folders}

    items = os.listdir(base_dir)
    # If a folder contains more than 8 items, ignore its content
    if len(items) > 8:
        return {"files": files, "folders": folders}

    for item in items:
        item_path = os.path.join(base_dir, item)
        relative_item_path = os.path.join(relative_path, item)

        if os.path.isdir(item_path):
            folders.append(relative_item_path)
            content = get_files_and_folders(
                item_path, relative_item_path, depth + 1)
            files.extend(content["files"])
            folders.extend(content["folders"])
        else:
            files.append(relative_item_path)

    return {"files": files, "folders": folders}
