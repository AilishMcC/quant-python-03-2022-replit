# import package first
import pandas as pd

# load data file and assign it
surveys_df= pd.read_csv("surveys.csv")

# describe weight column
desc_weight = surveys_df["weight"].describe()

#Print out 
print(desc_weight)