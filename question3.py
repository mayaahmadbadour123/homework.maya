def main():
    x=['true','true','true']
    
    outfile=open("D:\mm\new answers.txt",'w')
    newline=outfile.write('the answers:')
    print('the answers for the quiz:',x)
def createWithWrite(outfile):
    
    
    outfile.write(x)
    outfile.close()


