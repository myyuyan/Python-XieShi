import pinyin
def init():
	zifu=[]
	ge=[]
	jieguo=""
	n=0
	f=open("text.txt", encoding='utf-8')
	line=f.readline()
	while line:
		zifu.append(line)
		line=f.readline()
	f.close()
	geshi=input("1、绝句2、律诗")
	geshi2=input("1、五言2、七言")
	geshi3=input("韵脚为：")
	if geshi=="1":
		if geshi2=="1":
			for te in zifu:
				if len(te)==13:
					ge.append(te)
			for text in ge:
				ls=list(text)
				if pinyin.get(ls[10],format="strip").endswith(geshi3):
					jieguo+=text+"\r\n"
					n+=1
				if n==2:
					print(jieguo)
					print("韵脚为："+geshi3)
					break
		else:
			for te in zifu:
				if len(te)==17:
					ge.append(te)
			for text in ge:
				ls=list(text)
				if  pinyin.get(ls[14],format="strip").endswith(geshi3):
					jieguo+=text+"\r\n"
					n+=1
				if n==2:
					print(jieguo)
					print("韵脚为："+geshi3)
					break
	else:
		if geshi2=="1":
			for te in zifu:
				if len(te)==13:
					ge.append(te)
			for text in ge:
				ls=list(text)
				if  pinyin.get(ls[10],format="strip").endswith(geshi3):
					jieguo+=text+"\r\n"
					n+=1
				if n==4:
					print(jieguo)
					print("韵脚为："+geshi3)
					break
		else:
			for te in zifu:
				if len(te)==17:
					ge.append(te)
			for text in ge:
				ls=list(text)
				if  pinyin.get(ls[14],format="strip").endswith(geshi3):
					jieguo+=text+"\r\n"
					n+=1
				if n==4:
					print(jieguo)
					print("韵脚为："+geshi3)
					break
init()