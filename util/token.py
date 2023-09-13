import tiktoken

encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")


def count_token(text):
    return len(encoding.encode(text))


def trim_token(text, length):
    return encoding.decode(encoding.encode(text)[:length])
