from datetime import datetime

from util.text_io import write_text


def api_log(response_object, title=''):
    write_text(
        'log/' + datetime.today().strftime("%Y%m%d_%H%M%S") + '_' + title + '.json', response_object)
