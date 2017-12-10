import datetime
import csv
import time
import collections
import string
import stopwords


REMOVE_STOPS = False

# PAGES = [
#     'barbie',
#     'breakingbad',
#     'cnn',
#     'lego',
#     'pinterest',
#     'reddit',
#     'sexandthecity',
#     'taylorswift',
#     'zacefron',
#     'robertdowneyjr',
#     'mileycyrus', 
#     'beyonce', 
#     'justinbieber', 
#     'adele', 
#     'selenagomez', 
#     'jayz', 
#     'eminem', 
#     'justintimberlake',
#     'female_celebs', 
#     'general_feminine',
#     'male_celebs',
#     'general_masculine'
#     ]

# all pages
PAGES = [
    'adele', 
    'barbie',
    'beyonce',
    'breakingbad',
    'cnn',
    'eminem',
    'female_celebs',
    'general_feminine',
    'general_masculine',
    'jayz',
    'justinbieber',
    'justintimberlake',
    'lego',
    'male_celebs',
    'mileycyrus',
    'pinterest',
    'reddit',
    'robertdowneyjr',
    'selenagomez',
    'sexandthecity',
    'taylorswift',
    'zacefron'
]

# OR 
# PAGES = [
#     'female_celebs', 
#     'general_feminine',
#     'male_celebs',
#     'general_masculine'
#     ]

# comments_file_id = "dataFiles/breakingbad/comments_2017-01-01_2017-06-01.csv"


def unicode_decode(text):
    try:
        return text.encode('utf-8').decode()
    except UnicodeDecodeError:
        return text.encode('utf-8')


def getWordFrequencies(comments_file_id):
    frequDict = collections.defaultdict(int)
    author_frequ_dict = collections.defaultdict(int)
    num_comments = 0
    num_tokens = 0
    
    with open(comments_file_id , 'r') as file:
        reader = csv.DictReader(file)

        scrape_starttime = datetime.datetime.now()
        after = ''

        print("Processing Comments From  {}: {}\n".format(
            comments_file_id, scrape_starttime))


        for row in reader:
            comment = row['comment_message']
            author_first_name = row['comment_author'].split()[0]
            author_frequ_dict[author_first_name] += 1
            num_comments += 1

            tokens = comment.lower().split()
            num_tokens += len(tokens)

            for token in tokens:
                frequDict[token.translate(None, string.punctuation)] += 1
    
    # tokens in comments
    kvList = frequDict.items()
    filtered = [list(kv) for kv in kvList if kv[1] > 1]
    sortedList = sorted(filtered, key=lambda kv: kv[1] , reverse=True)
    extendedInfo = [ [lst[0], lst[1], '{:.4f}'.format(float(lst[1]) / num_comments * 100), '{:.4f}'.format(float(lst[1]) / num_tokens * 100)] for lst in sortedList]

    # remove 'stop words' that are non-lexical... used for grammatical purposes
    if REMOVE_STOPS:
        extended_info_no_stops = [token for token in extendedInfo if token[0] not in stopwords.stopwords]
        with open( str('frequencies_removed_stops').join( comments_file_id.split('comments') ) , 'w') as frequencyFile:
            w = csv.writer(frequencyFile, dialect='excel')
            w.writerow(['token', 'count','frequencyPer100Comment','frequencyPer100Token'])
            w.writerows(extended_info_no_stops)
    else:
        # writing frequencies to file
        with open( str('frequencies').join( comments_file_id.split('comments') ) , 'w') as frequencyFile:
            w = csv.writer(frequencyFile, dialect='excel')
            w.writerow(['token', 'count','frequencyPer100Comment','frequencyPer100Token'])
            w.writerows(extendedInfo)

    # author frequencies
    author_kv_list = author_frequ_dict.items()
    authors_filtered = [list(kv) for kv in author_kv_list if kv[1] > 1]
    authors_sortedList = sorted(authors_filtered, key=lambda kv: kv[1] , reverse=True)
    authors_extendedInfo = [ [lst[0], lst[1], '{:.4f}'.format(float(lst[1]) / num_comments * 100)] for lst in authors_sortedList]

    # writing author frequencies to file
    with open( str('author_frequencies').join( comments_file_id.split('comments') ) , 'w') as frequencyFile:
        w = csv.writer(frequencyFile, dialect='excel')
        w.writerow(['author_name', 'frequency','frequencyPer100Comment'])
        w.writerows(authors_extendedInfo)

    # writing comments summary to file
    with open( str('comments_summary').join( comments_file_id.split('comments') ) , 'w') as summaryFile:
        w = csv.writer(summaryFile, dialect='excel')
        w.writerow(['page_id', 'numComments','avgCommentLength'])
        w.writerow( 
            [comments_file_id.split("/")[1], 
            num_comments, 
            '{:.4f}'.format(float(num_tokens) / float(num_comments))] )
    

    


if __name__ == '__main__':
    for page in PAGES:
        getWordFrequencies('dataFiles/' + page + '/comments.csv')


# The CSV can be opened in all major statistical programs. Have fun! :)
