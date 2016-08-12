import pandas as pd
def load_data():
    '''
    The load_data() function reads specific .csv files in a given directory.
    Depends on the pandas function: read_csv()
    The dataframes: members, roles, status, eyecolor, members_status, members_roles,
    and physical_charact are created.
    as a result.
     
    Use as following:
    members, roles, status, eyecolor, members_status, members_roles, physical_charact = load_data()
    '''
    print('Reading data...')
    members  = pd.read_csv('members.csv')
    roles    = pd.read_csv('roles.csv')
    status   = pd.read_csv('status.csv')
    eyecolor = pd.read_csv('eyecolor.csv')
    members_status   = pd.read_csv('members_status.csv')
    members_roles    = pd.read_csv('members_roles.csv')
    physical_charact = pd.read_csv('physical_charact.csv')
    print('Alright! \n')
    return members, roles, status, eyecolor, members_status, members_roles, physical_charact
