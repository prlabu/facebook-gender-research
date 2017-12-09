import datetime
import csv
import time
import collections
import string

female_celebs = [
'taylorswift',
'mileycyrus', 
'beyonce', 
'adele', 
'selenagomez', 
]

general_feminine = [
'barbie',
'pinterest',
'sexandthecity',
'taylorswift',
'mileycyrus', 
'beyonce', 
'adele', 
'selenagomez', 
]

male_celebs = [
'zacefron',
'robertdowneyjr',
'justinbieber', 
'jayz', 
'eminem', 
'justintimberlake'
]

general_masculine = [
'barbie',
'breakingbad',
'cnn',
'lego',
'pinterest',
'reddit',
'sexandthecity',
'taylorswift',
'zacefron',
'robertdowneyjr',
'mileycyrus', 
'beyonce', 
'justinbieber', 
'adele', 
'selenagomez', 
'jayz', 
'eminem', 
'justintimberlake'
]

CATEGORIES = [female_celebs, general_feminine, male_celebs, general_masculine]
CATEGORY_NAMES = ['female_celebs', 'general_feminine', 'male_celebs', 'general_masculine']
# OR 
# PAGES = ['reddit']

# comments_file_id = "dataFiles/breakingbad/comments_2017-01-01_2017-06-01.csv"


def unicode_decode(text):
    try:
        return text.encode('utf-8').decode()
    except UnicodeDecodeError:
        return text.encode('utf-8')

# category is a list of pageIDs
def assemble_comments(category_zipped):
    category_page_ids = category_zipped[0]
    category_name = category_zipped[1]

    # output file with assembled comments
    with open('dataFiles/{}/comments.csv'.format(category_name) , 'w') as file:
        writer = csv.writer(file)

        scrape_starttime = datetime.datetime.now()
        after = ''

        print("Assembling comments for category : {}\n".format(category_name))


        for page_id in category_page_ids:
            with open('dataFiles/{}/comments.csv'.format(page_id) , 'r') as pageIDFile:
                reader = csv.reader(pageIDFile)
                for row in reader:
                    writer.writerow(row)
    


if __name__ == '__main__':
    for category in zip(CATEGORIES, CATEGORY_NAMES):
        assemble_comments(category)


# The CSV can be opened in all major statistical programs. Have fun! :)
