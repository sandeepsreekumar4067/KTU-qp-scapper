# A.P.J. Abdul Kalam Technological University (KTU) Question Papers and Notes Scraper

This repository contains a Flask API that scrapes the web to retrieve question papers and notes for engineering subjects from the A.P.J. Abdul Kalam Technological University (KTU) Kerala. The API performs searches based on the provided subject keyword and returns the relevant documents in JSON format.

## Features

- Scrapes question papers and notes from the KTU digital library.
- Returns search results including title, author, date, and PDF links.
- Configurable and extendable for other use cases.

## Requirements

- Python 3.7+
- Flask
- Selenium
- BeautifulSoup4
- WebDriver Manager for Chrome
- Dotenv

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/ktu-scraper.git
    cd ktu-scraper
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:

    Create a `.env` file in the root directory and add any required environment variables. For this project, there are no specific environment variables needed, but this file can be used to manage any future configurations.

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Use a web browser or an API client like Postman to send a GET request to the following endpoint:

    ```
    http://127.0.0.1:5000/search?q=<search_key>
    ```

    Replace `<search_key>` with the subject or keyword you want to search for.

3. The API will return a JSON response with the search results, including the title, author, date, and PDF link for each document.

## Example

Send a GET request to:

```
http://127.0.0.1:5000/search?q=computer+science
```

Example response:

```json
[
    {
        "Title": "Introduction to Computer Science",
        "Author": "John Doe",
        "Date": "2022-06-01",
        "pdf_link": "http://202.88.225.92/.../document.pdf"
    },
    {
        "Title": "Advanced Algorithms",
        "Author": "Jane Smith",
        "Date": "2021-12-15",
        "pdf_link": "http://202.88.225.92/.../document.pdf"
    }
]
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [Selenium](https://www.selenium.dev/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [WebDriver Manager for Python](https://github.com/SergeyPirogov/webdriver_manager)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact

For any inquiries or feedback, please contact [email](mailto:sandeepsreekumar4067@gmail.com).
