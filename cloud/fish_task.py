# %%
import boto3
import json
import pandas as pd
from io import StringIO
from pprint import pprint

s3_client = boto3.client('s3') # lower level service
s3_resource = boto3.resource('s3')

bucket_name = 'data-eng-resources'

# %%
csv_obj1 = s3_client.get_object(Bucket=bucket_name, Key='python/fish-market.csv')
df1 = pd.read_csv(csv_obj1.get("Body"))

# %%
df_spec_avg1 = df1.groupby('Species').mean().round(2)

print(df_spec_avg1)
# %%
csv_obj2 = s3_client.get_object(Bucket=bucket_name, Key='python/fish-market-mon.csv')
df2 = pd.read_csv(csv_obj2.get("Body"))

# %%
df_spec_avg2 = df2.groupby('Species').mean().round(2)

print(df_spec_avg2)
# %%
csv_obj3 = s3_client.get_object(Bucket=bucket_name, Key='python/fish-market-tues.csv')
df3 = pd.read_csv(csv_obj3.get("Body"))

# %%
df_spec_avg3 = df3.groupby('Species').mean().round(2)

print(df_spec_avg3)
# %% Combining the three dataframes and performing an average per Species
df = pd.concat([df1, df2, df3], axis=0)
df_avg = df.groupby('Species').mean().round(2)

# %% Upload to s3
csv_buffer = StringIO()
df_avg.to_csv(csv_buffer)

# using resource
s3_resource.Object(bucket_name, 'Data204/fish/FAIZ.csv').put(Body=csv_buffer.getvalue())
# %%
