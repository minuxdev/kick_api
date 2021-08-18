import json
from api.scrap.scraping import returning_json

def json_to_binary(keyword, url):
	out_json = returning_json(url)
	if len(out_json) == 0:
		return out_json
        
	else:
		with open(f"./stored_files/{keyword}.json", "w") as js:
			js.write(json.dumps(out_json, indent = 4, ensure_ascii = False,
				separators=(',', ': ')))

		return out_json


def binary_to_json(file):
	with open(file, "rb") as f:
		binary_file = f.read()

	return binary_file
