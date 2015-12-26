import urllib
import re
import socket

if __name__=='__main__':
    socket.setdefaulttimeout(10)
    
    htmlFile=open('index.txt','w') ##the entrance address
    url='http://www.zju.edu.cn/'
    htmlFile.write(urllib.urlopen(url).read())
    htmlFile.close()

    pattern='href="http://\S*\"'

    saveTxt=open('save.txt','w')
    htmlFile=open('index.txt','r')
    for line in htmlFile:
        text=line
        ma=re.search(pattern,text)
        if ma is not None :
            src=text[ma.start():ma.end()].split('"')[1]            
            saveTxt.write(src)
            saveTxt.write('\n')
    htmlFile.close()
    saveTxt.close()


    nameNum=1
    saveTxt=open('save.txt','r')
    for line in saveTxt:
        url=line
        print url
        name=str(nameNum)+".txt"
        htmlFile=open(name,'w')
        nameNum+=1
        try:
            htmlFile.write(urllib.urlopen(url).read())
        except:
            pass
        finally:
            htmlFile.close()        
    saveTxt.close()
    
