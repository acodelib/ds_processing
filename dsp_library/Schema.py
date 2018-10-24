import pandas
import csv
import copy

class Schema(object):
    """ETL Pipelines application domain. \n Represents the columns attributes in a data flow."""

    schema_cols         = []    
    schema_attributes   = []
    cols_attributes     = {}
    raw_data            = None
    metadata            = {}


    def __init__(self, path_to_csv_schema):              
        with open(path_to_csv_schema,"r") as schema_file:
            csv_as_dict = csv.DictReader(schema_file)

            self.schema_attributes = copy.deepcopy(csv_as_dict.fieldnames)
            self.schema_attributes.pop(0)            

            for dt in self.schema_attributes:
                self.cols_attributes[dt] = {}                            
            schema_file.seek(0)
            #print(type(self.schema_attributes))
            #print(self.schema_attributes)
            
            for rw in csv_as_dict:    
                if rw["column_name"]=="column_name":
                    continue
                self.schema_cols.append(rw["column_name"])                                                
                for a in self.schema_attributes:
                    self.cols_attributes[a][rw["column_name"]] = rw[a]
            #print(self.schema_cols)                    
            #print(self.cols_attributes)
            
      
        
                
            
            
    
                    
                    


        
        



