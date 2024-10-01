import requests
import json

from framework.utilities.Logger import Logger
from framework.utilities.utils import Utils


class APIRequests:
    log = Logger().get_logger()
    utils = Utils()

    @staticmethod
    def post_request(url, request_body, headers):
        try:
            response = requests.post(url, json=request_body, headers=headers, cookies={})
            response_json = response.json()
            APIRequests.log.info("Request body:")
            APIRequests.log.info(json.dumps(request_body, indent=4))
            APIRequests.log.info("Response body:")
            APIRequests.log.info(json.dumps(response_json, indent=4))
            return response_json
        except (requests.exceptions.RequestException, AssertionError, KeyError) as e:
            APIRequests.log.error(f"Error occurred: {e}")
            assert False

    @staticmethod
    def get_request(url, json_data, headers):
        try:
            response = requests.get(url, json=json_data, headers=headers)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            response_json = response.json()
            APIRequests.log.info(json.dumps(response_json, indent=4))
            return response_json
        except (requests.exceptions.RequestException, ValueError) as e:
            APIRequests.log.error(f"Error occurred: {e}")
            APIRequests.log.error(f"Response content: {response.text}")
            assert False