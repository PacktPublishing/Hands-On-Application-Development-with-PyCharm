import pandas as pd
import numpy as np

import os
import gc


#%% Read in data

user_file_list = os.listdir('data/Archived users/')
user_set_v1 = set(map(lambda x: x[5: 15], user_file_list))  # [5: 15] to return just the user IDs


tappy_file_list = os.listdir('data/Tappy Data/')
user_set_v2 = set(map(lambda x: x[: 10], tappy_file_list))  # [: 10] to return just the user IDs


user_set = user_set_v1.intersection(user_set_v2)

print(len(user_set))


#%% Format into a Pandas dataframe

def read_user_file(file_name):
    f = open('data/Archived users/' + file_name)
    data = [line.split(': ')[1][: -1] for line in f.readlines()]
    f.close()

    return data

files = os.listdir('data/Archived users/')

columns = [
    'BirthYear', 'Gender', 'Parkinsons', 'Tremors', 'DiagnosisYear',
    'Sided', 'UPDRS', 'Impact', 'Levadopa', 'DA', 'MAOB', 'Other'
]

user_df = pd.DataFrame(columns=columns) # empty Data Frame for now

for user_id in user_set:
    temp_file_name = 'User_' + user_id + '.txt' # tappy file names have the format of `User_[UserID].txt`
    if temp_file_name in files: # check to see if the user ID is in our valid user set
        temp_data = read_user_file(temp_file_name)
        user_df.loc[user_id] = temp_data # adding data to our DataFrame

print(user_df.head())


#%% Change numeric data into appropriate format

# force some columns to have numeric data type
user_df['BirthYear'] = pd.to_numeric(user_df['BirthYear'], errors='coerce')
user_df['DiagnosisYear'] = pd.to_numeric(user_df['DiagnosisYear'], errors='coerce')


#%% "Binarize" true-false data

user_df = user_df.rename(index=str, columns={'Gender': 'Female'})  # renaming `Gender` to `Female`
user_df['Female'] = user_df['Female'] == 'Female'  # change string data to boolean data
user_df['Female'] = user_df['Female'].astype(int)  # change boolean data to binary data

str_to_binary_columns = ['Parkinsons', 'Tremors', 'Levadopa', 'DA', 'MAOB', 'Other']  # columns to be converted to binary data

for column in str_to_binary_columns:
    user_df[column] = user_df[column] == 'True'
    user_df[column] = user_df[column].astype(int)


#%% Dummy variable (one-hot encoding)

# prior processing for `Impact` column
user_df.loc[
    (user_df['Impact'] != 'Medium') &
    (user_df['Impact'] != 'Mild') &
    (user_df['Impact'] != 'Severe'), 'Impact'] = 'None'


to_dummy_column_indices = ['Sided', 'UPDRS', 'Impact']  # columns to be one-hot encoded

for column in to_dummy_column_indices:
    user_df = pd.concat([
        user_df.iloc[:, : user_df.columns.get_loc(column)],
        pd.get_dummies(user_df[column], prefix=str(column)),
        user_df.iloc[:, user_df.columns.get_loc(column) + 1 :]
    ], axis=1)

print(user_df.head())


#%% Explore the second dataset

file_name = '0EA27ICBLF_1607.txt'  # an arbitrary file to explore


df = pd.read_csv(
    'data/Tappy Data/' + file_name,
    delimiter = '\t',
    index_col = False,
    names = ['UserKey', 'Date', 'Timestamp', 'Hand', 'Hold time', 'Direction', 'Latency time', 'Flight time']
)

df = df.drop('UserKey', axis=1)

print(df.head())


#%% Format datetime data

df['Date'] = pd.to_datetime(df['Date'], errors='coerce', format='%y%M%d').dt.date
# converting time data to numeric
for column in ['Hold time', 'Latency time', 'Flight time']:
    df[column] = pd.to_numeric(df[column], errors='coerce')

df = df.dropna(axis=0)

print(df.head())


#%% Remove incorrect data

# cleaning data in Hand
df = df[
    (df['Hand'] == 'L') |
    (df['Hand'] == 'R') |
    (df['Hand'] == 'S')
]

# cleaning data in Direction
df = df[
    (df['Direction'] == 'LL') |
    (df['Direction'] == 'LR') |
    (df['Direction'] == 'LS') |
    (df['Direction'] == 'RL') |
    (df['Direction'] == 'RR') |
    (df['Direction'] == 'RS') |
    (df['Direction'] == 'SL') |
    (df['Direction'] == 'SR') |
    (df['Direction'] == 'SS')
]

print(df.head())


#%% Group by direction (hand transition)

direction_group_df = df.groupby('Direction').mean()
print(direction_group_df)


#%% Combine into one function

def read_tappy(file_name):
    df = pd.read_csv(
        'data/Tappy Data/' + file_name,
        delimiter='\t',
        index_col=False,
        names=['UserKey', 'Date', 'Timestamp', 'Hand', 'Hold time',
               'Direction', 'Latency time', 'Flight time']
    )

    df = df.drop('UserKey', axis=1)

    df['Date'] = pd.to_datetime(df['Date'], errors='coerce', format='%y%M%d').dt.date

    # Convert time data to numeric
    for column in ['Hold time', 'Latency time', 'Flight time']:
        df[column] = pd.to_numeric(df[column], errors='coerce')
    df = df.dropna(axis=0)

    # Clean data in `Hand`
    df = df[
        (df['Hand'] == 'L') |
        (df['Hand'] == 'R') |
        (df['Hand'] == 'S')
        ]

    # Clean data in `Direction`
    df = df[
        (df['Direction'] == 'LL') |
        (df['Direction'] == 'LR') |
        (df['Direction'] == 'LS') |
        (df['Direction'] == 'RL') |
        (df['Direction'] == 'RR') |
        (df['Direction'] == 'RS') |
        (df['Direction'] == 'SL') |
        (df['Direction'] == 'SR') |
        (df['Direction'] == 'SS')
        ]

    direction_group_df = df.groupby('Direction').mean()
    del df
    gc.collect()

    direction_group_df = direction_group_df.reindex(
        ['LL', 'LR', 'LS', 'RL', 'RR', 'RS', 'SL', 'SR', 'SS'])
    direction_group_df = direction_group_df.sort_index()  # to ensure correct order of data

    return direction_group_df.values.flatten()  # returning a numppy array


def process_user(user_id, filenames):
    running_user_data = np.array([])

    for filename in filenames:
        if user_id in filename:
            running_user_data = np.append(running_user_data, read_tappy(filename))

    running_user_data = np.reshape(running_user_data, (-1, 27))  # flatten time data

    return np.nanmean(running_user_data, axis=0)  # ignoring NaNs while calculating the mean


#%% Run through all available data

import warnings; warnings.filterwarnings("ignore")


filenames = os.listdir('data/Tappy Data/')

column_names = [first_hand + second_hand + '_' + time
                for first_hand in ['L', 'R', 'S']
                for second_hand in ['L', 'R', 'S']
                for time in ['Hold time', 'Latency time', 'Flight time']]

user_tappy_df = pd.DataFrame(columns=column_names)

for user_id in user_df.index:
    user_tappy_data = process_user(str(user_id), filenames)
    user_tappy_df.loc[user_id] = user_tappy_data

# Some preliminary data cleaning
user_tappy_df = user_tappy_df.fillna(0)
user_tappy_df[user_tappy_df < 0] = 0

print(user_tappy_df.head())


#%% Save processed data

combined_user_df = pd.concat([user_df, user_tappy_df], axis=1)
print(combined_user_df.head())

combined_user_df.to_csv('data/combined_user.csv')
