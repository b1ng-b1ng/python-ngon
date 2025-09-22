import pandas as pd
data = {'Name':['Hung','Linh','tuan'],
        'Age':[12,12,12],
        'Weight':[45,67,55]
        }
df = pd.DataFrame(data)
# add col
df['Class'] = ['1','2','3']
# add row
new_rows = pd.DataFrame([{'Name':'Hoang','Age':12,'Weight':43,'Class':2},
                        ]
                        ,index=['3'])
df = pd.concat([df,new_rows])
print(df)