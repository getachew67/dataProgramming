
def parse(file_name, int_cols):
    """
    Parses the CSV file specified by file_name and returns the data as a list
    of dictionaries where each row is represented by a dictionary that
    has keys for each column and value which is the entry for that column
    at that row.

    Also takes a list of column names that should have the data for that column
    converted to integers. All other data will be str.
    """
    data = []
    with open(file_name) as f:
        headers = f.readline().strip().split(',')
        num_cols = len(headers)

        for line in f.readlines():
            row_data = line.strip().split(',')
            row = {}
            for i in range(num_cols):
                if headers[i] in int_cols:
                    row[headers[i]] = int(row_data[i])
                else:
                    row[headers[i]] = row_data[i]
            data.append(row)
    return data


# Write your solutions here!
def species_count(data):
    """
    Returns the number of unique Pokemon names from the given data.
    """
    s = set()
    for pokemon in data:
        s.add(pokemon['name'])
    return len(s)


def max_level(data):
    """
    Returns the name and the level of Pokemon that has max level
    from the given data.

    If a tie exists, returns the Pokemon that appears earlier.
    """
    max = 0
    name = None
    for pokemon in data:
        if max < pokemon['level']:
            max = pokemon['level']
            name = pokemon['name']
    return (name, max)


def filter_range(data, a, b):
    """
    Returns the list of names of Pokemons that have level within
    the range between a(inclusive) and b(exclusive) from the given data.

    The list returned has the order as they appear in the given data.
    """
    output = list()
    for pokemon in data:
        if a <= pokemon['level'] and pokemon['level'] < b:
            output.append(pokemon['name'])
    return output


def mean_attack_for_type(data, type):
    """
    Returns the mean of attack for Pokemons with the given type
    from the given data.

    If no Pokemon has the given type from the given data, returns None.
    """
    sum = 0
    n = 0
    for pokemon in data:
        if pokemon['type'] == type:
            sum += pokemon['atk']
            n += 1
    if n == 0:
        return None
    else:
        return sum/n


def count_types(data):
    """
    Returns a dictionary with keys that are Pokemon types and values that are
    the number of Pokemons of each corresponding key from the given data.
    """
    d = {}
    for pokemon in data:
        if pokemon['type'] in d:
            d[pokemon['type']] += 1
        else:
            d[pokemon['type']] = 1
    return d


def highest_stage_per_type(data):
    """
    Returns a dictionary with keys that are Pokemon types and values that are
    the highest stage of each corresponding key from the given data.
    """
    d = {}
    for pokemon in data:
        if pokemon['type'] in d:
            if d[pokemon['type']] < pokemon['stage']:
                d[pokemon['type']] = pokemon['stage']
        else:
            d[pokemon['type']] = pokemon['stage']
    return d


def mean_attack_per_type(data):
    """
    Returns a dictionary with keys that are Pokemon types and values that are
    the mean attack of each corresponding key from the given data.
    """
    d = {}
    for pokemon in data:
        if pokemon['type'] in d:
            ty = pokemon['type']
            d[ty] = [d[ty][0] + pokemon['atk'], d[ty][1] + 1]
        else:
            d[pokemon['type']] = [pokemon['atk'], 1]
    for each in d:
        d[each] = (d[each][0])/(d[each][1])
    return d
