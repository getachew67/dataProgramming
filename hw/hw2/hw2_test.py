from cse163_utils import assert_equals
# Don't worry about this import syntax, we will talk about it later

import hw2_manual
import hw2_pandas

data1 = hw2_manual.parse('pokemon_test.csv', ['id', 'level', 'atk', 'def',
                         'hp', 'stage'])
data2 = hw2_pandas.parse('pokemon_test.csv')
data3 = hw2_manual.parse('pokemon_box.csv', ['id', 'level', 'atk', 'def',
                         'hp', 'stage'])
data4 = hw2_pandas.parse('pokemon_box.csv')
data5 = hw2_manual.parse('pokemon_test2.csv', ['id', 'level', 'atk', 'def',
                         'hp', 'stage'])
data6 = hw2_pandas.parse('pokemon_test2.csv')


# This file is left blank for you to fill in with your tests!
def test_species_count():
    """
    Test the function species_count
    """
    print('Testing species_count')

    assert_equals(3, hw2_manual.species_count(data1))
    assert_equals(3, hw2_pandas.species_count(data2))
    assert_equals(82, hw2_manual.species_count(data3))
    assert_equals(82, hw2_pandas.species_count(data4))
    assert_equals(8, hw2_manual.species_count(data5))
    assert_equals(8, hw2_pandas.species_count(data6))


def test_max_level():
    """
    Test the function max_level
    """
    print('Testing max_level')

    assert_equals(('Lapras', 72), hw2_manual.max_level(data1))
    assert_equals(('Lapras', 72), hw2_pandas.max_level(data2))
    assert_equals(('Victreebel', 100), hw2_manual.max_level(data3))
    assert_equals(('Victreebel', 100), hw2_pandas.max_level(data4))
    assert_equals(('Magmar', 96), hw2_manual.max_level(data5))
    assert_equals(('Magmar', 96), hw2_pandas.max_level(data6))


def test_filter_range():
    """
    Test the function filter_range
    """
    print('Testing filter_range')

    assert_equals(['Arcanine', 'Arcanine', 'Starmie'],
                  hw2_manual.filter_range(data1, 30, 70))
    assert_equals(['Arcanine', 'Arcanine', 'Starmie'],
                  hw2_pandas.filter_range(data2, 30, 70))
    assert_equals([], hw2_manual.filter_range(data1, 40, 60))
    assert_equals([], hw2_pandas.filter_range(data2, 40, 60))
    assert_equals(['Lapras'], hw2_manual.filter_range(data1, 72, 75))
    assert_equals(['Lapras'], hw2_pandas.filter_range(data2, 72, 75))
    assert_equals(['Butterfree', 'Poliwag', 'Sandslash', 'Nidorina', 'Goldeen',
                   'Ditto', 'Dugtrio'], hw2_manual.filter_range(data3, 10, 15))
    assert_equals(['Butterfree', 'Poliwag', 'Sandslash', 'Nidorina', 'Goldeen',
                   'Ditto', 'Dugtrio'], hw2_pandas.filter_range(data4, 10, 15))
    assert_equals(['Magmar', 'Kingler', 'Venusaur'],
                  hw2_manual.filter_range(data5, 30, 50))
    assert_equals(['Magmar', 'Kingler', 'Venusaur'],
                  hw2_pandas.filter_range(data6, 30, 50))


def test_mean_attack_for_type():
    """
    Test the function mean_attack_for_type
    """
    print('Testing mean_attack_for_type')

    assert_equals(47.5, hw2_manual.mean_attack_for_type(data1, 'fire'))
    assert_equals(47.5, hw2_pandas.mean_attack_for_type(data2, 'fire'))
    assert_equals(140.5, hw2_manual.mean_attack_for_type(data1, 'water'))
    assert_equals(140.5, hw2_pandas.mean_attack_for_type(data2, 'water'))
    assert_equals(108.0, hw2_manual.mean_attack_for_type(data3, 'normal'))
    assert_equals(108.0, hw2_pandas.mean_attack_for_type(data4, 'normal'))
    assert_equals(79.0, hw2_manual.mean_attack_for_type(data5, 'fire'))
    assert_equals(79.0, hw2_pandas.mean_attack_for_type(data6, 'fire'))


def test_count_types():
    """
    Test the function count_types
    """
    print('Testing count_types')

    assert_equals({'water': 2, 'fire': 2}, hw2_manual.count_types(data1))
    assert_equals({'water': 2, 'fire': 2}, hw2_pandas.count_types(data2))
    assert_equals({'fighting': 1, 'fire': 2, 'grass': 3, 'normal': 1,
                  'poison': 1, 'water': 1}, hw2_manual.count_types(data5))
    assert_equals({'fighting': 1, 'fire': 2, 'grass': 3, 'normal': 1,
                  'poison': 1, 'water': 1}, hw2_pandas.count_types(data6))


def test_highest_stage_per_type():
    """
    Test the function highest_stage_per_type
    """
    print('Testing highest_stage_per_type')

    assert_equals({'water': 2, 'fire': 2},
                  hw2_manual.highest_stage_per_type(data1))
    assert_equals({'water': 2, 'fire': 2},
                  hw2_pandas.highest_stage_per_type(data2))
    assert_equals({'fighting': 2, 'fire': 1, 'grass': 3, 'normal': 1, 'poison':
                   1, 'water': 2}, hw2_manual.highest_stage_per_type(data5))
    assert_equals({'fighting': 2, 'fire': 1, 'grass': 3, 'normal': 1, 'poison':
                   1, 'water': 2}, hw2_pandas.highest_stage_per_type(data6))


def test_mean_attack_per_type():
    """
    Test the function mean_attack_per_type
    """
    print('Testing mean_attack_per_type')

    assert_equals({'water': 140.5, 'fire': 47.5},
                  hw2_manual.mean_attack_per_type(data1))
    assert_equals({'water': 140.5, 'fire': 47.5},
                  hw2_pandas.mean_attack_per_type(data2))
    assert_equals({'fighting': 20, 'fire': 79, 'grass': 105, 'normal': 68,
                   'poison': 30, 'water': 110},
                  hw2_manual.mean_attack_per_type(data5))
    assert_equals({'fighting': 20, 'fire': 79, 'grass': 105, 'normal': 68,
                   'poison': 30, 'water': 110},
                  hw2_pandas.mean_attack_per_type(data6))


def main():
    test_species_count()
    test_max_level()
    test_filter_range()
    test_mean_attack_for_type()
    test_count_types()
    test_highest_stage_per_type()
    test_mean_attack_per_type()


if __name__ == '__main__':
    main()
