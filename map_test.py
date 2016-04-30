import json

def get_json():
	with open('mcc.json', 'r') as f:
    		category_map_file = json.load(f)

	category_map = {}

	for idx, key in enumerate(category_map_file):
		category_map[key["mcc"]] =  key["edited_description"]

	categories = category_map.values()
	
	return category_map,categories


if __name__ == "__main__":
	category_map,categories = get_json()
	categories.extend(['something','something else'])
	print categories
