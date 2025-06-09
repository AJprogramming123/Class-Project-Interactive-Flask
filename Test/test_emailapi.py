import os
import pytest
from App.api_request import check_email_breach

#This is important testing with MY OWN API Key to test an email atleast to see if it works
@pytest.mark.skipif(
    not os.getenv("RAPIDAPI_KEY"),
    reason="RAPIDAPI_KEY not set in environment" #I guess for the decorator this is a possible command you can use to give out the reason during testings toward why not
)
def test_api_returns_response():
    result = check_email_breach("test@example.com")
    assert result is not None
    assert isinstance(result, dict) or isinstance(result, list)

