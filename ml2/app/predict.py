from typing import List
import joblib
import pandas as pd
import numpy as np

model = joblib.load('models/ml2_v17.joblib')

def data_ch_trimmed(data):
    
    if "SalePrice" in data.columns:
        labels = data["SalePrice"]
        data=data.drop("SalePrice",axis=1)
    else:
        labels=None
    unnessecary_feature=[
        'index',
        'Id',
        'MSSubClass',
        'MSZoning',
        'LotFrontage',
        'LotArea',
        'Street',
        'MasVnrType', 
        'ExterQual', 
        'ExterCond', 
        'Foundation', 
        'BsmtQual', 
        'BsmtCond',
        'BsmtExposure', 
        'BsmtFinType1', 
        'BsmtFinSF1', 
        'BsmtFinType2', 
        'BsmtFinSF2', 
        'BsmtUnfSF', 
        '3SsnPorch', 
        'ScreenPorch',
        'PoolArea',
        'PoolQC', 
        'Fence', 
        'MiscFeature', 
        'MiscVal', 
        'MoSold', 
        'YrSold', 
        'SaleType', 
        'SaleCondition',
        'saleprice_cat',
        'GarageYrBlt', 
        'MasVnrArea', 
        'Heating', 
        'HeatingQC', 
        'Alley',
        'LotShape',
        'LandContour', 
        'Utilities', 
        'LotConfig', 
        'LandSlope', 
        'Neighborhood', 
        'Condition1',
        'Condition2', 
        'BldgType', 
        'HouseStyle',
        'OverallCond', 
        'RoofStyle', 
        'RoofMatl', 
        'Exterior1st',
        'Exterior2nd', 
        'CentralAir', 
        'Electrical', 
        '2ndFlrSF', 
        'LowQualFinSF', 
        'BsmtFullBath', 
        'BsmtHalfBath',
        'HalfBath',
        'BedroomAbvGr', 
        'KitchenAbvGr', 
        'KitchenQual', 
        'Functional', 
        'FireplaceQu', 
        'GarageType', 
        'GarageFinish',
        'GarageQual', 
        'GarageCond', 
        'PavedDrive', 
        'EnclosedPorch', 
        'Fireplaces', 
        'WoodDeckSF', 
        'OpenPorchSF']
    
    
    
    
    
    for feat in unnessecary_feature:
        if feat in data.columns:
            data=data.drop(feat,axis=1)
    
    
    from sklearn.impute import SimpleImputer
    imputer = SimpleImputer(strategy="median")
    freq_imputer = SimpleImputer(strategy="most_frequent")

    data_numbr = data.select_dtypes(include=[np.number])
    data_imputed = imputer.fit_transform(data_numbr)
    features = list(data_numbr.columns)
    output = np.hstack([data_imputed])
    return output,labels,features
    
def predict(data):
    values = data

    column_order = [
        'OverallQual',
        'YearBuilt',
        'YearRemodAdd',
        'TotalBsmtSF',
        'FirstFlrSF',
        'GrLivArea',
        'FullBath',
        'TotRmsAbvGrd',
        'GarageCars',
        'GarageArea']
 
    
    values = [values[feat] for feat in column_order]
    values = pd.DataFrame([list(values)],columns=[c for c in column_order])

    test_data, test_labels, test_features = data_ch_trimmed(values)
    values = test_data
    pred = model.predict(values.reshape(1, -1))

    return pred[0]