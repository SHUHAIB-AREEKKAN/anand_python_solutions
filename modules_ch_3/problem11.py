import sys
import zipfile

def zips(name,files):
	sec=zipfile.ZipFile(name,'w')
	for i in files:
		sec.write(i)

if __name__ == '__main__':
	name=sys.argv[1]
	files=[sys.argv[k] for k in range(2,len(sys.argv))]
	print name,files
	zips(name,files)
	
	
