import hashlib
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
    files_and_folders = _get_files_and_folders(
        base_dir, relative_path, depth, max_depth)
    files_and_folders['files'] = ext_filter(files_and_folders['files'])
    files_and_folders['folders'] = folder_filter(files_and_folders['folders'])
    return files_and_folders


def _get_files_and_folders(base_dir, relative_path='', depth=1, max_depth=4):
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
            content = _get_files_and_folders(
                item_path, relative_item_path, depth + 1)
            files.extend(content["files"])
            folders.extend(content["folders"])
        else:
            files.append(relative_item_path)

    return {"files": files, "folders": folders}


def calc_sha384(file_path):
    sha384 = hashlib.sha384()

    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha384.update(chunk)

    return "sha384-" + sha384.hexdigest()
