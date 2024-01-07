# HTML Downloader

## Overview

HTML Downloader is a Python script that uses Selenium and a headless Chrome browser to download the HTML content of a specified website. This can be useful for web scraping or archiving website data.

## How to Use

1. **Clone this repository to your local machine:**

    ```bash
    git clone https://github.com/your-username/html-downloader.git
    cd html-downloader
    ```

2. **Install the required dependencies:**

    ```bash
    pip install selenium
    ```

3. **Open the `main.py` file and make the following changes:**

   - Change the `website_url` variable to the desired website you want to download HTML from.
   - Change the `output_file_path` variable to the desired location where you want to save the downloaded HTML.

4. **Run the `main.py` Python file:**

    ```bash
    python main.py
    ```

## Output

The downloaded HTML content will be saved to the specified file in the same directory where you are running the program.

## Code

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def download_html(url, output_file):
    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')  # Required for headless mode on Linux

    # Initialize the Chrome browser
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Navigate to the specified URL
        driver.get(url)

        # Get the HTML content
        html_content = driver.page_source

        # Save the HTML content to a file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(html_content)

        print(f"HTML content downloaded and saved to {output_file}")

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    # Specify the URL of the website and the output file
    website_url = 'https://www.example.com'
    output_file_path = 'downloaded-webpage.html'

    # Call the download_html function
    download_html(website_url, output_file_path)
