# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu



dummy_data = pd.DataFrame(np.random.rand(100, 10))
dummy_data['Id'] = list(range(10))*10

input_df = dummy_data


# Write recipe outputs
input = dataiku.Dataset("input")
input.write_with_schema(input_df)
