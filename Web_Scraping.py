#!/usr/bin/env python
# coding: utf-8

# Installing Web scraping module

# Reading in Web contents

# In[21]:


import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'
dfs = pd.read_html(url)

print(len(dfs))


# In[ ]:


df_data_1


# In[46]:



# @hidden_cell
# The following code contains the credentials for a file in your IBM Cloud Object Storage.
# You might want to remove those credentials before you share your notebook.
credentials_1 = {
    'IAM_SERVICE_ID': 'iam-ServiceId-f0aae712-76b7-460d-94af-173468b5a646',
    'IBM_API_KEY_ID': 'tLvcSB91BCmKD_c3SMR9lXOsE3QvmWxkoBxo6pDvKXbU',
    'ENDPOINT': 'https://s3.eu-geo.objectstorage.service.networklayer.com',
    'IBM_AUTH_ENDPOINT': 'https://iam.cloud.ibm.com/oidc/token',
    'BUCKET': 'applieddatasciencew3-donotdelete-pr-gotyt0eqrdb6i6',
    'FILE': 'Toronto_main.csv'
}


# In[47]:



import types
import pandas as pd
from botocore.client import Config
import ibm_boto3

def __iter__(self): return 0

# @hidden_cell
# The following code accesses a file in your IBM Cloud Object Storage. It includes your credentials.
# You might want to remove those credentials before you share the notebook.
client_7a1d4d3d3fd943d1b132ed48dd066a72 = ibm_boto3.client(service_name='s3',
    ibm_api_key_id='tLvcSB91BCmKD_c3SMR9lXOsE3QvmWxkoBxo6pDvKXbU',
    ibm_auth_endpoint="https://iam.cloud.ibm.com/oidc/token",
    config=Config(signature_version='oauth'),
    endpoint_url='https://s3.eu-geo.objectstorage.service.networklayer.com')

body = client_7a1d4d3d3fd943d1b132ed48dd066a72.get_object(Bucket='applieddatasciencew3-donotdelete-pr-gotyt0eqrdb6i6',Key='Toronto_main.csv')['Body']
# add missing __iter__ method, so pandas accepts body as file-like object
if not hasattr(body, "__iter__"): body.__iter__ = types.MethodType( __iter__, body )

#pd.options.display.width=None
df_data_1 = pd.read_csv(body, delimiter = ';',error_bad_lines=False)
pd.options.display.max_columns = None
df_data_1.head()


# In[58]:


df_data_1 = df_data_1.drop('Postal Code.1', axis=1)


# In[61]:



left_2 = df_data_1.style.set_properties(**{'text-align': 'left'}).set_table_styles([ dict(selector='th', props=[('text-align', 'left')] ) ])
display(left_2 ) 


# In[48]:


df_data_1.shape


# In[ ]:


import geocoder # import geocoder

# initialize your variable to None
lat_lng_coords = None

# loop until you get the coordinates
while(lat_lng_coords is None):
  g = geocoder.google('{}, Toronto, Ontario'.format(postal_code))
  lat_lng_coords = g.latlng

latitude = lat_lng_coords[0]
longitude = lat_lng_coords[1]

