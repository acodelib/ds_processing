from dsp_library import DataAdapter
from pymssql import *

class MssqlAdapter(DataAdapter):

    ##----------------------------------------------------CONSTRUCTOR----------------------------------------------------------------
    def __init__(self,**kwargs):
        super(MssqlAdapter,self).__init__(**kwargs)
        self.TYPE_TAG = "mssql"
    
