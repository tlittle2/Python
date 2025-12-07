from pandas import DataFrame, Series
from datetime import datetime
import numpy as np

def set_guid(df: DataFrame, app_id: str):
    seq_nums = np.arange(1, len(df) + 1).astype(str)
    prefix = datetime.today().date().strftime("%Y%m%d")

    for num in range(len(seq_nums)):
        seq_nums[num] = prefix + app_id + str.rjust(seq_nums[num], 12, '0')

    return Series(seq_nums)

#=======================================================================
def indent(text: str, indentDepth: int) -> str:
    return (" " * (4 * indentDepth)) + text

def createDfObject(df: DataFrame, componentName: str) -> None:

    print("class {}:".format(componentName))
    print(indent("def __init__(self, df: DataFrame = None):", 1))

    for col in df.columns:
        print(indent("self.col_{} = '{}'".format(col.lower(), col), 2))

    print(indent("if df is not None:", 2))
    print(indent("self.main_df = df", 3))
