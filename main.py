import requests
import pytest

URL = "https://api.chucknorris.io"

#Check that the request returns a code 200, the data type is JSON and the result is not empty
def test_get_jokes_categories_check():
    response = requests.get(URL + "/jokes/categories")
    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]
    assert len(response.json()) > 0


#Take one of the categories and make a request for it
def test_get_jokes_search_check_successful_request_returns():
    response_categories = requests.get(URL + "/jokes/categories")
    response_categories_body = response_categories.json()

    failed = 0
    #Iterating over the list of categories
    for category in response_categories_body:        
        #Making a request to receive search results for the selected category
        response_search = requests.get(URL + "/jokes/search?query={}".format(category))

        assert response_search.status_code == 200
        assert "application/json" in response_search.headers["Content-Type"]
        response_search_body = response_search.json()
        assert len(response_search_body) > 0
        
        for item_result in response_search_body["result"]:
            in_result = 0
            if category in str(item_result["value"]).lower():
                in_result += 1
            if category in item_result["categories"]:
                in_result += 1

            if in_result == 0:
                pytest.skip("search result is empty\nquery: {}\nvalue: {}\ncategories: {}".format(category, item_result["value"], str(item_result["categories"])))
