from abc import ABCMeta,abstractmethod
from dsp_library import Schema
import inspect


class DataAdapter(object):
    '''Defines the abstraction of a Data Adapter type. This type handles operations (SELECT DML and DDL) against a DB-like source'''
    __metaclass__ = ABCMeta

    TYPE_TAG = ""

    ##-------------------------------------------------------FIELDS------------------------------------------------------------------    
    name     = ""    
    __schema = None

    @property
    def schema(self):
        if self.__schema == None:
            print("Warning! Schema is not set yet")
        return self.__schema

    @schema.setter
    def schema(self,a_schema_object):
        if inspect.isclass(a_schema_object) == False and issubclass(type(a_schema_object),Schema) == False:
            raise TypeError("The Schema argument is not a Schema instance")
        self.__schema = a_schema_object

    ##----------------------------------------------------CONSTRUCTOR----------------------------------------------------------------
    def __init__(self,**kwargs):
        self.name = kwargs["name"]
    ##------------------------------------------------------METHODS------------------------------------------------------------------