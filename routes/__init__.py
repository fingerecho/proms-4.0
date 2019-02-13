
def w_l(info,file="log/test.log"):
	f = open(file,"a+",encoding="utf-8")
	f.write("\n")
	f.write(info)
	f.write("\n")
	f.close()
