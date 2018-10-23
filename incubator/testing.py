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
import dsp_library as d

sc = d.Schema("C:\DIRECT\source_code\ds_processing\Book1.csv")
mssql = sc.cols_attributes["type_mssql"]
for k,v in mssql.items():
        print("{}  {},".format(k,v))