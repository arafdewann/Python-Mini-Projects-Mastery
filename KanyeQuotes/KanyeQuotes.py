import requests  # This lets us get data from the internet

# This function gets a quote from Kanye West
def fetch_quote():
    response = requests.get("https://api.kanye.rest")  # Get data from the Kanye API
    response.raise_for_status()  # Check if the request was successful
    return response.json()["quote"]  # Get the quote from the data

# This is the main part of the program
def main():
    try:
        print(f"Kanye says: {fetch_quote()}")  # Print the quote from Kanye
    except requests.RequestException as e:
        print(f"Error: {e}")  # Print an error message if something goes wrong

# This runs the main part of the program
if __name__ == "__main__":
    main()
