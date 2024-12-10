import os
import re
import requests
import time
import pandas as pd
from PyPDF2 import PdfReader

class PDFScraper:
    
    def v1(self, datasource_name, lorcana_set_name, pdf_path):
        """ 
        This is the first version of the method that scrapes data from the PDF file.

        Currently, this method only supports the following raw data sources sets:

        - Disney Lorcana
            - The First Chapter
            - Rise of The Floodborn
            - Into the Inklands
            - Ursula's Return
            - Shimmering Skies
        """
        print(f"Scraping data for the {datasource_name} data source")
        print(f"Scraping data for the {lorcana_set_name} set")
        print(f"Scraping data from the PDF path: {pdf_path}")

        # Open the PDF file
        reader = PdfReader(pdf_path)

        # Get the number of pages
        number_of_pages = len(reader.pages)
        print(f"Number of pages: {number_of_pages}")

        # Only extract text from the first page
        page = reader.pages[0]
        text = page.extract_text()
        # Uncomment the following line to see the extracted text for debugging purposes
        # print(text)

        # Extract text that matches a specific pattern
        # The pattern is a number followed by a space and then any character
        pattern = r'\d+\s.*'
        matches = re.findall(pattern, text)
        # Uncomment the following line to see the matches for debugging purposes
        # print(matches)

        # Split each value in the list by the first space only
        text_list = [re.split(r'\s', x, 1) for x in matches]
        # Uncomment the following line to see the text list for debugging purposes
        
        # Convert text_list to a DataFrame
        df = pd.DataFrame(text_list, columns=["card_number", "card_name"])

        # Create data directory if it does not exist
        data_dir = f"data/processed/{datasource_name.lower().replace(' ', '_')}"
        print(f"Data directory: {data_dir}")

        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
            print("Data directory created")
        else:
            print("Data directory already exists")

        # Create a CSV file
        csv_file = f"{data_dir}/{lorcana_set_name.lower().replace(' ', '_')}.csv"
        print(f"CSV file: {csv_file}")

        # Convert text_list to a DataFrame
        df = pd.DataFrame(text_list, columns=["card_number", "card_name"])
        print("DataFrame created")

        # Save the DataFrame to a CSV file
        df.to_csv(csv_file, index=False)
        print("CSV file created")

        print("Data extraction complete")

class LorcastScraper:

    def __init__(self):
        self.base_api_url = "https://api.lorcast.com/v0"
        self.datasource_name = "Lorcast API"
        # Get the current date and time in UTC in the format: YYYY-MM-DD
        self.scraped_at = pd.Timestamp.now(tz="UTC").strftime("%Y-%m-%d")

        # Create data directory if it does not exist
        self.data_dir = f"data/raw/{self.datasource_name.lower().replace(' ', '_')}"
        print(f"Data directory: {self.data_dir}")

        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
            print("Data directory created")
        else:
            print("Data directory already exists")

        # Create images directory if it does not exist
        self.images_dir = f"images/cards/{self.datasource_name.lower().replace(' ', '_')}"
        print(f"Images directory: {self.images_dir}")

        if not os.path.exists(self.images_dir):
            os.makedirs(self.images_dir)
            print("Images directory created")
        else:
            print("Images directory already exists")

    def sets(self):
        print(f"Getting sets data from the Loecast API")

        # Create the API URL for the sets endpoint
        api_url = f"{self.base_api_url}/sets"
        print(f"API URL: {api_url}")

        # Get the sets from the Lorecast API
        sets = requests.get(api_url).json().get('results')

        # Coverting the sets to a DataFrame
        df = pd.DataFrame(sets)

        # Add the scraped_at column
        df['scraped_at'] = self.scraped_at

        # Create a CSV file
        csv_file =  f"{self.data_dir}/sets.csv"
        print(f"CSV file: {csv_file}")

        # Save the DataFrame to a CSV file
        df.to_csv(csv_file, index=False)

        # Return the sets JSON data
        return sets
    
    def cards(self, set_id, set_name):
        print(f"Getting cards data for the {set_id} set from the Lorcast API")

        # Format the set name to be used as a file name
        # Remove replace spaces with underscores, convert to lowercase and remove special characters expect underscores
        set_name = re.sub(r'[^a-zA-Z0-9_]', '', set_name.replace(' ', '_').lower())

        # Create the API URL for the sets endpoint
        api_url = f"{self.base_api_url}/sets/{set_id}/cards"
        print(f"API URL: {api_url}")

        # Get the cards from the Lorecast API
        cards = requests.get(api_url).json()
        num_of_cards = len(cards)
        print(f"Number of cards: {num_of_cards}")
        
        # Coverting the sets to a DataFrame
        df = pd.DataFrame(cards)

        # Create images directory for the set name if it does not exist
        image_set_dir = f"{self.images_dir}/{set_name}"
        print(f"Images set directory: {image_set_dir}")

        if not os.path.exists(image_set_dir):
            os.makedirs(image_set_dir)
            print("Images set directory created")
        else:
            print("Images set directory already exists")

        # Download card images by getting the image_uris
        for index, row in df.iterrows():
            card_id = row.get('id')
            image_uri = row.get('image_uris').get('digital').get('large', None)
            if image_uri:
                image_file = f"{image_set_dir}/{card_id}.png"
                print(f"Downloading image: {image_uri}")
                # Wait for 100 milliseconds before downloading the next image
                time.sleep(0.1)

                # Download the image
                with open(image_file, 'wb') as image:
                    image.write(requests.get(image_uri).content)
                print(f"Image downloaded: {image_file}")

        # Add the scraped_at column
        df['scraped_at'] = self.scraped_at

        # Create a CSV file
        csv_file =  f"{self.data_dir}/{set_name}.csv"
        print(f"CSV file: {csv_file}")

        # Save the DataFrame to a CSV file
        df.to_csv(csv_file, index=False)

if __name__ == '__main__':

    # Create an instance of the PDFScraper class
    pdf_scraper = PDFScraper()

    # Extract data for `The First Chapter` set from the `Disney Lorcana` data source
    pdf_scraper.v1(
        datasource_name='Disney Lorcana',
        lorcana_set_name='The First Chapter',
        pdf_path='data/raw/disney_lorcana/the-first-chapter-set-checklist.pdf'
    )

    # Extract data for `Rise of The Floodborn` set from the `Disney Lorcana` data source
    pdf_scraper.v1(
        datasource_name='Disney Lorcana',
        lorcana_set_name='Rise of The Floodborn',
        pdf_path='data/raw/disney_lorcana/rise-of-the-floodborn-set-checklist.pdf'
    )

    # Extract data for `Into the Inklands` set from the `Disney Lorcana` data source
    pdf_scraper.v1(
        datasource_name='Disney Lorcana',
        lorcana_set_name='Into the Inklands',
        pdf_path='data/raw/disney_lorcana/into-the-inklands-set-checklist.pdf'
    )

    # Extract data for `Ursula's Return` set from the `Disney Lorcana` data source
    pdf_scraper.v1(
        datasource_name='Disney Lorcana',
        lorcana_set_name="Ursulas Return",
        pdf_path='data/raw/disney_lorcana/ursulas-return-set-checklist.pdf'
    )

    # Extract data for `Shimmering Skies` set from the `Disney Lorcana` data source
    pdf_scraper.v1(
        datasource_name='Disney Lorcana',
        lorcana_set_name='Shimmering Skies',
        pdf_path='data/raw/disney_lorcana/shimmering-skies-set-checklist.pdf'
    )

    # Create an instance of the LorecastScraper class
    lorcast_scraper = LorcastScraper()

    # Get the sets from the Lorcast API
    sets = lorcast_scraper.sets()

    # Get cards from each set from the Lorcast API
    for set in sets:
        # Wait for 100 millisecond before getting the cards data for the next set
        time.sleep(0.1)
        set_id = set.get('id')
        set_name = set.get('name')
        print(f"Getting cards data for the {set_name} set from the Lorcast API")
        lorcast_scraper.cards(set_id, set_name)
        
