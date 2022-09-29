'''
pip install simhash==2.1.2
https://github.com/1e0ng/simhash

https://www.jianshu.com/p/1187fb7c59c5 for chinese - 短文本不太 work 長文本比較 work 要注意 distance
'''

import re
from simhash import Simhash, SimhashIndex
import jieba


def ngram_from_list(input : list,n=3) -> list:
	return [''.join(input[i:i + n]) 
			for i 
			in range(max(len(input) - n + 1, 1)
			)
	]

def ngram_from_string(s : str,n=3) -> list:
	s = s.lower()
	s = re.sub(r'[^\w]+', '', s)
	return [s[i:i + n] for i in range(max(len(s) - n + 1, 1))]

def cut(s : str, stopwords : list = None) -> list:
	if stopwords is None:
		stopwords = []
	stopwords = set(stopwords + [''])
	return [e for e in jieba.lcut(s,cut_all=True) if e.strip() not in stopwords]




if __name__ == '__main__':


	raw_data = [
	u'How are you? I Am fine. blar blar blar blar blar Thanks.',
	u'How are you i am fine. blar blar blar blar blar than',
	'燒肉',
	'【2022行事曆(民國111年)】一張表秒懂國定假日,連假補班',
	u'This is simhash test.'
	]


	processed = [
		(s,
		cut(s),
		Simhash(cut(s))
		)
		for s in raw_data
		]
	
	for p in processed:
		print(p[0],p[1])
	
	index = SimhashIndex(
		[(p[0], p[2]) for p in processed],
		 k=10
		 )

	print(index.bucket_size())

	for s in [
		'How are you i am fine. blar blar blar blar blar thank',
		'燒肉',
		'【2023行事曆(民國112年)】一張表秒懂國定假日,連假補班'
		]:

	
		# hashed = Simhash(ngram_from_list(cut(s)))
		hashed = Simhash(cut(s))
		print(f'src : {s}','find duplicates : ', index.get_near_dups(hashed), sep='\n')
		print()

	# use jieba for chinese
	for p in [
		(u'How are you? I Am fine. blar blar blar blar blar Thanks.',
		u'How are you i am fine. blar blar blar blar blar than'),
		(u'燒肉丼',u'燒肉丼'),
		(u'【2023行事曆(民國112年)】一張表秒懂國定假日,連假補班',u'【2022行事曆(民國111年)】一張表秒懂國定假日,連假補班')

	]:
		print(p)
		print('jieba : ')
		print(
			Simhash(
				jieba.lcut(p[0],cut_all=True)
			).distance(
				Simhash(jieba.cut(p[1],cut_all=True))
			)
		)
		print('ngram : ')
		print(
			Simhash(
				ngram_from_list(p[0])
			).distance(
				Simhash(ngram_from_list(p[1]))
			)
		)

		print('ngram after jieba : ')

		print(
			Simhash(
				ngram_from_list(cut(p[0]))
			).distance(
				Simhash(ngram_from_list(cut(p[1])))
			)
		)
