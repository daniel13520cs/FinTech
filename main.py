from asyncio.proactor_events import _ProactorDuplexPipeTransport
import numpy as np
import pandas as pd
import yfinance as yf
from finlab import data
import pickle
import matplotlib.pyplot as plt
import os

def fetch(id):
    df=yf.download(id + ".TWO",start='2018-03-20',end='2023-03-20')
    if df.empty:
        df=yf.download(id + ".TW",start='2018-03-20',end='2023-03-20')
    df.to_excel("finlab_db/" + id + ".xlsx")  
    print(df) 
        
def plot(idList):
    df1 = pd.read_excel("finlab_db/" + idList[0] + ".xlsx")
    for id in idList:
        #if not os.path.isfile("finlab_db/" + id + ".xlsx"):
        fetch(id)
        df = pd.read_excel("finlab_db/" + id + ".xlsx")
        df=df[['Close']]
        df=df.rename(columns = {'Close': id[:4]})   
        df1=df1.set_index(df1.index).join(df.set_index(df.index))
        
    print(df1)
    df1.to_excel("finlab_db/" + "Close" + ".xlsx")  
    df1.plot.line(y = idList, figsize=(9,6))
    
def show():
    plt.show();
    
#list = ["3303", "3004", "6690", "6811", "6874"]
list = ["3303", "3004"]
plot(list)
show()