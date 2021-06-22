import requests, json
from secrets import token

authHeader = {'Authorization': 'token {token}'.format(token = token)}
baseUrl = 'https://api.github.com/'

def apiCall(endpoint, **kwargs):
  return requests.get(baseUrl + endpoint, headers=authHeader, **kwargs)

def issues(**kwargs):
  return apiCall('repos/lampepfl/dotty/issues', params=kwargs).json()
