from botocore.vendored import requests
import base64

def handler(event, context):

    output = []

    for record in event['records']:
        payload=base64.b64decode(record["data"])
        headers = {'Content-type': 'text/plain'}
        r = requests.post("https://philter-ip:8080/api/filter", verify=False, data=payload, headers=headers, timeout=20)
        filtered = r.text
        output_record = {
            'recordId': record['recordId'],
            'result': 'Ok',
            'data': base64.b64encode(filtered.encode('utf-8') + b'\n').decode('utf-8')
        }
        output.append(output_record)

    return {'records': output}
