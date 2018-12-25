import sys

from urllib.request import urlopen
import string
import collections
import urllib.error
def exchange():#查询的函数
    doc = urlopen(sys.argv[1])
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode()
    return jstr#返回从网页上获得的信息（字符串）
def wcount(k):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    lst=exchange().lower()
    a=lst.strip().replace('\n', ' ').replace('\t', ' ').replace('\r', ' ').strip()
    b=''
    for i in a:
        if i in string.punctuation:
            b+=' '
        else:
            b+=i

    nov=b.split()
    
    dic=collections.Counter(nov)
    lsttt=dic.most_common(k)
    for i in range(k):
        print(fo(*lsttt[i]),ba(*lsttt[i]))
def fo(x,y):
    return x
def ba(x,y):
    return y


if __name__ == '__main__':

    if  len(sys.argv) == 1:

        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    else: 
        try:#尝试
            doc = urlopen(sys.argv[1])
            docstr= doc.read()
            doc.close()
        except ValueError:# 报错
            print('网址输入格式错误')
        except urllib.error.URLError:
            print('网络连接错误')
        except urllib.error.HTTPError:
            print('错误 404: Not Found.')
        else:
            if len(sys.argv)==3:
                try:
                    x=int(sys.argv[2])
                except ValueError:
                    print('数字输入有误')
                x=int(sys.argv[2])  
                wcount(x)
                
            else:
                wcount(10)
