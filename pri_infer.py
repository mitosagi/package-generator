from util.text_io import read_text, write_text
from util.gpt_token import count_token


def pri_infer(info_prompt, bing=False):
    separater = '-'*16
    first = '\n'.join([
        '以下はjson schemaです。',
        read_text('util/schema.json').strip(),
        separater,
        info_prompt,
        separater,
        '今回インストールするパッケージの圧縮ファイルから読み取ったメタデータです。',
        read_text('workspace/metadata.yaml').strip()])
    second = '\n'.join([
        read_text('pri_infer.txt').strip(),
        'これらの情報からjsonファイルを生成し上記のjson schemaによりエラーを出力して検証を行ってください。エラーのある場合はリトライしてください。その後、完成したjsonファイルのダウンロードリンクを提供してください。Pythonにschemaを入力する際はFalseの先頭を大文字にしてdescription以外の要素は省略せず入力してください。もし、json.dump()を使用する場合は ensure_ascii=Falseを指定してください。'])
    return '\n'.join([first,
                      separater,
                      second]) if not bing else '\n'.join([
                          first,
                          separater,
                          '理解したら"continue"とのみ返事してください。',
                          'BINGBINGBING',
                          second])


if __name__ == '__main__':
    prompt = pri_infer(read_text('workspace/gpt3_output.txt'),)
    write_text('workspace/gpt4_input.txt', prompt)
    print(count_token(prompt))
