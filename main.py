import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

if __name__ == '__main__':
    data['human'] = data['whoAmI'].apply(lambda columns: columns == "human")
    data['robot'] = data['whoAmI'].apply(lambda columns: columns == "robot")
    data = data.drop('whoAmI', axis=1)
    print(data)
