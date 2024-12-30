import requests


def display_title():
    """
    Display the title screen with ASCII art and tool information.
    """
    title = """
    
U   U   RRRR   L       
U   U   R   R  L       
U   U   RRRR   L       
U   U   R  R   L       
 UUU    R   R  LLLLL   
                  
           SSS   H   H   OOO   RRRR   TTTTT  N   N  EEEE  RRRR
          S      H   H  O   O  R   R    T    NN  N  E     R   R
           SSS   HHHHH  O   O  RRRR     T    N N N  EEE   RRRR
              S  H   H  O   O  R  R     T    N  NN  E     R  R
          SSSS   H   H   OOO   R   R    T    N   N  EEEE  R   R
                                                                  
    """
    details = """
Version: 1.1
Created by: Epi-Nabeel
https://github.com/Epi-Nabeel
"""
    print(title)
    print(details)


def shorten_url_with_bitly(api_key, long_url):
    """
    Shortens a URL using the Bitly API and returns the shortened link.
    """
    api_url = "https://api-ssl.bitly.com/v4/shorten"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "long_url": long_url
    }

    try:
        response = requests.post(api_url, json=payload, headers=headers)
        if response.status_code in (200, 201):
            # Extract and return the shortened link
            data = response.json()
            return data["link"]  # This is the Bitly shortened URL
        else:
            # Display only the error message from the response
            print(f"Error: {response.status_code} - {response.json().get('message', 'Unknown error')}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None


def main():
    display_title()

    # Prompt user for their Bitly API key
    bitly_api_key = input("Enter your Bitly API key: ").strip()
    if not bitly_api_key:
        print("Error: Bitly API key is required. Exiting.")
        return

    print("\nWelcome to the Bitly URL Shortener!")
    while True:
        print("\nMenu:")
        print("1. Shorten a URL")
        print("2. Exit")

        choice = input("Enter your choice (1/2): ").strip()
        if choice == '1':
            long_url = input("Enter the URL to shorten: ").strip()
            if not long_url:
                print("Error: URL cannot be empty!")
                continue

            short_url = shorten_url_with_bitly(bitly_api_key, long_url)
            if short_url:
                print(f"Shortened URL: {short_url}")
            else:
                print("Failed to shorten the URL. Please try again.")
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
