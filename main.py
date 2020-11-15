import json

items = json.loads('[{"id":1,"text":"Item 1"}, {"id":2,"text":"Item 2"}, {"id":3,"text":"Item 3"}]')

for item in items:
    print (item['text']) 


def greet(name,greeting):
    """return a greeting

    Args:
        name ([type]): [description]
        greeting ([type]): [description]

    Returns:
        [type]: [description]
    """
    return f'{greeting} {name}'

print (greet("name","hamid"))
print (greet("karim","hiee"))

