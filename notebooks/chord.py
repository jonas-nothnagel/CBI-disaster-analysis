#%%
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

import chord as chord
import numpy as np

import holoviews as hv
from holoviews import opts, dim
import holoviews.plotting.bokeh
import panel as pn
# %%
df = pd.read_excel("../data/matrix_v1.xlsm", index_col=None)

#remove non ascii characters
df['Technology'] = df['Technology'].astype(str).str.replace(u'\xa0', '')
df['Use Case'] = df['Use Case'].astype(str).str.replace(u'\xa0', '')

df_tech = df[['Technology']]

df_use = df[['Use Case']]
# %%
#count occurences tech
df_tech['AI'] = df_tech.Technology.str.count('Machine Learning')
df_tech['Drones'] = df_tech.Technology.str.count('Drones')
df_tech['3D_Printing'] = df_tech.Technology.str.count('3D')
df_tech['Communication_Networks'] = df_tech.Technology.str.count('Communication')
df_tech['AR/VR'] = df_tech.Technology.str.count('Augmented')
df_tech['GIS'] = df_tech.Technology.str.count('GIS')
df_tech['Social_Media'] = df_tech.Technology.str.count('Social')
df_tech['Crowdsourcing'] = df_tech.Technology.str.count('Crowdsourcing')
df_tech['Cloud_Computing'] = df_tech.Technology.str.count('Cloud')
df_tech['CPS'] = df_tech.Technology.str.count('Cyber')
df_tech['Blockchain'] = df_tech.Technology.str.count('Blockchain')
df_tech['Remote_Sensing'] = df_tech.Technology.str.count('Remote')
df_tech['IoT'] = df_tech.Technology.str.count('Internet')
#%%
#delete text
del df_tech['Technology']

#construct co_occurence 
df_tech = df_tech.astype(int)
coocc = df_tech.T.dot(df_tech)

#reset diagonal
np.fill_diagonal(coocc.values, 0)
#%%
#count occurences use case

df_use['Disaster Prediction &  EWS'] = df_use['Use Case'].str.count('Early')
df_use['Damage & Loss Assessment'] = df_use['Use Case'].str.count('Loss')
df_use['Search & Rescue'] = df_use['Use Case'].str.count('Search')
df_use['Event Simulations'] = df_use['Use Case'].str.count('Event')
df_use['Disaster Detection'] = df_use['Use Case'].str.count('Detection')
df_use['Situational Awareness & AIG'] = df_use['Use Case'].str.count('Gathering')
df_use['Disaster Relief & Resource Allocation'] = df_use['Use Case'].str.count('Resource')
df_use['Emergency Communication'] = df_use['Use Case'].str.count('Communication')

del df_use['Use Case']
#construct co_occurence 
#%%
df_use = df_use.astype(int)
coocc = df_use.T.dot(df_use)

#reset diagonal
np.fill_diagonal(coocc.values, 0)
# %%
# Declare a gridded HoloViews dataset and call dframe to flatten it
hv.extension('bokeh')
hv.output(size=200)

data = hv.Dataset((list(coocc.columns), list(coocc.index), coocc),
                  ['source', 'target'], 'value').dframe()

# Now create your Chord diagram from the flattened data
chord = hv.Chord(data)

chord.opts(
    node_color='index', edge_color='source', label_index='index',  
    cmap='Category10', edge_cmap='Category10', width=400, height=400)
# %%



# %%
