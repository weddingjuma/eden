# -*- coding: utf-8 -*-

"""
    This file specifies the tests which are to be run on the Philippines template.

    modules/tests/suite.py runs this file to get the test_list which is to be loaded.
    To add more tests which are to run on this template, simply add the class name
    to the list below.
"""

from gluon import current

current.selenium_tests = [
                          "CreateOrganisation",
                          "CreateOffice",
                          "CreateStaff",
                          "CreateStaffJobTitle",
                          "CreateStaffCertificate",
                          "SearchStaff",
                          "StaffReport",
                          "CreateStaffTraining",
                          "AddStaffParticipants",
                          "AddStaffToOffice",
                          "CreateCatalog",
                          "CreateCategory",
                          "CreateFacility",
                          "AddStaffToOrganisation",
                          ]
