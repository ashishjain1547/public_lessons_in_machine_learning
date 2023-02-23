import cartopy
import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
from cartopy.feature import LAND

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from datetime import datetime

# Setting the color to shade the countries.
cmap = mpl.cm.Greys # Other color: mpl.cm.Blues

countries = {
    "India": 49,
    "United States": 48,
    "United Arab Emirates": 47,
    "Germany": 46,
    "Singapore": 45,
    "United Kingdom": 44,
    "Russian Federation": 43,
    "Ukraine":42,              
    "Netherlands": 41,
    "Hong Kong": 40,
    "Canada": 39,
    "France": 38,
    "Oman": 37,
    "Australia": 36,
    "Pakistan": 35,
    "Kenya": 34,
    "Malaysia": 33,
    "Saudi Arabia": 32,
    "Turkey": 31,
    "Spain": 30, 
    "Nepal": 29,
    "Qatar": 28,
    "Kuwait": 27,
    "Indonesia": 26,
    "Italy": 25,
    "Sweden": 24,
    "Portugal": 23,
    "Mauritius": 22,
    "New Zealand": 21,
    "Japan": 20,
    "Republic of Korea": 21, # South Korea
    "Barbados": 20, # Not listed in cartopy package
    "Brazil": 19,
    "China": 18,
    "Greece": 17,
    "Poland": 16,
    "Czech Republic": 15,
    "Kazakhstan": 14,
    "Latvia": 13,
    "Ireland": 12,
    "Finland": 11,
    "Peru": 10
}


max_users = float(max(countries.values()))
shapename = 'admin_0_countries'
countries_shp = shpreader.natural_earth(resolution='110m', category='cultural', name=shapename)
ax = plt.axes(projection=ccrs.Robinson())

for country in shpreader.Reader(countries_shp).records():
    name = country.attributes['NAME_LONG']
    
    if name in countries:
        num_users = countries[name]
    else:
        num_users = 1
    
    # ax.add_geometries(country.geometry, ccrs.PlateCarree(), facecolor=cmap(num_users/max_users, 1))
    # TypeError: 'Polygon' object is not iterable
    # name: Fiji, type(country.geometry): <class 'shapely.geometry.multipolygon.MultiPolygon'>
    # name: Tanzania, type(country.geometry): <class 'shapely.geometry.polygon.Polygon'>
    
    try:
        ax.add_geometries(country.geometry, ccrs.PlateCarree(), facecolor=cmap(num_users/max_users, 1))
    except Exception as e:
        #print(e)
        import shapely.wkt as wkt
        from shapely.geometry import MultiPolygon

        list_str_polygons = [str(country.geometry)]

        c = MultiPolygon(map(wkt.loads, list_str_polygons))
        ax.add_geometries(c, ccrs.PlateCarree(), facecolor=cmap(num_users/max_users, 1))

    ax.add_feature(cartopy.feature.OCEAN, color='lightblue')

#Save the image as a file.
plt.savefig('Audience ' + str(datetime.now()).replace(':', '_') + '.png', transparent=True, dpi=900)  
print("Done")


"""Listed on 20201022:
Fiji
Tanzania
Western Sahara
Canada
United States
Kazakhstan
Uzbekistan
Papua New Guinea
Indonesia
Argentina
Chile
Democratic Republic of the Congo
Somalia
Kenya
Sudan
Chad
Haiti
Dominican Republic
Russian Federation
Bahamas
Falkland Islands
Norway
Greenland
French Southern and Antarctic Lands
Timor-Leste
South Africa
Lesotho
Mexico
Uruguay
Brazil
Bolivia
Peru
Colombia
Panama
Costa Rica
Nicaragua
Honduras
El Salvador
Guatemala
Belize
Venezuela
Guyana
Suriname
France
Ecuador
Puerto Rico
Jamaica
Cuba
Zimbabwe
Botswana
Namibia
Senegal
Mali
Mauritania
Benin
Niger
Nigeria
Cameroon
Togo
Ghana
Côte d'Ivoire
Guinea
Guinea-Bissau
Liberia
Sierra Leone
Burkina Faso
Central African Republic
Republic of the Congo
Gabon
Equatorial Guinea
Zambia
Malawi
Mozambique
eSwatini
Angola
Burundi
Israel
Lebanon
Madagascar
Palestine
The Gambia
Tunisia
Algeria
Jordan
United Arab Emirates
Qatar
Kuwait
Iraq
Oman
Vanuatu
Cambodia
Thailand
Lao PDR
Myanmar
Vietnam
Dem. Rep. Korea
Republic of Korea
Mongolia
India
Bangladesh
Bhutan
Nepal
Pakistan
Afghanistan
Tajikistan
Kyrgyzstan
Turkmenistan
Iran
Syria
Armenia
Sweden
Belarus
Ukraine
Poland
Austria
Hungary
Moldova
Romania
Lithuania
Latvia
Estonia
Germany
Bulgaria
Greece
Turkey
Albania
Croatia
Switzerland
Luxembourg
Belgium
Netherlands
Portugal
Spain
Ireland
New Caledonia
Solomon Islands
New Zealand
Australia
Sri Lanka
China
Taiwan
Italy
Denmark
United Kingdom
Iceland
Azerbaijan
Georgia
Philippines
Malaysia
Brunei Darussalam
Slovenia
Finland
Slovakia
Czech Republic
Eritrea
Japan
Paraguay
Yemen
Saudi Arabia
Antarctica
Northern Cyprus
Cyprus
Morocco
Egypt
Libya
Ethiopia
Djibouti
Somaliland
Uganda
Rwanda
Bosnia and Herzegovina
Macedonia
Serbia
Montenegro
Kosovo
Trinidad and Tobago
South Sudan
"""