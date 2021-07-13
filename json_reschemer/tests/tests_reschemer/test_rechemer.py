from jsonpath_ng import parse, jsonpath

def sample_json():
    return {
        'foo': [
            {'baz': 1},
            {'baz': 2},
            {'bar': [
                3,
                4,
                5
            ]},
        ]
    }

def test(mappings):

    to_find = list(mappings.keys())[0]
    to_create = list(mappings.values())[0]

    # A robust parser, not just a regex. (Makes powerful extensions possible; see below)
    jsonpath_expr = parse(to_find)

    # Extracting values is easy
    matches = [match.value for match in jsonpath_expr.find(sample_json())]
    print(matches)
    # [1, 2]

    # Create the structure of whats passed in
    create_expr = parse(to_create)
    print(create_expr)




if __name__ == "__main__":
    mappings = {'foo[*].baz,bar[*]': "numbers[*]"}

    test(mappings)
