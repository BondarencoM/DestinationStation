import pandas as pd

# this dictonary is for documentation reasons
column_names_dict = {
    '# STN': 'StationCode',
    'YYYYMMDD': 'Timestamp',  # date (YYYY=year,MM=month,DD=day)
    'HH': 'Hour',  # time (HH uur/hour, UT. 12 UT=13 MET, 14 MEZT. Hourly division 05 runs from 04.00 UT to 5.00 UT
    'DD': 'WindDir',  # Mean wind direction (in degrees) during the 10-minute period preceding the time of observation (360=north, 90=east, 180=south, 270=west, 0=calm 990=variable)
    'FH': 'WindHour',  # Hourly mean wind speed (in 0.1 m/s)
    'FF': 'WindSpeed', # Mean wind speed (in 0.1 m/s) during the 10-minute period preceding the time of observation  
    'FX': 'MaxWindSpeed',  # Maximum wind gust (in 0.1 m/s) during the hourly division
    'T': 'Temperature',  # Temperature (in 0.1 degrees Celsius) at 1.50 m at the time of observation  
    'T10N': 'MinTemp10M',  # Minimum temperature (in 0.1 degrees Celsius) at 0.1 m in the preceding 6-hour period
    'TD': 'DewPointTemp',  # Dew point temperature (in 0.1 degrees Celsius) at 1.50 m at the time of observation 
    'SQ': 'SunshineDur',  # Sunshine duration (in 0.1 hour) during the hourly division, calculated from global radiation (-1 for <0.05 hour) 
    'Q': 'Radiation',  # Global radiation (in J/cm2) during the hourly division   
    'DR': 'PrecipDur',  # Precipitation duration (in 0.1 hour) during the hourly division
    'RH': 'PrecipHour',  # Hourly precipitation amount (in 0.1 mm) (-1 for <0.05 mm)
    'P': 'AirPressure',  # Air pressure (in 0.1 hPa) reduced to mean sea level, at the time of observation 
    'VV': 'Visibility',  # Horizontal visibility at the time of observation (0=less than 100m, 1=100-200m, 2=200-300m,..., 49=4900-5000m, 50=5-6km, 56=6-7km, 57=7-8km, ..., 79=29-30km, 80=30-35km, 81=35-40km,..., 89=more than 70km)
    'N': 'Cloudines',  # Cloud cover (in octants), at the time of observation (9=sky invisible)
    'U': 'Humidity',  # Relative atmospheric humidity (in percents) at 1.50 m at the time of observation
    'WW': 'WeatherCode',  # Present weather code (00-99), description for the hourly division. (http://bibliotheek.knmi.nl/scholierenpdf/weercodes_Nederland)
    'IX': 'WeatherCodeIndicator',  # Indicator present weather code (1=manned and recorded (using code from visual observations), 2,3=manned and omitted (no significant weather phenomenon to report, not available), 4=automatically recorded (using code from visual observations), 5,6=automatically omitted (no significant weather phenomenon to report, not available), 7=automatically set (using code from automated observations) 
    'M': 'Fog',  # Fog 0=no occurrence, 1=occurred during the preceding hour and/or at the time of observation
    'R': 'Rain',  # Rainfall 0=no occurrence, 1=occurred during the preceding hour and/or at the time of observation
    'S': 'Snow',  # Snow 0=no occurrence, 1=occurred during the preceding hour and/or at the time of observation
    'O': 'Thunder',  # Thunder  0=no occurrence, 1=occurred during the preceding hour and/or at the time of observation 
    'Y': 'IceFormation'  # Ice formation 0=no occurrence, 1=occurred during the preceding hour and/or at the time of observation
}

column_names_list = [
    'StationCode',
    'Timestamp',  # date (YYYY=year,MM=month,DD=day)
    'Hour',  # time (HH uur/hour, UT. 12 UT=13 MET, 14 MEZT. Hourly division 05 runs from 04.00 UT to 5.00 UT
    'WindDir',  # Mean wind direction (in degrees) during the 10-minute period preceding the time of observation (360=north, 90=east, 180=south, 270=west, 0=calm 990=variable)
    'WindHour',  # Hourly mean wind speed (in 0.1 m/s)
    'WindSpeed', # Mean wind speed (in 0.1 m/s) during the 10-minute period preceding the time of observation  
    'MaxWindSpeed',  # Maximum wind gust (in 0.1 m/s) during the hourly division
    'Temperature',  # Temperature (in 0.1 degrees Celsius) at 1.50 m at the time of observation  
    'MinTemp10M',  # Minimum temperature (in 0.1 degrees Celsius) at 0.1 m in the preceding 6-hour period
    'DewPointTemp',  # Dew point temperature (in 0.1 degrees Celsius) at 1.50 m at the time of observation 
    'SunshineDur',  # Sunshine duration (in 0.1 hour) during the hourly division, calculated from global radiation (-1 for <0.05 hour) 
    'Radiation',  # Global radiation (in J/cm2) during the hourly division   
    'PrecipDur',  # Precipitation duration (in 0.1 hour) during the hourly division
    'PrecipHour',  # Hourly precipitation amount (in 0.1 mm) (-1 for <0.05 mm)
    'AirPressure',  # Air pressure (in 0.1 hPa) reduced to mean sea level, at the time of observation 
    'Visibility',  # Horizontal visibility at the time of observation (0=less than 100m, 1=100-200m, 2=200-300m,..., 49=4900-5000m, 50=5-6km, 56=6-7km, 57=7-8km, ..., 79=29-30km, 80=30-35km, 81=35-40km,..., 89=more than 70km)
    'Cloudines',  # Cloud cover (in octants), at the time of observation (9=sky invisible)
    'Humidity',  # Relative atmospheric humidity (in percents) at 1.50 m at the time of observation
    'WeatherCode',  # Present weather code (00-99), description for the hourly division. (http://bibliotheek.knmi.nl/scholierenpdf/weercodes_Nederland)
    'WeatherCodeIndicator',  # Indicator present weather code (1=manned and recorded (using code from visual observations), 2,3=manned and omitted (no significant weather phenomenon to report, not available), 4=automatically recorded (using code from visual observations), 5,6=automatically omitted (no significant weather phenomenon to report, not available), 7=automatically set (using code from automated observations) 
    'Fog',  # Fog 0=no occurrence, 1=occurred during the preceding hour and/or at the time of observation
    'Rain',  # Rainfall 0=no occurrence, 1=occurred during the preceding hour and/or at the time of observation
    'Snow',  # Snow 0=no occurrence, 1=occurred during the preceding hour and/or at the time of observation
    'Thunder',  # Thunder  0=no occurrence, 1=occurred during the preceding hour and/or at the time of observation 
    'IceFormation'  # Ice formation 0=no occurrence, 1=occurred during the preceding hour and/or at the time of observation
]

df_bilt = pd.read_csv('./assets/original_dataset/de_bilt_weather_raw.txt',
                        na_values='     ', 
                        header=28, 
                        parse_dates=['YYYYMMDD']).rename(columns=str.strip)

df_schiphol = pd.read_csv('./assets/original_dataset/schiphol_weather_raw.txt',
                        na_values='     ', 
                        header=28, 
                        parse_dates=['YYYYMMDD']).rename(columns=str.strip)

print(df_bilt.head())
print(df_bilt.shape)
print()
print(df_schiphol.head())
print(df_schiphol.shape)

# rename column name to more descriptive ones
df_bilt.columns = column_names_list
df_schiphol.columns = column_names_list

# devide column values by 10
column_div = ['WindHour', 'WindSpeed', 'MaxWindSpeed', 
            'Temperature', 'MinTemp10M', 'DewPointTemp', 
            'SunshineDur', 'PrecipDur', 'PrecipHour', 
            'AirPressure'
        ]
df_bilt[column_div] = df_bilt[column_div] / 10
df_schiphol[column_div] = df_schiphol[column_div] / 10

print(df_bilt.head())
print()
print(df_schiphol.head())


# filter the out 2016
df_bilt_2016 = df_bilt.loc[(df_bilt['Timestamp'] >= '2016-01-01') & (df_bilt['Timestamp'] <= '2016-12-07')]
df_schiphol_2016 = df_schiphol.loc[(df_schiphol['Timestamp'] >= '2016-01-01') & (df_schiphol['Timestamp'] <= '2016-12-07')]

print(df_bilt_2016.shape)
print(df_schiphol_2016.shape)

# save dataset
df_bilt_2016.to_csv('./assets/data/de_bilt_weather_2016.csv', index=False, mode='w')
df_schiphol_2016.to_csv('./assets/data/schiphol_weather_2016.csv', index=False, mode='w')


