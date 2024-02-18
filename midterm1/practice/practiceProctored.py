input = [{'target_id': 0,
          'primary_type': 'text',
          'primary_description': 'I told you not to pick the one from the pilot experiment...'},
         {'target_id': 1,
          'primary_type': 'text',
          'primary_description': 'Well that explains the gas station'},
         {'target_id': 2,
          'primary_type': 'text',
          'primary_description': "The dairy-free vegan soy cheese doesn't seem to be having the same effect..."},
         {'target_id': 3,
          'primary_type': 'text',
          'primary_description': 'Repeatedly, cheese demonstrated characteristics of a performance enhancing drug'}]


def get_captions(captions_json):
    return [x['primary_description'] for x in captions_json]


res = get_captions(input)
print(res)
