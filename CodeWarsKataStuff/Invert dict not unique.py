
d = {
      'Ice': 'Cream',
      'Age': '21',
      'Light': 'Cream',
      'Double': 'Cream'
    }

inverted_dict = {i.setdefault(d[key], [])}


"""
def invert_to_lists(dct):
    inverted_dict = {}
    for key in dct:
        inverted_dict.setdefault(dct[key], []).append(key)
    return inverted_dict


d = {
      'Ice': 'Cream',
      'Age': '21',
      'Light': 'Cream',
      'Double': 'Cream'
    }
"""
