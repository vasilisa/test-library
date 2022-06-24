# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu


# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs and take the input schema to output dataset

inp = dataiku.Dataset("input")
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
