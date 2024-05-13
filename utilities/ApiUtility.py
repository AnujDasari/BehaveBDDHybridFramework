import requests

from utilities import ConfigReaderUtility


class APIUtility:
    api_url = ConfigReaderUtility.read_configuration("basic info", "api_url")
    api_key = ConfigReaderUtility.read_configuration("basic info", "api_key")
    global response

    def method_call(self, method, endpoint, city):
        if method == 'GET':
            uri = self.api_url + endpoint + "?q=" + city + "&key=" + self.api_key
            response = requests.request("GET", uri)
            return response

    def get_status_code(self):
        status_code = response.status_code
        return status_code

    def verify_get_response_data(self, table):
        for row in table:
            name = row['name']
            region = row['region']
            country = row['country']
            return name, region, country
