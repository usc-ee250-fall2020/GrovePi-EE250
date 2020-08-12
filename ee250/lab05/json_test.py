import json

# json library: https://docs.python.org/3.5/library/json.html

person = {
    'name': 'Tommy Trojan',
    'email': 'tommy@usc.edu',
    'phone': '213-740-2311',
    'nicknames': [
        'Tommy T',
        'Spirit of Troy',
    ],
}

print(type(person))
print(person)

person_json = json.dumps(person)
print(person_json)

# TODO: What type is person_json?

# TODO: Pretty printing
