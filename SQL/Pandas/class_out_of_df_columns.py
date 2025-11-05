def createDfObject(df: DataFrame, componentName: str) -> None:
    def indent(text: str, pad: int) -> str:
        return (" " * pad) + text

    default_pad_num : int = 4

    print("class {}:".format(componentName))
    print(indent("def __init__(self, df: DataFrame = None):", default_pad_num))

    for col in df.columns:
        print(indent("self.col_{} = '{}'".format(col.lower(), col), default_pad_num * 2))

    print(indent("if df is not None:", default_pad_num * 2))
    print(indent("self.main_df = df", default_pad_num * 3))


def main():
  createDfObject(pd.read_csv("Salaries.csv", sep=','), "Salaries")

if __name__ == "__main__": 
    main()  
