import pandas as pd

def ImportingData() :
    data = pd.read_csv("Data_set\Eartquakes-1990-2023.csv")
    return data 
    