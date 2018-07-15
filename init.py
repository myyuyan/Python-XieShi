def init():
	print("开始")
	zifu=[]
	f=open("a.txt", encoding='utf-8')
	line=f.readline()
	while line:
		if len(line)==13:
			zifu.append(line)
		if len(line)==17:
			zifu.append(line)
		print((len(line)))
		print(line)
		line=f.readline()
	text=""
	print(zifu)
	print("读取完毕，写入中！")
	for te in zifu:
		text+=te
	file=open("text.txt","a+",encoding='utf-8')
	file.write(text)
	file.close()
	f.close()
	print("OK")
init()