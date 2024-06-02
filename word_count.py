from optparse import OptionParser

class WordCount(object):

    def __init__(self,config_dict={}):
        self.dwords = dict()
        self.count  = int(config_dict['count'])
        self.file   = open(config_dict['file'])

    def counter(self):
        for word in sum([line.strip().split(' ') for line in self.file.readlines()],[]):
            if word in self.dwords.keys(): self.dwords[word] += 1
            else: self.dwords[word] = 1
        return list(dict(sorted(self.dwords.items(), key=lambda item: item[1], reverse=True)).items())[:self.count]

if __name__ == '__main__':

    # file -> '/home/anthony/Documents/TXT/WhatsApp/madelin.txt'

    # The line below removes emojies and unicode chars from file
    #iconv -f utf8 -t ascii//TRANSLIT < madelin.txt > madelin-converted.txt

    parser = OptionParser()
    parser.add_option('-C', '--count',
        dest='count', type='int', default=100,
        help='Top number of most used words to return.')
    parser.add_option('--file',
        dest='file',
        default='/home/anthony/Documents/TXT/WhatsApp/madelin.txt',
        help='File used to count words.')
    (options, args) = parser.parse_args()

    config_dict = {
        'file':  options.file,
        'count': options.count,
    }

    word_count = WordCount(config_dict)
    print(word_count.counter()) 
