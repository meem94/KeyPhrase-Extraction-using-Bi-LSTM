import re
import nltk
#sentence_delimiters = re.compile(u'[\\[\\]\n.!?,;:\t\\-\\"\\(\\)\\\'\u2019\u2013]')
nltk.download()
sentence_delimiters = re.compile(u'[৷\u002f\u0053\u0056\u00a0\u00ad\u00d0\u00da\u00e6\u00f2\u00f3\u2013\u2014\\[\\]\n!?,;:\।\t\\"\\(\\)\\\'\‘\‘‘]')
text = ''
text.encode(encoding='utf8')
text = 'ছোটবেলার স্মৃতি আজও আমাদের নাড়া দেয়, অতীতের সঙ্গে বর্তমানের যোগসূত্র গড়ে তোলে৷ কিন্তু সেই স্মৃতি আচমকা হারিয়ে গেলে পায়ের তলা থেকে যেন মাটি সরে যায়৷ '
sentences = nltk.sent_tokenize('i am meem.akd.')
#sentences = sentence_delimiters.split(text)
print(sentences, file=open("o.txt", "a", encoding='utf8'))
