import json
import requests
from text_io import write_text


def remove_keys(d, _remove_keys):
    if isinstance(d, dict):
        d = {k: (remove_keys(v, _remove_keys) if isinstance(v, dict) or isinstance(v, list) else v)
             for k, v in d.items() if k not in _remove_keys}
    elif isinstance(d, list):
        d = [(remove_keys(v, _remove_keys) if isinstance(v, dict) or isinstance(v, list) else v)
             for v in d if v not in _remove_keys]
    return d


schema_json = requests.get(
    'https://raw.githubusercontent.com/team-apm/apm-schema/main/v3/schema/packages.json').json()
package = schema_json['properties']['packages']['items']
no_use_attributes = ['conflicts', 'provides', 'directURL',
                     'isContinuous', 'installer', 'installArg', 'nicommons', 'isHidden', 'pageURL', 'downloadURLs', 'releases',
                     'isUninstallOnly', 'isInstallOnly', 'archivePath', 'isObsolete', 'description']
package = remove_keys(package, no_use_attributes)

write_text('schema.json', json.dumps(package, separators=(',', ':')))
