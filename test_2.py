import json
import requests
import urllib.parse as urlparse
from urllib.parse import urlencode

url = "https://www.ringcentral.com/services/plans-and-pricing.servlet"
parameterValueInvalidException = 'com.ringcentral.www.aem.core.commons.http.exceptions.exposable.ParameterValueInvalidException'

def get_request_json(url, params):
    r = requests.get(url, params=params)
    return r.json()

def get_request_header(url, params):
    r = requests.get(url, params=params)
    return r.headers


def test_productId():
    # https://www.ringcentral.com/services/plans-and-pricing.servlet?productId=blabla
    productId = 'blabla'
    response = get_request_json(url, {'productId': productId})
    assert response['statusCode'] == 400
    message = 'Request parameter "productId" value "' + productId + '" issue: Validation failed'
    assert response['content']['exceptions'][0]['message'] == message
    assert response['content']['exceptions'][0]["type"] == 'com.ringcentral.www.aem.core.commons.http.exceptions.exposable.ParameterValueInvalidException'
    headers = get_request_header(url, {'productId': productId})
    assert headers['Content-Type'] == 'application/json;charset=utf-8'

def test_product():
    productId = 'blabla1'
    response = get_request_json(url, {'productId': productId})
    assert response['statusCode'] == 400
    message = 'Request parameter "productId" value "' + productId + '" issue: Validation failed'
    assert response['content']['exceptions'][0]['message'] == message
    assert response['content']['exceptions'][0]["type"] == 'com.ringcentral.www.aem.core.commons.http.exceptions.exposable.ParameterValueInvalidException'
    headers = get_request_header(url, {'productId': productId})
    assert headers['Content-Type'] == 'application/json;charset=utf-8'



