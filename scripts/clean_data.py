import os
import pandas as pd

class DisneyLorcana:
    def the_first_chapter(self):
        """
        Clean up the data for `The First Chapter` set
        """

        print('Cleaning up the data for `The First Chapter` set')

        # Load the CSV file
        csv_file = 'data/processed/disney_lorcana/the_first_chapter.csv'
        data = pd.read_csv(csv_file)

        # Remove Ink Types from the Card Name
        ink_types = ['AMBER', 'AMETHYST', 'EMERALD', 'RUBY', 'SAPPHIRE', 'STEEL']
        for ink_type in ink_types:
            data['card_name'] = data['card_name'].apply(lambda x: x.replace(ink_type, '').strip())
            print(f'Removed {ink_type} from the card name')
        
        # Remove `TOTAL` from the Card Name
        data['card_name'] = data['card_name'].apply(lambda x: x.replace('TOTAL', '').strip())
        print('Removed TOTAL from the card name')

        # Save the cleaned data
        data.to_csv(csv_file, index=False)

        print('Cleaned up the data for `The First Chapter` set')

    def rise_of_the_floodborn(self):
        """
        Clean up the data for `Rise of The Floodborn` set
        """

        print('Cleaning up the data for `Rise of The Floodborn` set')

        # Load the CSV file
        csv_file = 'data/processed/disney_lorcana/rise_of_the_floodborn.csv'
        data = pd.read_csv(csv_file)

        # Remove Ink Types from the Card Name
        ink_types = ['AMBER', 'AMETHYST', 'EMERALD', 'RUBY', 'SAPPHIRE', 'STEEL']
        for ink_type in ink_types:
            data['card_name'] = data['card_name'].apply(lambda x: x.replace(ink_type, '').strip())
            print(f'Removed {ink_type} from the card name')
        
        # Remove `TOTAL` from the Card Name
        data['card_name'] = data['card_name'].apply(lambda x: x.replace('TOTAL', '').strip())
        print('Removed TOTAL from the card name')

        # Save the cleaned data
        data.to_csv(csv_file, index=False)

        print('Cleaned up the data for `Rise of The Floodborn` set')

    def into_the_inklands(self):
        """
        Clean up the data for `Into the Inklands` set
        """

        print('Cleaning up the data for `Into the Inklands` set')

        # Load the CSV file
        csv_file = 'data/processed/disney_lorcana/into_the_inklands.csv'
        data = pd.read_csv(csv_file)

        # Remove Ink Types from the Card Name
        ink_types = ['AMBER', 'AMETHYST', 'EMERALD', 'RUBY', 'SAPPHIRE', 'STEEL']
        for ink_type in ink_types:
            data['card_name'] = data['card_name'].apply(lambda x: x.replace(ink_type, '').strip())
            print(f'Removed {ink_type} from the card name')
        
        # Remove `TOTAL` from the Card Name
        data['card_name'] = data['card_name'].apply(lambda x: x.replace('TOTAL', '').strip())
        print('Removed TOTAL from the card name')

        # Save the cleaned data
        data.to_csv(csv_file, index=False)

        print('Cleaned up the data for `Into the Inklands` set')

    def ursulas_return(self):
        """
        Clean up the data for `Ursulas Return` set
        """

        print('Cleaning up the data for `Ursulas Return` set')

        # Load the CSV file
        csv_file = 'data/processed/disney_lorcana/ursulas_return.csv'
        data = pd.read_csv(csv_file)

        # Remove Ink Types from the Card Name
        ink_types = ['AMBER', 'AMETHYST', 'EMERALD', 'RUBY', 'SAPPHIRE', 'STEEL']
        for ink_type in ink_types:
            data['card_name'] = data['card_name'].apply(lambda x: x.replace(ink_type, '').strip())
            print(f'Removed {ink_type} from the card name')
        
        # Remove `TOTAL` from the Card Name
        data['card_name'] = data['card_name'].apply(lambda x: x.replace('TOTAL', '').strip())
        print('Removed TOTAL from the card name')

        # Save the cleaned data
        data.to_csv(csv_file, index=False)

        print('Cleaned up the data for `Ursulas Return` set')

    def shimmering_skies(self):
        """
        Clean up the data for `Shimmering Skies` set
        """

        print('Cleaning up the data for `Shimmering Skies` set')

        # Load the CSV file
        csv_file = 'data/processed/disney_lorcana/shimmering_skies.csv'
        data = pd.read_csv(csv_file)

        # Remove Ink Types from the Card Name
        ink_types = ['AMBER', 'AMETHYST', 'EMERALD', 'RUBY', 'SAPPHIRE', 'STEEL']
        for ink_type in ink_types:
            data['card_name'] = data['card_name'].apply(lambda x: x.replace(ink_type, '').strip())
            print(f'Removed {ink_type} from the card name')
        
        # Remove `TOTAL` from the Card Name
        data['card_name'] = data['card_name'].apply(lambda x: x.replace('TOTAL', '').strip())
        print('Removed TOTAL from the card name')

        # Save the cleaned data
        data.to_csv(csv_file, index=False)

        print('Cleaned up the data for `Shimmering Skies` set')

    def run(self):
        """
        Run the Disney Lorcana data cleaning
        """
        # Clean up the data for `The First Chapter` set
        self.the_first_chapter()

        # Clean up the data for `Rise of The Floodborn` set
        self.rise_of_the_floodborn()

        # Clean up the data for `Into the Inklands` set
        self.into_the_inklands()

        # Clean up the data for `Ursulas Return` set
        self.ursulas_return()

        # Clean up the data for `Shimmering Skies` set
        self.shimmering_skies()

class LorcastAPI:

    def __init__(self):
        self.process_dir = 'data/processed/lorcast_api'

        # Create the processed directory if it does not exist
        if not os.path.exists(self.process_dir):
            os.makedirs(self.process_dir)

    def clean_cards(self):
        # Load data from Lorcast API CSV files
        lorcast_api_dir = "data/raw/lorcast_api"
        csv_files = [f"{lorcast_api_dir}/{f}" for f in os.listdir(lorcast_api_dir) if f.endswith('.csv')]
        num_of_files = len(csv_files)
        print(f"Found {num_of_files} CSV files in {lorcast_api_dir}")

        # Load data from each CSV file
        for csv_file in csv_files:
            # Set the data file path to the current CSV file
            data_file = csv_file
            
            # Replace `raw` with `processed` in the file path for saving the processed data
            process_file = csv_file.replace('raw', 'processed')

            print(f"Loading data from {data_file}")
            df = pd.read_csv(csv_file)

            # Remove `image_uris` column
            if 'image_uris' in df.columns:
                df.drop(columns=['image_uris'], inplace=True)
                print("Removed `image_uris` column")

            # Replace `raw` with `processed` in the file path
            process_file = csv_file.replace('raw', 'processed')

            # Save the processed data
            df.to_csv(process_file, index=False)



            

            

    def run(self):
        """
        Run the Lorcast API data cleaning
        """
        self.clean_cards()

if __name__ == '__main__':

    # Clean up the data for Disney Lorcana
    disney_lorcana = DisneyLorcana()
    disney_lorcana.run()

    # Clean up the data for Lorcast API
    lorcast_api = LorcastAPI()
    lorcast_api.run()