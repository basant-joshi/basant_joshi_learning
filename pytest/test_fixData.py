# This file is for explanation how to send a data from conftest file and get them in the pytest file
# Fixture Name: data_load
# Check the same fixture in conftest file how we sent the data
import pytest


@pytest.mark.usefixtures("data_load")
class TestExample:

    def test_editProfile(self,data_load):
        print(data_load[0])
        print(data_load[1])
        print(data_load[1])
        print(data_load[2])

    

