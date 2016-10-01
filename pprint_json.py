# -*- coding: utf-8 -*-
import json

def load_data(filepath):
    json_string = open(filepath, 'r', encoding="utf8").readline()
    return json.loads(json_string)

def pretty_print_json(data):
    print (json.dumps(data, indent=4, sort_keys=True))

if __name__=="__main__":
    data = load_data('Магазины «Алкогольные напитки».json')
    pretty_print_json(data)
