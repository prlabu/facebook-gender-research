import datetime
import csv
import time
import collections
import string

# PAGES = [ 'barbie' ,
# 'breakingbad' ,
# 'cnn' ,
# 'lego' ,
# 'pinterest' ,
# 'reddit' ,
# 'sexandthecity' ,
# 'taylorswift' ,
# 'zacefron'
# ]
# OR 
PAGES = ['taylorswift']

# comments_file_id = "dataFiles/breakingbad/comments_2017-01-01_2017-06-01.csv"


def unicode_decode(text):
    try:
        return text.encode('utf-8').decode()
    except UnicodeDecodeError:
        return text.encode('utf-8')


def getWordFrequencies(comments_file_id):
    frequDict = collections.defaultdict(int)
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
            num_comments += 1

            tokens = comment.lower().split()
            num_tokens += len(tokens)

            for token in tokens:
                frequDict[token.translate(None, string.punctuation)] += 1
    

    # writing frequencies to file
    with open( str('frequencies').join( comments_file_id.split('comments') ) , 'w') as frequencyFile:
        w = csv.writer(frequencyFile, dialect='excel')
        kvList = frequDict.items()
        filtered = [list(kv) for kv in kvList if kv[1] > 1]
        sortedList = sorted(filtered, key=lambda kv: kv[1] , reverse=True)
        
        
        print 'num_comments: {}'.format(num_comments)
        extendedInfo = [ [lst[0], lst[1], float(lst[1]) / num_comments, float(lst[1]) / num_tokens] for lst in sortedList]

        w.writerow(['token', 'count','frequencyPerComment','frequencyPerToken'])
        w.writerows(extendedInfo)


if __name__ == '__main__':
    for page in PAGES:
        getWordFrequencies('dataFiles/' + page + '/comments.csv')


# The CSV can be opened in all major statistical programs. Have fun! :)
