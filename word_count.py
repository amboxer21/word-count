class WordCount(object):

    def __init__(self,file,count=1,dwords={}):
        count       = count
        self.dwords = dwords
        self.file   = open(file) 

    def count(self): 
        for word in sum([line.strip().split(' ') for line in self.file.readlines()],[]):
            if word in self.dwords.keys(): self.dwords[word] += 1
            else: self.dwords[word] = 1
        return list(dict(sorted(self.dwords.items(), key=lambda item: item[1], reverse=True)).items())[:100]

if __name__ == '__main__':
    # The line below removes emojies and unicode chars
    #iconv -f utf8 -t ascii//TRANSLIT < madelin.txt > madelin-converted.txt
    word_count = WordCount('/home/anthony/Documents/TXT/WhatsApp/madelin.txt')
    print(word_count.count()) 
