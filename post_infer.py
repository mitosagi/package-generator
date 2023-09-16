import json
import os
import yaml
from util.text_io import read_text, write_text
from util.get_files import calc_sha384

archivepath = 'data/Aviutl_NVEnc_7.31.zip'
folderpath = 'data/Aviutl_NVEnc_7.31'
files_and_folders = yaml.safe_load(read_text('workspace/metadata.yaml'))


package = json.loads(read_text('workspace/gpt4_output.json'))
release_files = []
package['releases'] = [
    {'version': package['latestVersion'],
     'integrity': {
        'archive': calc_sha384(archivepath),
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
            'hash': calc_sha384(os.path.join(folderpath, raw_filename[0]))})
    if os.path.dirname(raw_filename[0]) != '':
        file['archivePath'] = os.path.dirname(raw_filename[0]) + '/'

write_text('workspace/new_package.json', package)
