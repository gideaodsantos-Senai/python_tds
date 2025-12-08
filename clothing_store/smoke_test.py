import requests

BASE_URL = 'http://127.0.0.1:5000'

def test_route(url, expected_status=200):
    try:
        response = requests.get(url)
        if response.status_code == expected_status:
            print(f"✓ {url} - Status: {response.status_code}")
        else:
            print(f"✗ {url} - Status: {response.status_code} (expected {expected_status})")
    except Exception as e:
        print(f"✗ {url} - Error: {e}")

if __name__ == '__main__':
    print("Running smoke tests...")
    test_route(BASE_URL + '/')
    test_route(BASE_URL + '/products')
    test_route(BASE_URL + '/cart')
    print("Smoke tests completed.")
