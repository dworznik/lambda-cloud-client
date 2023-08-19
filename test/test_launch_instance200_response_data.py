# coding: utf-8

"""
    Lambda Cloud API

    API for interacting with the Lambda GPU Cloud  # noqa: E501

    The version of the OpenAPI document: 1.4.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import lambda_cloud_client
from lambda_cloud_client.models.launch_instance200_response_data import LaunchInstance200ResponseData  # noqa: E501
from lambda_cloud_client.rest import ApiException

class TestLaunchInstance200ResponseData(unittest.TestCase):
    """LaunchInstance200ResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LaunchInstance200ResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LaunchInstance200ResponseData`
        """
        model = lambda_cloud_client.models.launch_instance200_response_data.LaunchInstance200ResponseData()  # noqa: E501
        if include_optional :
            return LaunchInstance200ResponseData(
                instance_ids = [
                    '0920582c7ff041399e34823a0be62549'
                    ]
            )
        else :
            return LaunchInstance200ResponseData(
                instance_ids = [
                    '0920582c7ff041399e34823a0be62549'
                    ],
        )
        """

    def testLaunchInstance200ResponseData(self):
        """Test LaunchInstance200ResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
