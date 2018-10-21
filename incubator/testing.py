'''
def gen_fun(some_list):
    for j in some_list:
        yield j

g = gen_fun([1,2,3,4,5,6])

print(type(g))

for c in g:
    print(c)

'''

#from dsp_library import DataSchema
from dsp_library import Schema as s


sc = s.DataSchema("C:\DIRECT\source_code\ds_processing\Book1.csv")

p = sc.raw_data["type_mssql"]

print(p)
 print(type(p))
     

