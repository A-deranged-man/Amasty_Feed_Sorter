"""
Title: Amasty Feed Downloader
Author: Dylan Baker
Date: 19/06/19
Description: This program is designed to download CSV files from a website and save them in the users
             "Downloads" folder. Following this, it adds VAT to five specific sheets.
OS Compatibility: Can be compiled for Windows NT and *nix based systems
"""

import os  # Declare module-level (global) imports
import time


def main():
    """
    This section generates file-paths to store CSV files, downloads CSV files and adds VAT to specific CSV files
    """

    """ Retrieve the current date, format as a string and place in date variable """
    from datetime import date
    date = date.today().strftime("%d-%m-%Y")

    """ Print the title of the application and developer, wait 2 seconds """
    print('ETB Poland Amasty Feed Downloader\nDeveloped by Dylan Baker\n')
    time.sleep(2)

    """ 
    Get Downloads filepath and store in a variable. 
    Combine Downloads_Filepath variable with text and date variable to generate file-paths for all CSVs required       
    """
    print('Generating File-Paths\n')

    Downloads_Filepath = get_download_path()
    SANs_Filepath = os.path.join(Downloads_Filepath, '') + ("SANs " + date + ".csv")
    Servers_Filepath = os.path.join(Downloads_Filepath, '') + ("Servers " + date + ".csv")
    Network_Switch_Filepath = os.path.join(Downloads_Filepath, '') + ("Network_Switch " + date + ".csv")
    HDDs_Filepath = os.path.join(Downloads_Filepath, '') + ("HDDs " + date + ".csv")
    RAID_Controllers_Filepath = os.path.join(Downloads_Filepath, '') + ("RAID_Controllers " + date + ".csv")
    Network_Cards_FilePath = os.path.join(Downloads_Filepath, '') + ("Network_Cards " + date + ".csv")
    HBAs_Filepath = os.path.join(Downloads_Filepath, '') + ("HBAs " + date + ".csv")
    GBics_Filepath = os.path.join(Downloads_Filepath, '') + ("GBics " + date + ".csv")

    print('Operation Complete\n')
    time.sleep(2)

    """ Import requests as local module, use requests to download binary data from URLs and store data in variables """
    import requests

    print('Download Starting\n')

    print('Downloading SANs.csv')
    SANs_Data = requests.get(
        "REDACTED"
    )
    print('Downloading Servers.csv')
    Servers_Data = requests.get(
        "REDACTED"
    )
    print('Downloading Network_Switch.csv')
    Network_Switch_Data = requests.get(
        "REDACTED"
    )
    print('Downloading HDDs.csv')
    HDDs_Data = requests.get(
        "REDACTED"
    )
    print('Downloading RAID_Controllers.csv')
    RAID_Controllers_Data = requests.get(
        "REDACTED"
    )
    print('Downloading Network_Cards.csv')
    Network_Cards_Data = requests.get(
        "REDACTED"
    )
    print('Downloading HBAs.csv')
    HBAs_Data = requests.get(
        "REDACTED"
    )
    print('Downloading GBics.csv\n')
    GBics_Data = requests.get(
        "REDACTED"
    )

    print('Operation Complete\n')
    time.sleep(2)

    """ Open file-paths in write binary mode, write content from data variables  """
    print('Saving Files to ' + Downloads_Filepath + '\n')

    open(SANs_Filepath, 'wb').write(SANs_Data.content)
    open(Servers_Filepath, 'wb').write(Servers_Data.content)
    open(Network_Switch_Filepath, 'wb').write(Network_Switch_Data.content)
    open(HDDs_Filepath, 'wb').write(HDDs_Data.content)
    open(RAID_Controllers_Filepath, 'wb').write(RAID_Controllers_Data.content)
    open(Network_Cards_FilePath, 'wb').write(Network_Cards_Data.content)
    open(HBAs_Filepath, 'wb').write(HBAs_Data.content)
    open(GBics_Filepath, 'wb').write(GBics_Data.content)

    print('Operation Complete\n')
    time.sleep(2)

    """
    Import pandas framework as local module, read data from saved CSVs and create a data-frame saved in a variable.
    Create a new data-frame from first variable containing price * 1.2 for VAT
    Over-write price in first data-frame with price from new data-frame
    Over-write data in existing CSV with modified data-frame
    """
    import pandas as pd

    print('Adding VAT to CSVs\n')

    print('Adding VAT to HDDs.csv')
    HDDs_df = pd.read_csv(HDDs_Filepath)
    HDDs_df['price'] = (HDDs_df.price * 1.2)
    HDDs_df.to_csv(HDDs_Filepath, index=False)

    print('Adding VAT to RAID_Controllers.csv')
    RAID_Controllers_df = pd.read_csv(RAID_Controllers_Filepath)
    RAID_Controllers_df['price'] = (RAID_Controllers_df.price * 1.2)
    RAID_Controllers_df.to_csv(RAID_Controllers_Filepath, index=False)

    print('Adding VAT to Network_Cards.csv')
    Network_Cards_df = pd.read_csv(Network_Cards_FilePath)
    Network_Cards_df['price'] = (Network_Cards_df.price * 1.2)
    Network_Cards_df.to_csv(Network_Cards_FilePath, index=False)

    print('Adding VAT to HBAs.csv')
    HBAs_df = pd.read_csv(HBAs_Filepath)
    HBAs_df['price'] = (HBAs_df.price * 1.2)
    HBAs_df.to_csv(HBAs_Filepath, index=False)

    print('Adding VAT to GBics.csv\n')
    GBics_df = pd.read_csv(GBics_Filepath)
    GBics_df['price'] = (GBics_df.price * 1.2)
    GBics_df.to_csv(GBics_Filepath, index=False)

    print('Operation Complete\n')
    print('Exiting Application')
    time.sleep(2)


def get_download_path():
    """ Check users OS, return filepath to the default downloads folder for current OS """
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            downloads_location = winreg.QueryValueEx(key, downloads_guid)[0]
        return downloads_location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')


main()
