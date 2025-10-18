# This file is to show how to run a TC multiple times with different different values
# Fixture name: crossBrowser
# Check the same fixture in conftest file how we sent the data for the multiple run
import pytest

@pytest.mark.usefixtures("crossBrowser")
def test_openWebsite(crossBrowser):
        print("Opening for ",crossBrowser[0],"Where password is",crossBrowser[1])