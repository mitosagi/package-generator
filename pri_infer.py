from util.text_io import read_text, text2yaml, write_text
from util.token import count_token

separater = '-'*16
prompt = '\n'.join([
    read_text('workspace/gpt3_output.txt'),
    separater,
    '今回インストールするパッケージの圧縮ファイルから読み取ったメタデータです。',
    read_text('workspace/metadata.yaml'),
    separater,
    read_text('pri_infer.prompt.txt'),])
write_text('workspace/gpt4_input.txt', prompt)
print(count_token(prompt))
