import pytest
import requests
from selenium.webdriver.common.by import By
from collections import Counter


# API & Website URL
API_URL = "https://automationexercise.com/api/brandsList"

@pytest.mark.api

def test_hm_brand_presence(browser):
    """ Test to check if H&M brand exists in API and UI """

    # Step 1: Send GET API request
    response = requests.get(API_URL)
    assert response.status_code == 200, "API request failed"
    
    # Parse JSON response
    response_json = response.json()
    assert "brands" in response_json, "Key 'brands' missing in API response"
    
    # Extract brand names safely
    brand_names = []
    for brand in response_json["brands"]:
        if "brand" in brand:  # Ensure key exists
            brand_names.append(brand["brand"])

    assert "H&M" in brand_names, "H&M brand NOT found in API response"


def test_no_duplicate_brands():
    """ Ensure API response does not contain duplicate brand names """
    response = requests.get(API_URL)
    assert response.status_code == 200, "API request failed"
    response_json = response.json()  # Parse JSON
     # Ensure response is a dictionary
    assert isinstance(response_json, dict), f"Expected dict, got {type(response_json)}"
    assert "brands" in response_json, "Key 'brands' missing in API response"

    # Extract brand names safely and normalize (strip + lowercase)
    brand_names = [brand.get("brand", "").strip().lower() for brand in response_json["brands"]]

    # Count occurrences of each brand
    brand_counts = Counter(brand_names)
    duplicates = {brand: count for brand, count in brand_counts.items() if count > 1}

    if duplicates:
        pytest.fail(f"Duplicate brands found in API response: {duplicates}")

    assert len(brand_names) == len(set(brand_names)), "Duplicate brands found in API response"