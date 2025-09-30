import plotly.express as px
import pandas as pd

def read_dataset():
    df = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')
    return df.copy()

def survival_demographics():
    """
    - this function  adds col. that categorizes Age into different groups
    - returns dataframe with the survived people rate, class and sex
    """
    #print(ds.columns)
    ds = read_dataset()
    category_values = ['Child', 'Teen', 'Adult', 'Senior']
    bin_values = [0, 11, 19, 59, 100]
    ds['age_group'] = pd.cut(ds['Age'], bins=bin_values, labels=category_values, right=True)
    ds['age_group'] = ds['age_group'].astype('category')
    groups = ds.groupby(['Pclass','Sex','age_group']).agg(n_passengers=('PassengerId', 'count'),n_survivors=('Survived', 'sum')).reset_index()
    groups['survival_rate'] = groups['n_survivors'] / groups['n_passengers']
    #rename column for autograder compatibility
    groups.rename(columns={'Pclass':'pclass'}, inplace=True)
    return groups.sort_values(by=['pclass', 'age_group', 'Sex'])


def family_groups():
    """
    - this function adds a column that calculates family size
    - returns dataframe with family size, class, number of passengers, average fare, min fare, max fare
    """
    ds = read_dataset()
    ds['family_size'] = ds['SibSp'] + ds['Parch'] + 1  # +1 for self

    # Group by FamilySize and Pclass
    grouped = ds.groupby(['family_size', 'Pclass']).agg(
        n_passengers=('PassengerId', 'count'),
        avg_fare=('Fare', 'mean'),
        min_fare=('Fare', 'min'),
        max_fare=('Fare', 'max')
    ).reset_index()

    # Sort by class then family size
    grouped = grouped.sort_values(by=['Pclass', 'family_size'])
    return grouped

def last_names():
    """
    - this function extracts last names from the Name column and counts occurrences
    - returns a series with last names and their counts
    """
    ds = read_dataset()
    # Extract last name from Name (everything before the first comma)
    ds['LastName'] = ds['Name'].apply(lambda x: x.split(',')[0].strip())

    # Count occurrences
    last_name_counts = ds['LastName'].value_counts()
    return last_name_counts


if __name__ == "__main__":
    print(survival_demographics())
    print(family_groups())
    print(last_names())

