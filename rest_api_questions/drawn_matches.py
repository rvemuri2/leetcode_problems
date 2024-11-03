import requests

def get_drawn_matches(year):
    base_url = "https://jsonmock.hackerrank.com/api/football_matches"
    total_draws = 0
    page = 1

    while True:
        # Make the request with current page
        response = requests.get(base_url, params={"year": year, "page": page})
        
        # Check if the request was successful
        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code}")
            return 0

        # Parse the JSON data
        data = response.json()
        matches = data.get("data", [])

        # Check if there are no matches left
        if not matches:
            break

        # Count the draws
        for match in matches:
                total_draws += (int(match["team1goals"]) + int(match["team2goals"]))

        # Stop if we are on the last page
        if page >= data.get("total_pages", 0):
            break
        
        # Increment to the next page
        page += 1

    return total_draws

# Example usage
year = 2011
drawn_matches = get_drawn_matches(year)
print(f"Number of drawn matches in {year}: {drawn_matches}")
