import json
import os
import yaml
from util.text_io import read_text, write_text


def post_infer(json_prompt):
    metadata = yaml.safe_load(read_text(
        'workspace/metadata.yaml')) | json.loads(read_text('workspace/hidden_metadata.json'))
    package = json.loads(json_prompt)
    release_files = []
    package['pageURL'] = metadata['pageURL'][0]
    package['downloadURLs'] = ['']
    package['releases'] = [
        {'version': package['latestVersion'],
         'integrity': {
            'archive': metadata['archive_hash'],
            'file': release_files
        }}]

    for i in range(len(package['files'])):
        file = package['files'][i]
        is_folder = 'isDirectory' in file and file['isDirectory']
        raw_filename = [match for match in metadata['folders' if is_folder else 'files']
                        if os.path.basename(match) == os.path.basename(file['filename'])]
        if not raw_filename:
            file['error'] = '存在しないエントリが指定されています。'
            continue
        if len([entry for entry in package['files']
                if not file['filename'] == entry['filename'] and file['filename'].startswith(entry['filename'] + '/')]) > 0:
            file['remove'] = True
            continue
        if not is_folder:
            release_files.append({
                'target': file['filename'],
                'hash': [hashdict['hash'] for hashdict in metadata['files_hash'] if hashdict['rawfilename'] == raw_filename[0]][0]})
        if os.path.dirname(raw_filename[0]) != '':
            file['archivePath'] = os.path.dirname(raw_filename[0]) + '/'
    package['files'] = [
        file for file in package['files'] if not 'remove' in file]

    write_text(f"output/{package['id'].replace('/', '_')}.json", package)
    return package


if __name__ == '__main__':
    post_infer(read_text('workspace/gpt4_output.json'))
