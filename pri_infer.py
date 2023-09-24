from util.text_io import read_text, write_text
from util.gpt_token import count_token


def pri_infer(info_prompt, isAPI=True):
    separater = '-'*16
    return '\n'.join([
        '以下はjson schemaです。',
        read_text('util/schema.json').strip(),
        separater,
        info_prompt,
        separater,
        '今回インストールするパッケージの圧縮ファイルから読み取ったメタデータです。',
        read_text('workspace/metadata.yaml').strip(),
        separater,
        read_text('pri_infer.txt').strip(),
        'ここまでの情報からjson文字列を生成、validate_by_json_schemaにより検証してください。' if isAPI else 'これらの情報からjsonファイルを生成し上記のjson schemaによりエラーを出力して検証を行ってください。エラーのある場合はリトライしてください。その後、完成したjsonファイルのダウンロードリンクを提供してください。もし、json.dump()を使用する場合は ensure_ascii=Falseを指定してください。'])


if __name__ == '__main__':
    prompt = pri_infer(read_text('workspace/gpt3_output.txt'), False)
    write_text('workspace/gpt4_input.txt', prompt)
    print(count_token(prompt))
