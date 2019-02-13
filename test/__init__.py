REPORTINGSYSTEM = 'http://localhost:5000/reportingsystem/84a3bcfe-bdb6-4029-906d-e527182628c3'
def w_l(info,file="./logs/test.log"):
	f = open(file,"a+",encoding="utf-8")
	f.write(info)
	f.close()
