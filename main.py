import streamlit as st
import xarray as xr
import pandas as pd

st.title("ERA5 NGCM Data Analysis")

# ERA5 Data used for eval/training
neuralData = xr.open_zarr('gs://gcp-public-data-arco-era5/ar/full_37-1h-0p25deg-chunk-1.zarr-v3')
st.subheader("ERA5 Data Used for NGCM Training Summary")
st.write(neuralData)

# Accessing the 2m Temp data
tempDATA = neuralData['2m_temperature']
st.subheader("Summary of 2m Temperature Data")
st.write(tempDATA)

# Specify the target latitude, longitude, and time values
lat_values = [40.0, 40.25]  # example latitudes
lon_values = [0.0, 0.25]    # example longitudes
time_values = pd.date_range(start='2023-01-01T00:00:00', periods=20, freq='H')  # example times

# Extract the subset of data
temp_subset = tempDATA.sel(
    latitude=lat_values,
    longitude=lon_values,
    time=time_values,
    method='nearest'
)

# Convert the DataArray to a Pandas DataFrame
df = temp_subset.to_dataframe().reset_index()

# Display the DataFrame
st.subheader("Condensed 2m Temperature Table")
st.write(df)
