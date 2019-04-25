
import pandas as pd


# Write your functions here!
def parse(file_name):
    """
    Parses the CSV file specified by file_name and returns the data as
    a DataFrame with contents of the file.
    """
    return pd.read_csv(file_name)


def species_count(data):
    """
    Returns the number of unique Pokemon names from the given data.
    """
    return len(data['name'].unique())


def max_level(data):
    """
    Returns the name and the level of Pokemon that has max level
    from the given data.

    If a tie exists, returns the Pokemon that appears earlier.
    """
    d = data.loc[data['level'] == data['level'].max(), ['name', 'level']]
    return [tuple(x) for x in d.values][0]


def filter_range(data, a, b):
    """
    Returns the list of names of Pokemons that have level within
    the range between a(inclusive) and b(exclusive) from the given data.

    The list returned has the order as they appear in the given data.
    """
    d = data[(data['level'] >= a) & (data['level'] < b)]['name']
    return [x for x in d.values]


def mean_attack_for_type(data, type):
    """
    Returns the mean of attack for Pokemons with the given type
    from the given data.

    If no Pokemon has the given type from the given data, returns None.
    """
    return data[data['type'] == type]['atk'].mean()


def count_types(data):
    """
    Returns a dictionary with keys that are Pokemon types and values that are
    the number of Pokemons of each corresponding key from the given data.
    """
    d = data.groupby(['type'])['name'].count()
    dic = {}
    for x, y in d.items():
        dic[x] = y
    return dic


def highest_stage_per_type(data):
    """
    Returns a dictionary with keys that are Pokemon types and values that are
    the highest stage of each corresponding key from the given data.
    """
    d = data.groupby(['type'])['stage'].max()
    dic = {}
    for x, y in d.items():
        dic[x] = y
    return dic


def mean_attack_per_type(data):
    """
    Returns a dictionary with keys that are Pokemon types and values that are
    the mean attack of each corresponding key from the given data.
    """
    d = data.groupby(['type'])['atk'].mean()
    dic = {}
    for x, y in d.items():
        dic[x] = y
    return dic
