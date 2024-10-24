import requests
import pandas as pd


# # Bank of Canada API for GDP data (example)
# url = 'https://www.bankofcanada.ca/valet/observations/FXUSDCAD/json'

# # Fetching data
# response = requests.get(url)
# data = response.json()

# # Convert to DataFrame
# observations = data['observations']
# df = pd.DataFrame(observations)


# # Save to CSV
# df.to_csv('canadian_macro_data.csv', index=False)



# Bank of Canada Valet API endpoint for CPI data
url_cpi = 'https://www.bankofcanada.ca/valet/observations/V41690973/json'


# Fetching CPI data
response_cpi = requests.get(url_cpi)
cpi_data = response_cpi.json()

# Convert CPI data to DataFrame
cpi_observations = cpi_data['observations']
df_cpi = pd.DataFrame(cpi_observations)

breakpoint()
# Save CPI data to CSV
df_cpi.to_csv('canadian_cpi_data.csv', index=False)

print("Canadian CPI data saved to 'canadian_cpi_data.csv'")
