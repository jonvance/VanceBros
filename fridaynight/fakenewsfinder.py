import requests
import os
import datetime
import pandas as pd 
from bs4 import BeautifulSoup


# Create Directory
directory = '../rawdata/'
if os.path.exists(directory):
    print("Path already exists")
else:
	print("Data will be directed to " + str(directory))
	os.makedirs(directory)

# Set starter dataframe for concatenation
df_media = pd.DataFrame(columns=['headline_descriptions'])

# List of websites for scanning
media_list = ['wsj','cnbc','fortune','businessinsider']

for media_code in media_list:
    url = 'https://www.' + str(media_code) + '.com/'
    r = requests.get(url)
    if r.status_code == 200:
        print(str(media_code) + " was sucessfully scanned")
    else:
        print("There was an error with " + str(media_code) + " || Code: " + str(r.status_code))
        
    soup = BeautifulSoup(r.content, 'html.parser')
    textContent = []

# Loop through 1000 times at a time to retrieve headlines from media site
    for i in range(0, 1000):
        try:
            if media_code == 'wsj':
                paragraphs = soup.find_all("p")[i].text

            elif media_code == 'cnbc' or media_code == 'fortune' or media_code == 'businessinsider':
                paragraphs = soup.find_all("a")[i].text
                paragraphs = paragraphs.replace("\n", "")
                paragraphs = paragraphs.strip()
            
            if len(str(paragraphs)) > 20:
                textContent.append(paragraphs)

        except IndexError:
            num0 = len(textContent)

    print(str(media_code) + " has about " + str(num0) + " descriptions - COMPLETED")

    # Create DataFrame from list of headlines 
    df = pd.DataFrame(textContent, columns=['headline_descriptions'])

    # Add which media site this headline came from
    df['news_source'] = media_code

    # Append to 1 DataFrame
    df_media = pd.concat([df_media,df], ignore_index=True, sort=True)

df_media.to_csv(str(directory) + "media_{}".format(datetime.datetime.today().strftime('%Y%m%d')))