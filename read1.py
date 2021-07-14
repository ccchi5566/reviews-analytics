data = []
count = 0
with open('amazon.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('總共', len(data), '筆資料')

print(data[0])


wc = {} # word_count
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #新增新的key進wc字典

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))
print(wc['Allen'])

while True:
	word = input('請問要查什麼字:')
	if word == 'q':
		print('已退出')
		break
	if word in wc:
		print(word, '出現過的次數為:', wc[word])
	else:
		print(word, '沒出現過')












# sum_len = 0
# for d in data:
# 	sum_len = sum_len + len(d)
# print('留言平均是', sum_len / len(data))

# #篩選小於100字的留言
# new = []
# for d in data:
# 	if len(d) < 100:
# 		new.append(d) #小於100字的留言把它裝進new清單裡
# print('一共有', len(new), '筆留言長度小於100')
# print(new[0]) #隨便印一筆字數小於100的留言


# #篩選出含有good的留言數
# good = []
# for d in data:
# 	if 'good' in d:
# 	    good.append(d)
# print('一共有', len(good), '筆留言提到good')
# print(good[0]) #隨便印一筆提到good的


