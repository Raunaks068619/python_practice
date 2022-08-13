f = open("FH1.txt", "r")

while(True):

	line = f.readline()
	if not line:
		break
	print(line.strip())
f.close
