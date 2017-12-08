import datetime
import csv
import time
import collections
import string

comments_file_id = "dataFiles/breakingbad/comments_2017-01-01_2017-06-01.csv"


def unicode_decode(text):
    try:
        return text.encode('utf-8').decode()
    except UnicodeDecodeError:
        return text.encode('utf-8')




def processFacebookComment(comment, status_id, parent_id=''):

    # The status is now a Python dictionary, so for top-level items,
    # we can simply call the key.

    # Additionally, some items may not always exist,
    # so must check for existence first

    comment_id = comment['id']
    comment_message = '' if 'message' not in comment or comment['message'] \
        is '' else unicode_decode(comment['message'])
    comment_author = unicode_decode(comment['from']['name'])
    num_reactions = 0 if 'reactions' not in comment else \
        comment['reactions']['summary']['total_count']

    if 'attachment' in comment:
        attachment_type = comment['attachment']['type']
        attachment_type = 'gif' if attachment_type == 'animated_image_share' \
            else attachment_type
        attach_tag = "[[{}]]".format(attachment_type.upper())
        comment_message = attach_tag if comment_message is '' else \
            comment_message + " " + attach_tag

    # Time needs special care since a) it's in UTC and
    # b) it's not easy to use in statistical programs.

    comment_published = datetime.datetime.strptime(
        comment['created_time'], '%Y-%m-%dT%H:%M:%S+0000')
    comment_published = comment_published + datetime.timedelta(hours=-5)  # EST
    comment_published = comment_published.strftime(
        '%Y-%m-%d %H:%M:%S')  # best time format for spreadsheet programs

    # Return a tuple of all processed data

    return (comment_id, status_id, parent_id, comment_message, comment_author,
            comment_published, num_reactions)

def writeFrequencies(frequencyDict, comments_file_id):
    with open( str('frequencies').join( comments_file_id.split('comments') ) , 'w') as frequencyFile:
        w = csv.writer(frequencyFile, dialect='excel')
        kvList = frequencyDict.items()
        filtered = [kv for kv in kvList if kv[1] > 1]
        sortedList = sorted(filtered, key=lambda kv: kv[1] , reverse=True)

        w.writerow(['token', 'frequency'])
        w.writerows(sortedList)



def getWordFrequencies(comments_file_id):
    frequDict = collections.defaultdict(int)
    
    with open(comments_file_id , 'r') as file:
        reader = csv.DictReader(file)

        num_processed = 0
        scrape_starttime = datetime.datetime.now()
        after = ''

        print("Processing Comments From  {}: {}\n".format(
            comments_file_id, scrape_starttime))


        for row in reader:
            comment = row['comment_message']

            tokens = comment.lower().split()

            for token in tokens:
                frequDict[token.translate(None, string.punctuation)] += 1
    
    writeFrequencies(frequDict, comments_file_id)


if __name__ == '__main__':
    getWordFrequencies(comments_file_id)


# The CSV can be opened in all major statistical programs. Have fun! :)
