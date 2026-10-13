import pandas as pd

dict = {'Name':['chaitnya','sagar','amit','rohan'],
        'Age':[18,19,17,16],
        'Address':['pune','mumbai','Beed','nagar']}

df= pd.DataFrame(dict)
#bottom row
print(df.tail(3))