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
    website_url = 'https://www.youtube.com'
    output_file_path = 'downloaded-webpage.html'

    # Call the download_html function
    download_html(website_url, output_file_path)
