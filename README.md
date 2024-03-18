# OnlyFans Profile Scraper README
Description
This Python script is designed to automate the extraction of likes counts and direct social media links from OnlyFans profiles. Leveraging Selenium WebDriver for web navigation and scraping, it targets specific URLs to gather social media information. The script efficiently retrieves likes counts along with Instagram, Snapchat, TikTok, and Twitter profile links associated with each OnlyFans profile. The results are conveniently saved in a CSV file, facilitating social media analysis and comprehensive data collection for OnlyFans content creators.

Features
Automatically scrapes likes counts from OnlyFans profiles.
Retrieves direct links to associated Instagram, Snapchat, TikTok, and Twitter profiles from OnlyFans.
Outputs the collected data into a CSV file for subsequent analysis and review.
Requirements
Ensure you have Python 3.x installed on your machine. The script requires the following Python packages:

Selenium WebDriver
requests
Install the necessary Python packages by running:

Copy code
pip install -r requirements.txt
Usage
Prepare your input CSV file named of_scrapping.csv, containing the column "links" with URLs of the OnlyFans profiles to be scraped.
Ensure of_scrapping.csv is located in the same directory as the script.
Execute the script with the command:
Copy code
python social_media_scraper.py
Upon completion, the script generates an output file of_results.csv, detailing the URLs, likes counts, and direct social media links for each profile.
Input File Format
The CSV file for input should adhere to the following structure:

arduino
Copy code
links
https://onlyfans.com/exampleProfile1
https://onlyfans.com/exampleProfile2
...
Output File Format
The generated output CSV file contains the following columns:

mathematica
Copy code
URL, Likes Count, Instagram URL, Snapchat URL, TikTok URL, Twitter URL
Contributing
We welcome contributions, issues, and feature requests. Please visit the issues page if you're interested in contributing.

License
This project is open-source, licensed under the MIT License. See the LICENSE file for more details.

