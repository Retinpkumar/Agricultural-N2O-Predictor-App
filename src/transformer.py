import pandas as pd
import numpy as np


def input_transformer():
    # reading data
    df = pd.read_excel('data/Saha_et_al_2020_ERL_Data.xlsx', sheet_name='Data')
    # creating mean DAF feature
    df['Mean_DAF'] = (df['DAF_SD'] + df['DAF_TD']) * 0.5
    # dropping columns
    df = df.drop(columns=['Date', 'Year', 'Experiment', 'DataUse', 'Replication', 'VegType', 'DAF_SD', 'DAF_TD'], axis=1)
    df['WFPS25cm'] = df['WFPS25cm'].fillna(0.321753)  # constant value imputation
    df['NH4'] = df['NH4'].fillna(np.mean(df['NH4']))  # mean imputation
    df['NO3'] = df['NO3'].fillna(np.mean(df['NO3']))  # mean imputation
    for feat in ['PP2', 'PP7', 'NH4', 'NO3', 'Mean_DAF']:
        df[feat] = df[feat].astype('float')
        # log transformation
        df[feat] = np.log1p(df[feat])
        # Winsorizing
        q1 = df[feat].quantile(0.25)
        q3 = df[feat].quantile(0.75)
        iqr = q3 - q1
        upper = q3 + (1.5 * iqr)
        lower = q1 - (1.5 * iqr)
        df[feat] = np.where(df[feat] > upper, upper, np.where(df[feat] < lower, lower, df[feat]))
    return df
