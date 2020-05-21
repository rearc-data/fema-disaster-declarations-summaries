import os
import time
import boto3
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from multiprocessing.dummy import Pool

def data_to_s3(endpoint):

	# throws error occured if there was a problem accessing data
	# otherwise downloads and uploads to s3

	source_dataset_url = 'https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries'

	retries = 5
	for attempt in range(retries):
		try:
			response = urlopen(source_dataset_url + endpoint)
			break
		except HTTPError as e:
			if attempt == retries:
				raise Exception('HTTPError: ', e.code, endpoint)
			time.sleep(0.2 * attempt)

		except URLError as e:
			if attempt == retries:
				raise Exception('URLError: ', e.reason, endpoint)
			time.sleep(0.2 * attempt)

	data_set_name = os.environ['DATA_SET_NAME']
	filename = data_set_name + endpoint
	file_location = '/tmp/' + data_set_name + endpoint

	with open(file_location, 'wb') as f:
		f.write(response.read())

	# variables/resources used to upload to s3
	s3_bucket = os.environ['S3_BUCKET']
	new_s3_key = data_set_name + '/dataset/' + filename
	s3 = boto3.client('s3')

	s3.upload_file(file_location, s3_bucket, new_s3_key)

	print('Uploaded: ' + filename)

	# deletes to preserve limited space in aws lamdba
	os.remove(file_location)

	# dicts to be used to add assets to the dataset revision
	return {'Bucket': s3_bucket, 'Key': new_s3_key}

def source_dataset():

	# list of enpoints to be used to access data included with product
	endpoints = [
		'.csv',
		'.json',
		'.jsona'
	]

	# multithreading speed up accessing data, making lambda run quicker
	with (Pool(3)) as p:
		asset_list = p.map(data_to_s3, endpoints)

	# asset_list is returned to be used in lamdba_handler function
	return asset_list
