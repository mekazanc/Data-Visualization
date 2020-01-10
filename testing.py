di_acc = pd.read_csv('C:\\Users\mehmet.kazanc\\Desktop\\Hotspot_Analysis.csv', dtype=object)
# ANKARA
#map_hooray = folium.Map(location=[39.925533, 32.866287],
#                        zoom_start = 9)
# İSTANBUL    
map_hooray = folium.Map(location=[41.015137, 28.979530],
                        zoom_start = 9)    
    
map_hooray # Calls the map to display
 


# Ensure you're handing it floats
di_acc['userCentroidLocation_latitude'] = di_acc['userCentroidLocation_latitude'].astype(float)
di_acc['userCentroidLocation_longitude'] = di_acc['userCentroidLocation_longitude'].astype(float)


# Filter the DF for rows, then columns, then remove NaNs
di_acc = di_acc.loc[(di_acc['user_type'] == 'All')]
di_acc = di_acc.loc[(di_acc['reportDate'] == '2018-10-25')]
di_acc = di_acc.loc[(di_acc['loc_detail'] == 'ISTIKLAL_CAD_ISTANBUL')]


heat_dff = di_acc

heat_dff = heat_dff[['userCentroidLocation_latitude', 'userCentroidLocation_longitude']]
heat_dff['signalLinearPowerMeanDbmRelative_rank'] = di_acc['signalLinearPowerMeanDbmRelative_rank']

heat_dff = heat_dff.dropna(axis=0, subset=['userCentroidLocation_latitude','userCentroidLocation_longitude'])

 
# List comprehension to make out list of lists
heatt_data = [[row['userCentroidLocation_latitude'],row['userCentroidLocation_longitude']] for index, row in heat_dff.iterrows()]



for index, row in heat_dff.iterrows():
 if row['signalLinearPowerMeanDbmRelative_rank'] == '1.0':     
  folium.Marker([row['userCentroidLocation_latitude'],row['userCentroidLocation_longitude']], 
                popup='East London',
                icon=folium.Icon(color='green',icon='arrow-circle-up', prefix='fa') 
                ).add_to(map_hooray)

 elif row['signalLinearPowerMeanDbmRelative_rank'] == '2.0':    
    folium.Marker([row['userCentroidLocation_latitude'],row['userCentroidLocation_longitude']], 
                popup='East London',
                icon=folium.Icon(color='orange',icon='arrow-circle-right', prefix='fa') 
                ).add_to(map_hooray)
 else:   
    folium.Marker([row['userCentroidLocation_latitude'],row['userCentroidLocation_longitude']], 
                popup='East London',
                icon=folium.Icon(color='red',icon='arrow-circle-down', prefix='fa') 
                ).add_to(map_hooray)

#arrow-circle-down
#arrow-circle-right
 
# Display the map
map_hooray
