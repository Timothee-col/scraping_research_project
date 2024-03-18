import csv
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def find_likes_count(driver, url):
    try:
        driver.get(url)
        wait = WebDriverWait(driver, 10)
        xpath_expression = "//*[name()='svg' and @data-icon-name='icon-like']/following-sibling::span[contains(@class, 'b-profile__sections__count') and contains(@class, 'g-semibold')]"
        element = wait.until(EC.presence_of_element_located((By.XPATH, xpath_expression)))
        return element.text
    except Exception as e:
        print(f"Unable to find likes count for URL {url}: {e}")
        return "na"

def find_social_media_link(driver, url, icon_name):
    try:
        wait = WebDriverWait(driver, 10)
        xpath_expression = f"//*[name()='svg' and @data-icon-name='icon-{icon_name}-social']/ancestor::a"
        element = wait.until(EC.presence_of_element_located((By.XPATH, xpath_expression)))
        href = element.get_attribute('href')
        final_url = requests.get(href, allow_redirects=True).url
        return final_url
    except Exception as e:
        print(f"Exception occurred while trying to find {icon_name} link for URL {url}: {e}")
        return "na"

chrome_options = Options()
chrome_options.add_argument("--headless")
service = Service(ChromeDriverManager().install())


driver = webdriver.Chrome(service=service, options=chrome_options)

input_file_path = 'of_scrapping.csv'
output_file_path = 'of_results.csv'

with open(input_file_path, mode='r', newline='', encoding='utf-8') as file, open(output_file_path, mode='w', newline='', encoding='utf-8') as outfile:
    reader = csv.DictReader(file)
    writer = csv.writer(outfile)
    writer.writerow(['URL', 'Likes Count', 'Instagram URL', 'Snapchat URL', 'TikTok URL', 'Twitter URL'])
    
    for row in reader:
        url = row["links"]
        likes_count = find_likes_count(driver, url)
        instagram_url = find_social_media_link(driver, url, 'instagram')
        snapchat_url = find_social_media_link(driver, url, 'snapchat')
        tiktok_url = find_social_media_link(driver, url, 'tiktok')
        twitter_url = find_social_media_link(driver, url, 'twitter')
        writer.writerow([url, likes_count, instagram_url, snapchat_url, tiktok_url, twitter_url])


driver.quit()

print("Les résultats ont été enregistrés dans:", output_file_path)
