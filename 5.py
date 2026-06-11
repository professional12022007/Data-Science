import pandas as pd
dic={
    "name":["tom","nick","krish","jack"],
    "age":[20,21,19,18],
    "roll":[1,2,3,4]
}
df=pd.DataFrame(dic)
print(df)
pd.display(df)