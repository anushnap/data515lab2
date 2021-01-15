import pandas as pd
import sys

def download_data(dataset):
	if (dataset == 'fremont'):
		dataframe = pd.read_csv('https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD')
	elif (dataset == 'spokane'):
		dataframe = pd.read_csv('https://data.seattle.gov/api/views/upms-nr8w/rows.csv?accessType=DOWNLOAD')
	return dataframe

if __name__ == "__main__":
	data = download_data(dataset)
	print(data)

