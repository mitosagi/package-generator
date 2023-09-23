import json
import os
import openai
from post_infer import post_infer
from pri_infer import pri_infer
from pri_summarize import pri_summarize
from currency_converter import CurrencyConverter

from util.api_log import api_log
from util.text_io import read_text, write_text
from util.gpt_token import count_token

openai.api_key = os.getenv("OPENAI_API_KEY")
currencyConverter = CurrencyConverter()


def get_price(model, array: [float, float]):
    price = {'gpt-3.5-turbo': [0.0015/1000, 0.002/1000],
             'gpt-3.5-turbo-16k': [0.003/1000, 0.004/1000],
             'gpt-4': [0.03/1000, 0.06/1000]}
    price_usd = price[model][0]*array[0] + price[model][1]*array[1]
    price_yen = currencyConverter.convert(price_usd, 'USD', 'JPY')
    return '${:.6f} ￥{:.4f}'.format(price_usd, price_yen)


def chat(prompt, function=False, drill=True):
    model = 'gpt-4' if function else ('gpt-3.5-turbo-16k' if count_token(
        prompt) > 3000 else 'gpt-3.5-turbo')

    if drill:
        if function:
            chat_completion = json.loads(
                read_text('util/example_FC_response.json'))
        else:
            chat_completion = json.loads(
                read_text('util/example_response.json'))
    else:
        if function:
            functions = [
                {
                    "name": "validate_by_json_schema",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "json": {
                                "type": "string",
                            },
                        },
                        "required": ["json"],
                    },
                }
            ]
            chat_completion = openai.ChatCompletion.create(
                model=model, messages=[{"role": "user", "content": prompt}], functions=functions)
        else:
            chat_completion = openai.ChatCompletion.create(
                model=model, messages=[{"role": "user", "content": prompt}])
        print(model + ' called!')
        api_log(chat_completion, model)

    token_count = [chat_completion['usage']['prompt_tokens'],
                   chat_completion['usage']['completion_tokens']]
    print(
        f"token (in){token_count[0]} (out){token_count[1]}, {get_price(model, token_count)}")

    return json.loads(chat_completion['choices'][0]['message']['function_call']['arguments'])['json'] if function else chat_completion['choices'][0]['message']['content']


write_text('workspace/gpt3_input.txt', pri_summarize())
write_text('workspace/gpt3_output.txt',
           chat(read_text('workspace/gpt3_input.txt')))
write_text('workspace/gpt4_input.txt',
           pri_infer(read_text('workspace/gpt3_output.txt')))
write_text('workspace/gpt4_output.json',
           chat(read_text('workspace/gpt4_input.txt'), function=True))
post_infer(read_text('workspace/gpt4_output.json'))
