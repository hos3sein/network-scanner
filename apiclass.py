from coinmarketcapapi import CoinMarketCapAPI

import time


class getdata():
	
	def __init__(self , apikey):
		self.apikey = apikey

	def give_me_data():
		try:
			cmc =CoinMarketCapAPI(api_key= self.apikey)
			data_listing = cmc.cryptocurrency_listings_latest()
			data = (data_listing._Response__payload)
			return(self.data)

		except (ConnectionError, Timeout, TooManyRedirects) as e:
			raise e






