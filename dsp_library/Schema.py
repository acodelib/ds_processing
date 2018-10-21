import pandas

class DataSchema(object):
    '''ETL Pipelines application domain. \n Represents the columns attributes in a data flow.'''

    col_names = []
    raw_data  = None


    def __init__(self, path_to_csv_schema):
        self.raw_data = pandas.DataFrame.from_csv(path= path_to_csv_schema,parse_dates=False)

