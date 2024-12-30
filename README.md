
# URL Shortener using Bitly API

A simple and interactive URL shortener application built with Python. This tool leverages the [Bitly API](https://dev.bitly.com/) to shorten long URLs into concise and shareable links.

---

## Features

- **Interactive Command-Line Interface (CLI):**
  - Easily shorten URLs by selecting from a menu.
  - Validate URLs before making API requests.

- **Secure Token Management:**
  - Access the Bitly API securely using an environment variable for the access token.

- **Error Handling:**
  - Handles invalid URLs and Bitly API errors gracefully.

---

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.7 or higher
- Pip package manager

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Epi-Nabeel/urlshortener.git
   cd urlshortener
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate    # On Linux/Mac
   venv\Scripts\activate       # On Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your environment variables:**

   - Create a `.env` file in the root directory of the project.
   - Add your **Bitly Access Token**:
     ```
     You will need your Bitly API key for this to work
     ```

---

## Usage

1. **Run the application:**
   ```bash
   python main.py
   ```

2. **Follow the interactive menu:**

   - Option 1: Enter a URL to shorten.
   - Option 2: Exit the application.

---

## Example

### Input:
```
Enter the URL to shorten: https://www.example.com
```

### Output:
```
Shortened URL: https://bit.ly/3abcdEf
```

---

## Future Enhancements

- Add functionality to expand shortened URLs back to their original form.
- Display analytics for the shortened URLs (e.g., click count).
- Provide a web-based interface using Flask or FastAPI.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

## Author

**Epi-Nabeel**  
[GitHub](https://github.com/Epi-Nabeel)
