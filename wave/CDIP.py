import matplotlib.pyplot as plt
import xarray as xr
import pandas as pd
import numpy as np

def load_cdip_data(transect_codes, variable_names, start_date, end_date):
    """
    Loads specified CDIP MOP variables for multiple transects over a time range.

    Parameters:
        transect_codes (list of str): List of transect codes like ['MO921', 'MO897']
        variable_names (list of str): List of variable names like ['waveHs', 'waveSxy', 'waveDm']
        start_date (str or np.datetime64): Start date (e.g., '2025-03-17')
        end_date (str or np.datetime64): End date (e.g., '2025-03-18')

    Returns:
        dict: { variable_name: { transect_code: pandas.Series } }
    """

    base_url = "http://thredds.cdip.ucsd.edu/thredds/dodsC/cdip/model/MOP_alongshore"
    start = np.datetime64(start_date)
    end = np.datetime64(end_date)

    # Initialize output structure
    results = {var: {} for var in variable_names}

    for transect in transect_codes:
        url = f"{base_url}/{transect}_hindcast.nc"
        try:
            ds = xr.open_dataset(url)

            # Time filtering
            time = ds['waveTime']
            mask = (time >= start) & (time <= end)
            time_filtered = time[mask]
            time_pst = pd.to_datetime(time_filtered.values) - pd.Timedelta(hours=8)

            for var in variable_names:
                if var in ds:
                    values = ds[var].sel(waveTime=mask).values
                    results[var][transect] = pd.Series(values, index=time_pst)
                else:
                    print(f"Variable '{var}' not found in {transect}")
        except Exception as e:
            print(f"Error loading {transect}: {e}")

    return results
