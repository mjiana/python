# 자연어 읽고 쓰기
# nltk 설치 - 자연어 패키지
# import nltk
from nltk import word_tokenize
from nltk import Text
# nltk.download() # 1회만 실행

tokens = word_tokenize("Here is some not very interesting text")
text = Text(tokens)
print(text)
# 결과 : <Text: Here is some not very interesting text...>


# 빈도 분석 1
from nltk.book import *  # 아홉권의 책을 불러온다.
from nltk import ngrams
fourgrams = ngrams(text6, 4)  # 6번째 책으로 4 gram 만들기
for fg in fourgrams:
    if fg[0] == "coconut":
        print(fg)  # ('coconut', 'and', 'you', "'")


# 빈도 분석 2
from nltk.book import text6
from nltk import ngrams
fourgrams = ngrams(text6, 4)  # 6번째 책으로 4 gram 만들기
fourgramDist = FreqDist(fourgrams)
print(fourgramDist["father", "smelt", "of", "elderberries"])
# 결과 : 1


# 빈도분석 3
from nltk.book import text6
from nltk import FreqDist
fdist = FreqDist(text6)
print(fdist.most_common(10))  # 빈도수가 많은 것 10개 출력
# 결과 : [(':', 1197), ('.', 816), ...(생략)...


# 자연어 분석 : 품사 구분
from nltk import word_tokenize, sent_tokenize, pos_tag
# 자연어 문장
senteces = sent_tokenize("Google is one of the best companies in the world. "
                         " I constantly google myself to see what I'm up to.")
# print(pos_tag(senteces))

# NN 단수명사, NNS 복수명사, NNP 단수형 고유명사, NNPS 복수형 고유명사
nouns = ["NN", "NNS", "NNP", "NNPS"]

for st in senteces:
    if "google" in st.lower():  # 소문자로 변경 비교
        taggedWords = pos_tag(word_tokenize(st))  # 문자열을 잘라서 태그(NN, NNS..) 붙임
        for word in taggedWords:
            if word[0].lower() == "google" and word[0] in nouns:
                print(word)  # sent_tokenize일때 명사인 경우 출력
                # print(senteces)  # word_tokenize일때

# test
senteces = word_tokenize("Google is one of the best companies in the world. "
                         "I constantly google myself to see what I'm up to. ")
words = pos_tag(senteces)
print(words)  # [('Google', 'NNP'), ('is', 'VBZ'), ('one', 'CD'), ...

