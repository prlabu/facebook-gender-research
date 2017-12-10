import datetime
import csv
import time
import collections
import string
import pages



CATEGORIES = [pages.female_celebs, pages.general_feminine, pages.male_celebs, pages.general_masculine]
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

        # write header
        with open('dataFiles/{}/comments.csv'.format(category_page_ids[0]) , 'r') as pageIDFile:
                reader = csv.reader(pageIDFile)
                writer.writerow(reader.next())

        for page_id in category_page_ids:
            with open('dataFiles/{}/comments.csv'.format(page_id) , 'r') as pageIDFile:
                reader = csv.reader(pageIDFile)
                reader.next()
                for row in reader:
                    # skip the first comment in each file
                    writer.writerow(row)
    


if __name__ == '__main__':
    for category in zip(CATEGORIES, CATEGORY_NAMES):
        assemble_comments(category)


# The CSV can be opened in all major statistical programs. Have fun! :)
