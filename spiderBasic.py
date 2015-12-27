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
        htmlFile=open((str(count)+'.txt'),'r')
        for line in htmlFile:
            ans=re.findall(pattern,line)
            for one in ans :
                urlTail=one.split('"')[1]            
                url=urlparse.urljoin(url,urlTail)
                if table.has_key(url):
                    print 'skip---'+url
                else:
                    print 'download---'+url
                    count=add(count)
                    table[url]=count
                    catchFile=open((str(table[url])+'.txt'),'w')
                    try:
                        catchFile.write(urllib.urlopen(url).read())
                    except:
                        pass
                    finally:
                        catchFile.close()               
        htmlFile.close()
        

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
    



