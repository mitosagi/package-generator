import json
import os
import yaml
from util.text_io import read_text, write_text

files_and_folders = yaml.safe_load(read_text('workspace/metadata.yaml'))
sha368 = json.loads(read_text('workspace/sha368.json'))
package = json.loads(read_text('workspace/gpt4_output.json'))
release_files = []
package['releases'] = [
    {'version': package['latestVersion'],
     'integrity': {
        'archive': sha368['archive'],
        'file': release_files
    }}]


for i in range(len(package['files'])):
    file = package['files'][i]
    is_folder = 'isDirectory' in file and file['isDirectory']
    raw_filename = [match for match in files_and_folders['folders' if is_folder else 'files']
                    if os.path.basename(match) == os.path.basename(file['filename'])]
    if not raw_filename:
        file['error'] = '存在しないエントリが指定されています。'
        continue
    if not is_folder:
        release_files.append({
            'target': file['filename'],
            'hash': [hashdict['hash'] for hashdict in sha368['files'] if hashdict['rawfilename'] == raw_filename[0]][0]})
    if os.path.dirname(raw_filename[0]) != '':
        file['archivePath'] = os.path.dirname(raw_filename[0]) + '/'

write_text(f"output/{package['id'].replace('/', '_')}.json", package)
