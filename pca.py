import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def pca_run(df):
    # parse columns into numericals and categorials
    num_cols_data = []
    cat_cols_data = []

    for i in df.columns:
        if df[i].dtype == np.dtype('float64') or df[i].dtype == np.dtype('int64'):
            num_cols_data.append(df[i])
        else:
            cat_cols_data.append(df[i])

    num_data = pd.concat(num_cols_data,axis=1)
    cat_data = pd.concat(cat_cols_data,axis=1)

    # fill numerical data where na
    num_data = num_data.apply(lambda x: x.fillna(x.mean()))
    # scale numerical data
    scaler = StandardScaler()
    scaled_values = scaler.fit_transform(num_data)

    # run PCA algo
    pca = PCA()
    pca_data = pca.fit_transform(scaled_values)
    pca_data = pd.DataFrame(pca_data)

    # rename column names
    new_col_names   = ['PCA_' + str(i) for i in range(1,len(pca_data.columns)+1)]
    col_name_mapper = dict( zip( list(pca_data.columns), new_col_names ) )
    pca_data = pca_data.rename(col_name_mapper,axis=1)
    output = pd.concat([df,pca_data],axis=1)

    return output, cat_data.columns.to_list(), new_col_names