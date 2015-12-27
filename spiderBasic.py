import urllib
import re
import socket
import urlparse

def add(num):
    num+=1
    return num

def spiderWeb(url,count):
    if table.has_key(url):
        pass
    else:
        count=add(count)
        table[url]=count
        htmlFile=open((str(count)+'.txt'),'w')
        htmlFile.write(urllib.urlopen(url).read())
        htmlFile.close()
        
        pattern=re.compile('href="[^(javascript)]\S*[^(#)(css)(js)]\"')
        saveTxt=open('save.txt','w')
        htmlFile=open((str(count)+'.txt'),'r')
        for line in htmlFile:
            ans=re.findall(pattern,line)
            for one in ans :
                srcTail=one.split('"')[1]            
                src=urlparse.urljoin(url,srcTail)
                saveTxt.write(src)
                #print src
                saveTxt.write('\n')
        htmlFile.close()
        saveTxt.close()
        
        saveTxt=open('save.txt','r')
        for line in saveTxt:
            url=line.strip('\n')
            if table.has_key(url):
                print 'skip---'+url
            else:
                print 'download---'+url
                count=add(count)
                table[url]=count
                htmlFile=open((str(table[url])+'.txt'),'w')
                try:
                    htmlFile.write(urllib.urlopen(url).read())
                except:
                    pass
                finally:
                    htmlFile.close()
        saveTxt.close()

    urlMapFile=open('map.txt','w')
    for key in table.keys():
        urlMapFile.write(str(key)+'\t'+str(table[key])+'\n')
    urlMapFile.close()
    
    print 'success!'


if __name__=='__main__':
    socket.setdefaulttimeout(10)

    entrance='http://www.zju.edu.cn/'
    count=0
    table={}
    spiderWeb(entrance,count)
    



