# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# create an empty dataset with ID column

# dummy_data = pd.DataFrame(np.random.rand(100, 10))
# dummy_data['Id'] = list(range(10))*10

# # # save it to the dataframe
# inp = dataiku.Dataset("test")
# inp.write_with_schema(dummy_data)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs and take the input schema to output dataset

inp = dataiku.Dataset("test")
out = dataiku.Dataset("output")
out.write_schema_from_dataframe(inp.get_dataframe())

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
count = 0 
with out.get_writer() as writer:
    
    for df in inp.iter_dataframes(chunksize=10): # access the input dataset in the chunks of 10 rows 
        count += 1
        print(count)
        # Make some changes for the columns in the chunk
        tmp = df.copy() 
        tmp['Id'] = tmp['Id']+1000 # increment the Id by 1000
        tmp.iloc[0:10] = np.round(tmp.iloc[0:10] )

#          print(tmp.head())
        writer.write_dataframe(tmp)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# for some of the IDs we want to replace the content
# for i in range(5):

# #    tmp = dummy_data[dummy_data['Id'] == i] * i
#     tmp = np.round(dummy_data[dummy_data['Id'] == i] * (i+1000))

#     with dataiku.Dataset("test").get_writer() as writer:

#         for (origin,count) in tmp.items():
#             print(count)

#             writer.write_row_array((origin,count))