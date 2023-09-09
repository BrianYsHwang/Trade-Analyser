import requests
import pandas as pd
import numpy as np

class MovingAverage:
    def __init__(self, api_key):
        self.api_key = api_key
        self.data = None

    def retrieve_data(self, start_date, end_date, symbol):
        '''
        Retrieves data from the Polygon.io API and turns it into a DataFrame.

        inputs: 
            start_date: the lower bound of the data
            end_date: upper bound of the data
            symbol: the stock symbol or identifier
        '''
        base_url = 'https://api.polygon.io'
        endpoint = f'/v2/aggs/ticker/{symbol}/range/1/day/{start_date}/{end_date}'
        
        params = {
            'apiKey': self.api_key,
        }

        response = requests.get(base_url + endpoint, params=params)

        if response.status_code == 200:
            # Parse the JSON response into a DataFrame if the response is valid
            data = response.json()
            if 'results' in data:
                self.data = pd.DataFrame(data['results'])
            else:
                print(f"No historical data found for symbol {symbol}.")
        else:
            # if there is an error retrieving the data
            print(f"Failed to get data from Polygon.io API. Status code: {response.status_code}. Response: {response.content}")

    def prepare_data(self):
        '''
        Prepares the dataframe by changing the date datatype to datetime format.
        '''

        if self.data is not None:
            print(self.data)
            #self.data['date'] = pd.to_datetime(self.data['date'], format='%Y-%m-%d')



    def calculate_moving_averages(self, windows=[5, 10, 50, 100, 200]):
        '''
        Creates new columns in the dataframe.
        Closing prices are used to calculate moving averages.
        This is done for various periods from 5 to 200.

        input:
            windows: a list of values representing the periods
        '''
        if self.data is not None:
            for window in windows:
                # create a new column representing the moving averages (based off closing price) for each period value in windows
                self.data[f'{window} day ma'] = self.data['close'].rolling(window).mean()  

            #test_calculate_ma()
        
    def test_calculate_ma(self):
        pass

        


