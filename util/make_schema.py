import json
import requests

from text_io import write_text


schema_json = requests.get(
    'https://raw.githubusercontent.com/team-apm/apm-schema/main/v3/schema/packages.json').json()
package = schema_json['properties']['packages']['items']
# package['$schema'] = json['$schema']
no_use_attributes = ['conflicts', 'provides', 'directURL',
                     'isContinuous', 'installer', 'installArg', 'nicommons', 'isHidden', 'pageURL', 'downloadURLs', 'releases',
                     'isUninstallOnly', 'isInstallOnly', 'archivePath', 'isObsolete']
package['properties'] = {k: v for k,
                         v in package['properties'].items() if k not in no_use_attributes}
package['required'] = [v for v in package['required']
                       if v not in no_use_attributes]
package['properties']['files']['items']['properties'] = {k: v for k,
                                                         v in package['properties']['files']['items']['properties'].items() if k not in no_use_attributes}
write_text('schema.json', json.dumps(package, separators=(',', ':')))
