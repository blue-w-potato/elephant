import pandas as pd
import math as mm
import numpy as np

class append:
    class Total:
        def column(data:pd.DataFrame, columnName:str = 'total'):
            data[columnName] = sum([data[i] for i in data.columns])
            return data
        
        def row(data:pd.DataFrame):
            data = data._append({i:data[i].sum() for i in data.columns}, ignore_index = True)
            return data
        
    class Average:
        def column(data:pd.DataFrame, columnName:str = 'total', f:int = 3, mode:int = 0):
            '''
            data: 來源資料，型別一定要DataFrame
            colunName: 新欄的欄名
            f: mode = 0 :不額外處理

               mode = 1 :四捨五入到小數點後f位
               mode = 2 :四捨五入到10**f 

               mode = 3 :無條件捨去到小數點後f位
               mode = 4 :無條件捨去到10**f 

               mode = 5 :無條件進位到小數點後f位
               mode = 6 :無條件進位到10**f 
            '''
            columns = pd.Series(data.columns)
            average = sum([data[i] for i in columns])/columns.size
            t = (10**f)
            if mode == 0:
                data[columnName] = sum([data[i] for i in columns])/columns.size
            if mode == 1:
                data[columnName] = round(average,f)
            elif mode == 2:
                data[columnName] = round(average/(10**(f-1)))*(10**(f-1))
            
            elif mode == 3:
                data[columnName] = np.ceil(average)
            elif mode == 4:
                data[columnName] = np.ceil(average) 
            return data 
        
        def row(data:pd.DataFrame, f:int = 3, p:int = 1):
            if f:
                data = data._append({i:round(data[i].sum()/data[i].size, f) for i in data.columns}, ignore_index = True)
            else:
                data = data._append({i:data[i].sum()//data[i].size//(10**p)*(10**p) for i in data.columns}, ignore_index = True)
            return data

    
    
class getTotal:
    def column(data:pd.DataFrame, columnName:str = 'total'):
        return pd.DataFrame({f'{columnName}':sum([data[i] for i in data.columns])})
    
    def row(data:pd.DataFrame):
        return pd.DataFrame({i:data[i].sum() for i in data.columns})