from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import json
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Function to perform the search and return results
def perform_search(search_key):
    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('window-size=1920x1080')
    
    search_results = []

    # Initialize the WebDriver in headless mode
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    IP = "http://202.88.225.92/"
    URL = "http://202.88.225.92/xmlui/community-list"
    driver.get(URL)

    # Wait for the search field to be visible
    try:
        search_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "ds-text-field"))
        )
    except TimeoutException:
        driver.quit()
        return {"error": "Search field not found"}

    # Enter the search key into the search field
    search_field.clear()
    search_field.send_keys(search_key)

    # Submit the search
    search_field.send_keys(Keys.RETURN)

    # Wait for the search results to load
    try:
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ds-artifact-item"))
        )
    except TimeoutException:
        driver.quit()
        return {"error": "Timed out waiting for search results to load"}

    # Select maximum results per page
    driver.maximize_window()

    # Wait until the dropdown is present
    wait = WebDriverWait(driver, 10)
    results_per_page_dropdown = wait.until(EC.presence_of_element_located((By.ID, 'aspect_artifactbrowser_SimpleSearch_field_rpp')))

    # Select 100 results per page
    select = Select(results_per_page_dropdown)
    select.select_by_value('100')

    # Wait until the "Go" button is present
    go_button = wait.until(EC.presence_of_element_located((By.ID, 'aspect_artifactbrowser_SimpleSearch_field_submit')))

    # Click the "Go" button to reload the page with 100 results per page
    go_button.click()

    # Wait for the page to reload and the results to be present
    try:
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ds-artifact-item"))
        )
    except TimeoutException:
        driver.quit()
        return {"error": "Timed out waiting for search results to load"}

    # Get the page source and parse it with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Extract and print search results
    results = soup.find_all('li', class_='ds-artifact-item')
    for result in results:
        title_elem = result.find('div', class_='artifact-title').find('a')
        title = title_elem.get_text(strip=True)
        href = IP + title_elem['href']
        author = result.find('span', class_='author').get_text(strip=True)
        date = result.find('span', class_='date').get_text(strip=True)
        search_results.append({
            "Title": title,
            "Author": author,
            "Date": date,
            "Href": href
        })

    # Close the WebDriver
    driver.quit()

    return search_results

@app.route('/search', methods=['GET'])
def search():
    search_key = request.args.get('q')
    if not search_key:
        return jsonify({"error": "No search key provided"}), 400

    results = perform_search(search_key)
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
