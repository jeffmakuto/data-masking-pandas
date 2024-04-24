#!/usr/bin/env python3
""" Masking data """
from load_csv import DataFrameLoader
from create_df import main as create_df


class DataMasker:
    """
    class that masks sensitive data
    """
    def __init__(self, loader: DataFrameLoader) -> None:
        """
        Initializes a DataMasker object with a DataFrameLoader
        instance

        Args:
            loader(DataFrameLoader): an instance of
            DataFrameLoader
        """
        self.loader = loader

    def mask_email_address(self, placeholder: str = 'masked_email@masked.com') -> None:
        """
        Masks real emails with a placeholder in their place

        Args:
            placeholder(str): replaces the original real email address
        """
        try:
            if 'Email' in self.loader.df.columns:
                self.loader.df['Email'] = placeholder
        except KeyError:
            print("DataFrame does not have an 'Email' column.")

    def save_masked_data(self, output_file: str) -> None:
        """
        Saves masked data frame to a csv file

        Args:
            output_file(str): path to output CSV file
        """
        self.loader.df.to_csv(output_file, index=False)
        print(f"Masked data has been saved to {output_file}")
