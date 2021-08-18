import json


def encoding(json_file):
    json_file = json.dumps(json_file, ensure_ascii=False, 
                indent=4, separators=(",", " :"))
    encoded_file = json_file.encode('utf-32')

    return encoded_file


def decoding(encoded_file):
    decoded_file = encoded_file.decode('utf-32')

    return decoded_file
