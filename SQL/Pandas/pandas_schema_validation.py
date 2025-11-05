"""
Dataframe Creation Guidelines
-------------------------------

1. The column names of any dataframe shall be saved in a class that use their string equivalents
    a. This allows for safer implementation of queries, schema checks, etc.

2. all __init__ methods shall at least 2 arguments passed to them
    a. self 
        i. this Python required

    b. DataFrame object = None
        i. Having this as an optional argument allows flexibility to associate a specific dataframe with an object instance, while
            also allowing for the use of the column names independently should one desire to use them

3. If a DataFrame is passed as an argument from the caller as source data, the schema must be validated as the time of instantiation
    a. Therefore, all objects should have a validate schema method that runs in these cases

"""
from pandas import DataFrame
from pandera.pandas import DataFrameSchema, Column
from pandera.errors import SchemaError
import sys

def generic_schema_validation(schema: DataFrameSchema, df: DataFrame, componentName: str):
    try:
        schema.validate(df)
    except SchemaError:
        print("Schema for {} does not match what is expected. Exiting".format(componentName))
        sys.exit(1)
