from pandas import DataFrame

def is_between(val: int, lower_bound: int, upper_bound: int) -> bool:
    return val >= lower_bound and val <= upper_bound


#=======================================================================
def indent(text: str, pad: int) -> str:
    return (" " * pad) + text

def createDfObject(df: DataFrame, componentName: str) -> None:
    DEFAULT_PAD_NUM : int = 4

    print("class {}:".format(componentName))
    print(indent("def __init__(self, df: DataFrame = None):", DEFAULT_PAD_NUM))

    for col in df.columns:
        print(indent("self.col_{} = '{}'".format(col.lower(), col), DEFAULT_PAD_NUM * 2))

    print(indent("if df is not None:", DEFAULT_PAD_NUM * 2))
    print(indent("self.main_df = df", DEFAULT_PAD_NUM * 3))
