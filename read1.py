data = []
count = 0
with open('amazon.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('總共', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('留言平均是', sum_len / len(data))

#篩選小於100字的留言
new = []
for d in data:
	if len(d) < 100:
		new.append(d) #小於100字的留言把它裝進new清單裡
print('一共有', len(new), '筆留言長度小於100')
print(new[0]) #隨便印一筆字數小於100的留言
