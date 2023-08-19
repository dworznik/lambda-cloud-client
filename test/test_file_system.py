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
from lambda_cloud_client.models.file_system import FileSystem  # noqa: E501
from lambda_cloud_client.rest import ApiException

class TestFileSystem(unittest.TestCase):
    """FileSystem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FileSystem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FileSystem`
        """
        model = lambda_cloud_client.models.file_system.FileSystem()  # noqa: E501
        if include_optional :
            return FileSystem(
                id = '0920582c7ff041399e34823a0be62547', 
                name = 'shared-fs', 
                created = '2023-02-24T20:48:56+00:00', 
                created_by = lambda_cloud_client.models.user.user(
                    id = '0920582c7ff041399e34823a0be62549', 
                    email = 'teammate@example.com', 
                    status = 'active', ), 
                mount_point = '/home/ubuntu/shared-fs', 
                region = lambda_cloud_client.models.region.region(
                    name = 'us-tx-1', 
                    description = 'Austin, Texas', ), 
                is_in_use = True
            )
        else :
            return FileSystem(
                id = '0920582c7ff041399e34823a0be62547',
                name = 'shared-fs',
                created = '2023-02-24T20:48:56+00:00',
                created_by = lambda_cloud_client.models.user.user(
                    id = '0920582c7ff041399e34823a0be62549', 
                    email = 'teammate@example.com', 
                    status = 'active', ),
                mount_point = '/home/ubuntu/shared-fs',
                region = lambda_cloud_client.models.region.region(
                    name = 'us-tx-1', 
                    description = 'Austin, Texas', ),
                is_in_use = True,
        )
        """

    def testFileSystem(self):
        """Test FileSystem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()