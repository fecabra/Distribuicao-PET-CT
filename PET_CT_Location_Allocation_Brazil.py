#upload necessary libraries
from arcgis.gis import GIS
import arcgis.network as network
from arcgis.features import FeatureLayer, Feature, FeatureSet, FeatureCollection, find_locations
import pandas as pd
import time
import datetime as dt

#import databese of Brazilian Cities
cidades_total = pd.read_csv(r"~\cidades_total.csv")
cidades_total.head()

#choose states involved in the analisys, only uncomment depending on the region to be analized
#code for Centro_norte
##cidades_total_Centro_Norte=cidades_total.query('sigla=="AM" or sigla=="AC" or sigla=="AP" or sigla=="DF" or sigla=="GO" or sigla=="MS" or sigla=="PA" or sigla=="MT" or sigla=="RR" or sigla=="TO"') 
##cidades_total_Centro_Norte.head()
#code for Sul
##cidades_total_Sul=cidades_total.query('sigla=="SC" or sigla=="PR" or sigla=="RS"') 
##cidades_total_Sul.head()
#code for Sudeste without SP
##cidades_total_Sudeste=cidades_total.query('sigla=="RJ" or sigla=="ES" or sigla=="MG"') 
##cidades_total_Sudeste.head()
#code for Nordeste
##cidades_total_Nordeste=cidades_total.query('sigla=="BA" or sigla=="MA" or sigla=="PI" or sigla=="PB" or sigla=="PB" or sigla=="RN" or sigla=="AL" or sigla=="SE" or sigla=="CE"') 
##cidades_total_Nordeste.head()
#code for SP
cidades_total_SP=cidades_total.query('sigla=="SP"') 
cidades_total_SP.head()

#Filter cities with an existing PET-CT
#cities from SP with an exinting PET-CT, uncomment the code denpending on the region to be analized
filter4 = cidades_total_SP.query('cidade=="São Paulo"  or cidade== "Campinas" or cidade=="Ribeirão Preto" or cidade== "Presidente Prudente" or cidade== "Sorocaba" or cidade== "Barretos"')
##filter4 = cidades_total_Centro_Norte.query('cidade=="Sinop"  or cidade== "Goiânia" or cidade== "Brasília" or cidade== "Manaus" or cidade== "Campo Grande" or cidade== "Belém" or cidade== "Brasnorte"')
##filter4 = cidades_total_Sudeste.query('cidade=="Rio de Janeiro" or cidade== "Belo Horizonte" or cidade== "Pouso Alegre" or cidade== "Montes Claros" or cidade=="Passa Quatro"')
##filter4 = cidades_total_Nordeste.query('cidade=="Salvador" or cidade== "Caruaru"  or cidade== "Aracaju" or cidade== "João Pessoa" or cidade=="Natal" or cidade=="São Luís" or cidade=="Recife" or cidade== "Imperatriz" or cidade== "Teresina"')
##filter4 = cidades_total_Sul.query('cidade=="Curitiba"  or cidade== "Criciúma" or cidade== "Brusque" or cidade=="Maravilha" or cidade== "Itajaí" or cidade== "Porto Alegre" or cidade== "Tubarão" or cidade== "Caxias do Sul" or cidade== "Londrina" or cidade== "Passo Fundo"')
#Drop  the cities with an exinting PET-CT from the candidate cities to receive a new PET-CT
cidades_candidates_SP = cidades_total_SP.drop(filter4.index, axis=0)
##cidades_candidates_Centro_Norte = cidades_total_Centro_Norte.drop(filter4.index, axis=0)
##cidades_candidates_Sudeste = cidades_total_Sudeste.drop(filter4.index, axis=0)
##cidades_candidates_Nordeste = cidades_total_Nordeste.drop(filter4.index, axis=0)
##cidades_candidates_Sul = cidades_total_Sul.drop(filter4.index, axis=0)
#filter the candidate cities acc. to the population, > 50T or 100T inhabitants
filter1 = cidades_candidates_SP[cidades_total['populacao'] < 50000 ]
cidades_candidates_SP=cidades_candidates_SP.drop(filter1.index, axis=0)
##filter1 = cidades_candidates_Centro_Norte[cidades_total['populacao'] < 10000 ]
##cidades_candidates_Centro_Norte=cidades_candidates_Centro_Norte.drop(filter1.index, axis=0)
##filter1 = cidades_candidates_Sudeste[cidades_total['populacao'] < 10000 ]
##cidades_candidates_Sudeste=cidades_candidates_Sudeste.drop(filter1.index, axis=0)
##filter1 = cidades_candidates_Nordeste[cidades_total['populacao'] < 10000 ]
##cidades_candidates_Nordeste=cidades_candidates_Nordeste.drop(filter1.index, axis=0)
##filter1 = cidades_candidates_Sul[cidades_total['populacao'] < 10000 ]
##cidades_candidates_Sul=cidades_candidates_Sul.drop(filter1.index, axis=0)

#Save csv candidate cities, , uncomment the code denpending on the region to be analized
cidades_candidates_SP.to_csv(r"~\cidades_candidates_SP.csv", index=False, sep=",",encoding='latin1')
#cidades_candidates_Centro_Norte.to_csv(r"~\cidades_candidates_Centro_Norte.csv", index=False, sep=",",encoding='latin1')
#cidades_candidates_Sudeste.to_csv(r"~\cidades_candidates_Sudeste.csv", index=False, sep=",",encoding='latin1')
#cidades_candidates_Nordeste.to_csv(r"~\cidades_candidates_Nordeste.csv", index=False, sep=",",encoding='latin1')
#cidades_candidates_Sul.to_csv(r"~\cidades_candidates_Sul.csv", index=False, sep=",",encoding='latin1')

#choose the cities to demand a PET-CT, uncomment the code denpending on the region to be analized
cidades_demand_SP=cidades_total_SP
##cidades_demand_Centro_Norte=cidades_total_Centro_Norte
##cidades_demand_Sudeste=cidades_total_Sudeste
##cidades_demand_Nordeste=cidades_total_Nordeste
##cidades_demand_Sul=cidades_total_Sul

#Save csv demand cities
cidades_demand_SP.to_csv(r"~\cidades_demand_SP.csv", index=False, sep=",",encoding='latin1')
#cidades_demand_Centro_Norte.to_csv(r"~\cidades_demand_Centro_Norte.csv", index=False, sep=",",encoding='latin1')
#cidades_demand_Sudeste.to_csv(r"~\cidades_demand_Sudeste.csv", index=False, sep=",",encoding='latin1')
#cidades_demand_Nordeste.to_csv(r"~\cidades_demand_Nordeste.csv", index=False, sep=",",encoding='latin1')
#cidades_demand_Sul.to_csv(r"~\cidades_demand_Sul.csv", index=False, sep=",",encoding='latin1')

## filter cidades_existing, uncomment the code denpending on the region to be analized
cidades_existing_SP= filter4
cidades_existing=cidades_existing_SP.reset_index(drop=True)
cidades_existing_SP.head(11)
##cidades_existing_Centro_Norte= filter4
##cidades_existing=cidades_existing_Centro_Norte.reset_index(drop=True)
##cidades_existing_Centro_Norte.head(11)
##cidades_existing_Sudeste= filter4
##cidades_existing=cidades_existing_Sudeste.reset_index(drop=True)
##cidades_existing_Sudeste.head(11)
##cidades_existing_Nordeste= filter4
##cidades_existing=cidades_existing_Nordeste.reset_index(drop=True)
##cidades_existing_Nordeste.head(11)
##cidades_existing_Sul= filter4
##cidades_existing=cidades_existing_Sul.reset_index(drop=True)
##cidades_existing_Sul.head(11)

#Save csv demand cities
cidades_existing_SP.to_csv(r"~\cidades_existing_SP.csv", index=False, sep=",",encoding='latin1')
##cidades_existing_Centro_Norte.to_csv(r"~\cidades_existing_Centro_Norte.csv", index=False, sep=",",encoding='latin1')
##cidades_existing_Sudeste.to_csv(r"~\cidades_existing_Sudeste.csv", index=False, sep=",",encoding='latin1')
##cidades_existing_Nordeste.to_csv(r"~\cidades_existing_Nordeste.csv", index=False, sep=",",encoding='latin1')
##cidades_existing_Sul.to_csv(r"~\cidades_existing_Sul.csv", index=False, sep=",",encoding='latin1')

my_gis = GIS('home')

#Configure candidate cities layer, necessary publish in ArcGis Portal

import requests
import csv
import os

csv_file = r"~\cidades_candidates_SP.csv" #path to CSV
##csv_file = r"~\cidades_candidates_Centro_Norte.csv" #path to CSV
##csv_file = r"~\cidades_candidates_Sudeste.csv" #path to CSV
##csv_file = r"~\cidades_candidates_Nordeste.csv" #path to CSV
##csv_file = r"~\cidades_candidates_Sul.csv" #path to CSV

csv_item = my_gis.content.add({}, csv_file) #add CSV to Enterprise Portal
display(csv_item) #display it here 

#Configure candidate cities layer, necessary publish in ArcGis Portal
#edit visualization un the portal with yellow points, size 7
csv_file1 = r"~\cidades_demand_SP.csv" #path to CSV
##csv_file1 = r"~\cidades_demand_Centro_Norte.csv" #path to CSV
##csv_file1 = r"~\cidades_demand_Sudeste.csv" #path to CSV
##csv_file1 = r"~\cidades_demand_Nordeste.csv" #path to CSV
##csv_file1 = r"~\cidades_demand_Sul.csv" #path to CSV
csv_item1 = my_gis.content.add({}, csv_file1) #add CSV to Enterprise Portal
display(csv_item1) #display it here 

#Configure existing cities layer, necessary publish in ArcGis Portal
#edit visualization in the portal the image from url https://static.arcgis.com/images/Symbols/Basic/BlueShinyPin.png
csv_file2 = r"~\cidades_existing_SP.csv" #path to CSV
##csv_file2 = r"~\cidades_existing_Centro_Norte.csv" #path to CSV
##csv_file2 = r"~\cidades_existing_Sudeste.csv" #path to CSV
##csv_file2 = r"~\cidades_existing_Nordeste.csv" #path to CSV
##csv_file2 = r"~\cidades_existing_Sul.csv" #path to CSV
csv_item2 = my_gis.content.add({}, csv_file2) #add CSV to Enterprise Portal
display(csv_item2)

#get the layer candidates key from the url link in layer overview in the portal
candidates= my_gis.content.get('48685362fde54c81a21f41a3710a568b')

#get the layer demand key from the url view link in layer overview in the portal
demand=my_gis.content.get('5fe6bb41449045d6ac9320524ae52784')

#get the layer existing key from the url view link in layer overview in the portal
existing= my_gis.content.get('98c3bb066b41420e9acb2114e146a477')

#show the Brazilian map in dark-gray colors
map1 = my_gis.map("Brazil")
map1.basemap = 'dark-gray'
map1

#add the layers to the map
map1.add_layer(demand)
map1.add_layer(candidates)
map1.add_layer(existing)

#confirm the layers added
for lyr in map1.layers:
    print(lyr.properties.name)

#confirm the number of demand points
demand_points_fl = map1.layers[0]
try:
    demand_points = demand_points_fl.query(where="1=1", as_df=False)
    display(demand_points)
except RuntimeError as re:
    print("Query failed.")

#confirm the number of candidate points
candidate_fl = map1.layers[1]
try:
    candidate_facilities = candidate_fl.query(where="1=1", as_df=False)
    display(candidate_facilities)
except RuntimeError as re:
    print("Query failed.")

#confirm the number of existing points
existing_fl = map1.layers[2]
try:
    required_facilities = existing_fl.query(where="1=1", as_df=False)
    display(required_facilities)
except RuntimeError as re:
    print("Query failed.")

#set caditates facicilities with type 0, it will be considered by the solver
object_id_count = 0

for f in candidate_facilities:
    object_id_count+=1
    f.attributes.update({"FacilityType":0})
    print(f.attributes)

#set existinting/required facicilities with type 1, it will be considered by the solver
for f in required_facilities:
    object_id_count+=1
    f.attributes.update({"FacilityType":1, "OBJECTID":object_id_count})
    print(f.attributes)

#confirm the number of possible locations to be choosen
facilities_flist = []

for ea in candidate_facilities:
    facilities_flist.append(ea)

for ea in required_facilities:
    facilities_flist.append(ea)

facilities = FeatureSet(facilities_flist)
display(facilities)

#consider the population as a weight for the decision
for f in demand_points:
    tmp = f.get_value("populacao")
    f.attributes.update({"Weight":tmp})

#Run the solver in order to give the location allocation results, in this work were setted up: 
#problem_type='Maximize Coverage' (MCLP) or problem_type='Maximize Attendance'
#number_of_facilities_to_find= depending on the region to be analized, respecting the share 500T inhabitants/equipment
#impedance="Travel Distance"
#measurement_units='Kilometers',
#default_measurement_cutoff=100
#Maximaxe with a maximal travel distance from demmand point of 100 kilometrs

%%time
result1 = network.analysis.solve_location_allocation(   problem_type='Maximize Coverage',
                                                        travel_direction='Demand to Facility',
                                                        number_of_facilities_to_find='75',
                                                        measurement_transformation_model="Linear",
                                                        measurement_transformation_factor=2,
                                                        demand_points=demand_points,
                                                        facilities=candidate_facilities,
                                                        impedance="Travel Distance",
                                                        measurement_units='Kilometers',
                                                        default_measurement_cutoff=100
                                                    )
print('Analysis succeeded? {}'.format(result1.solve_succeeded))

# Display the analysis results in a pandas dataframe.
result1.output_facilities.sdf[['Name', 'FacilityType','Weight','DemandCount', 'DemandWeight']]

# Import the ArcGIS API for Python
from arcgis import *
from IPython.display import display
import numpy as np

# Define a function to display the output analysis results in a map
def visualize_locate_allocate_results(map_widget, solve_locate_allocate_result, zoom_level):
    # The map widget
    m = map_widget
    # The locate-allocate analysis result
    result1 = solve_locate_allocate_result
    
    # 1. Parse the locate-allocate analysis results
    # Extract the output data from the analysis results
    # Store the output points and lines in pandas dataframes
    demand_df = result1.output_demand_points.sdf
    lines_df = result1.output_allocation_lines.sdf

    # Extract the allocated demand points (pop) data.
    demand_allocated_df = demand_df[demand_df['DemandOID'].isin(lines_df['DemandOID'])]
    demand_allocated_fset = features.FeatureSet.from_dataframe(demand_allocated_df)
    display(demand_allocated_df.head())

    # Extract the un-allocated demand points (pop) data.
    demand_not_allocated_df = demand_df[~demand_df['DemandOID'].isin(lines_df['DemandOID'])]
    demand_not_allocated_df['AllocatedWeight'] = demand_not_allocated_df['AllocatedWeight'].replace(np.nan, 0)
    demand_not_allocated_df['FacilityOID'] = demand_not_allocated_df['FacilityOID'].replace(np.nan, 0)
    if len(demand_not_allocated_df)>0:
        display(demand_not_allocated_df.head())
        demand_not_allocated_fset = features.FeatureSet.from_dataframe(demand_not_allocated_df)

    # Extract the chosen facilities (candidate sites) data.
    facilities_df = result1.output_facilities.sdf[['Name', 'FacilityType', 
                                                 'Weight','DemandCount', 'DemandWeight', 'SHAPE']]
    facilities_chosen_df = facilities_df[facilities_df['FacilityType'] == 3]
    facilities_chosen_fset = features.FeatureSet.from_dataframe(facilities_chosen_df)

    # 2. Define the map symbology
    # Allocation lines
    allocation_line_symbol_1 = {'type': 'esriSLS', 'style': 'esriSLSSolid',
                                'color': [255,255,255,153], 'width': 0.7}

    allocation_line_symbol_2 = {'type': 'esriSLS', 'style': 'esriSLSSolid',
                                'color': [0,255,197,39], 'width': 3}

    allocation_line_symbol_3 = {'type': 'esriSLS', 'style': 'esriSLSSolid',
                                'color': [0,197,255,39], 'width': 5}
    
    allocation_line_symbol_4 = {'type': 'esriSLS', 'style': 'esriSLSSolid',
                                'color': [0,92,230,39], 'width': 7}
    
    # Patient points within 90 minutes drive time to a proposed location.
    allocated_demand_symbol = {'type' : 'esriPMS', 'url' : 'https://maps.esri.com/legends/Firefly/cool/1.png',
                               'contentType' : 'image/png', 'width' : 26, 'height' : 26,
                               'angle' : 0, 'xoffset' : 0, 'yoffset' : 0}

    # Patient points outside of a 90 minutes drive time to a proposed location.
    unallocated_demand_symbol = {'type' : 'esriPMS', 'url' : 'https://maps.esri.com/legends/Firefly/warm/1.png',
                                 'contentType' : 'image/png', 'width' : 19.5, 'height' : 19.5,
                                 'angle' : 0, 'xoffset' : 0, 'yoffset' : 0}

    # Selected facilities
    selected_facilities_symbol = {"angle":0,"xoffset":0,"yoffset":0,"type":"esriPMS",
                                  "url":"https://static.arcgis.com/images/Symbols/Basic/GreenShinyPin.png",
                                  "contentType":"image/png","width":20,"height":20, "tranCentro_Nortearency" : 0}
    
    # 3. Display the analysis results in the map
    
    # Zoom out to diCentro_Nortelay all of the allocated census points.
    m.zoom = zoom_level
    
    # Display the locations of pop within the Centro_Norteecified drive time to the selected site(s).
    m.draw(shape=demand_allocated_fset, symbol=allocated_demand_symbol)

    # Display the locations of pop outside the Centro_Norteecified drive time to the selected site(s).
    if len(demand_not_allocated_df)>0:
        m.draw(shape = demand_not_allocated_fset, symbol = unallocated_demand_symbol)

    # Display the chosen site.
    m.draw(shape=facilities_chosen_fset, symbol=selected_facilities_symbol)
    m.draw(shape=result1.output_allocation_lines, symbol=allocation_line_symbol_2)
    m.draw(shape=result1.output_allocation_lines, symbol=allocation_line_symbol_1)

visualize_locate_allocate_results(map1, result1, zoom_level=8)

#creat web map of analysis for that is recommended clean the cache in ArcGIS options -> display, it will be saved on your ArcGIS content
item_properties = {
    "title": "Locatitton Allocation PET_CT",
    "tags" : "Location Allttocation",
    "snippet": "Location Allocttation PET_CT",
    "description": "a web map of Location Allocation PET_CT in Brazil"
}

item = map1.save(item_properties)
print(item)


#save the excel with allocated facilities results
result1.output_facilities.sdf.to_excel(r"C:\Users\Carol\Desktop\TCC Distr. PET CT_100\output_facilities_SP.xlsx")
##result1.output_facilities.sdf.to_excel(r"~\output_facilities_Centro_Norte.xlsx")
##result1.output_facilities.sdf.to_excel(r"~\output_facilities_Sudeste.xlsx")
##result1.output_facilities.sdf.to_excel(r"~\output_facilities_Nordeste.xlsx")
##result1.output_facilities.sdf.to_excel(r"~\output_facilities_Sul.xlsx")

#save the excel with not allocated facilities results
result1.output_demand_points.sdf.to_excel(r"C:\Users\Carol\Desktop\TCC Distr. PET CT_100\output_not_allocated_SP.xlsx")
##result1.output_demand_points.sdf.to_excel(r"~\output_not_allocated_Centro_Norte.xlsx")
##result1.output_demand_points.sdf.to_excel(r"~\output_not_allocated_Sudeste.xlsx")
##result1.output_demand_points.sdf.to_excel(r"~\output_not_allocated_Nordeste.xlsx")
##result1.output_demand_points.sdf.to_excel(r"~\output_not_allocated_Sul.xlsx")

map1
