fw = open('aman.html','w')
fw.write('<html> <head> </head> </html>')
fw.close()

fr = open('aman.html','r')
text = fr.read()
lines = text.split(' ')
for abc in lines :
    print(abc)
fr.close
#str ='my name is aman '  str.split(' ')
