import cse163_utils  # noqa: F401
# This is a hacky workaround to an unfortunate bug on macs that causes an
# issue with seaborn, the graphing library we want you to use on this
# assignment.  You can just ignore the above line or delete it if you are
# not using a mac!
# Add your imports and code here!

import pandas as pd
import seaborn as sns
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
sns.set()


def parse(file_name):
    """
    Parse the data from the given file_name(csv file).

    Takes na_values that specify NaN values in the file
    and will be replaced by NaN.
    """
    return pd.read_csv(file_name, na_values='---')


def completions_between_years(data, yr1, yr2, sex):
    """
    Retuns all rows of the given data that have data between the given years
    yr1(inclusive) and yr2(exclusive) and match the givnen sex.

    If no data is found for the given parameters, return None.
    """
    d = data[(data['Year'] >= yr1) & (data['Year'] < yr2)
             & (data['Sex'] == sex)]
    if len(d) == 0:
        return 'None'
    return d


def compare_bachelors_1980(data):
    """
    Returns a tuple (% for men, % for women) having earned Bachelor's degree
    in 1980.
    """
    d = data[(data['Year'] == 1980) & (data['Min degree'] == 'bachelor\'s')] \
        .groupby(['Sex'])['Total'].sum().loc[['M', 'F']]
    return (d[0], d[1])


def top_2_2000s(data):
    """
    Returns the list of tuples that are the two most commonly eanred degree
    between 2000 and 2010 (inclusive)
    """
    data = data[(data['Year'] >= 2000) & (data['Year'] <= 2010)
                & (data['Sex'] == 'A')].groupby(['Min degree'])['Total'] \
                                       .mean().nlargest(2)
    return [i for i in data.items()]


def percent_change_bachelors_2000s(data, sex='A'):
    """
    Returns the difference between total percent of bachelor's degrees in 2010
    and that in 2000.

    sex parameter is defaulted as 'A'
    """
    d = data[(data['Min degree'] == 'bachelor\'s') & (data['Sex'] == sex)]
    d2000 = d[d['Year'] == 2000]['Total'].sum()
    d2010 = d[d['Year'] == 2010]['Total'].sum()
    return d2010 - d2000


def line_plot_bachelors(data):
    """
    Plot the line chart of the total percentages of all people who have earned
    bachelor's degree as minimal completion over the years and save the plot.
    """
    data = data[data['Min degree'] == 'bachelor\'s'] \
        .groupby(['Year'])['Total'].sum()
    sns.lineplot(data.keys(), data.values)
    plt.savefig('line_plot_bachelors.png')


def bar_chart_high_school(data):
    """
    Plot the bar chart of the total percentages of women, men,
    and total people with a minimum education of high school degrees in 2009
    and save the plot.
    """
    data = data[(data['Min degree'] == 'high school')
                & (data['Year'] == 2009)].groupby(['Sex'])['Total'].sum()
    sns.barplot(data.keys(), data.values)
    plt.savefig('bar_chart_high_school.png')


def plot_hispanic_min_degree(data):
    """
    Plot the cat chart that shows how the percent of Hispanic people with
    degrees of high school and bachelor's degree has changed
    between 1990 and 2010 (inclusive) and save the plot.
    """
    data = data[(data['Year'] >= 1990) & (data['Year'] <= 2010) &
                ((data['Min degree'] == 'high school')
                    | (data['Min degree'] == 'bachelor\'s'))]
    sns.catplot(x="Year", y="Hispanic", hue="Min degree", data=data)
    plt.savefig('plot_hispanic_min_degree.png')


def fit_and_predict_degrees(data):
    """
    Returns the test mean square error
    """
    data = data[['Year', 'Min degree', 'Sex', 'Total']]
    data = data.dropna()
    data = pd.get_dummies(data)
    X = data.loc[:, data.columns != 'Total']
    y = data['Total']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = DecisionTreeRegressor()
    model.fit(X_train, y_train)
    y_test_pred = model.predict(X_test)
    return mean_squared_error(y_test, y_test_pred)


def main():
    data = parse('hw3-nces-ed-attainment')
    completions_between_years(data, 2007, 2008, 'F')
    cse163_utils.assert_equals((24.0, 21.0), compare_bachelors_1980(data))
    cse163_utils.assert_equals([('high school', 87.55714285714285),
                                ("associate's", 38.75714285714286)],
                               top_2_2000s(data))
    cse163_utils.assert_equals(2.599999999999998,
                               percent_change_bachelors_2000s(data))
    line_plot_bachelors(data)
    bar_chart_high_school(data)
    plot_hispanic_min_degree(data)
    fit_and_predict_degrees(data)
