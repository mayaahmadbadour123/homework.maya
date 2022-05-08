filename = 'D:\mm\quizm.txt'
print('..open file using read method')
infile=open(filename,'r')
s=infile.read()
print(s,type(s))
