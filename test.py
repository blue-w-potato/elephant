import pandas as pd
import numpy as np
import bluePotato

a = pd.DataFrame({'a':[1111,311,113],
                  'b':[455,157,556],
                  'c':[67,166,691]})
print(a)
print('='*100)

b = bluePotato.append.Average.column(a, 'yee')
print(b)
b = bluePotato.append.Average.column(a, 'yee', f=3, mode=1)
print(b)
b = bluePotato.append.Average.column(a, 'yee', f=3, mode=2)
print(b)
b = bluePotato.append.Average.column(a, 'yee', f=3, mode=3)
print(b)
b = bluePotato.append.Average.column(a, 'yee', f=3, mode=4)
print(b)