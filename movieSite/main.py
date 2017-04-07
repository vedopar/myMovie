'''
Created on Apr 5, 2017

@author: vedopar
'''

from tw116 import tw116

if __name__ == '__main__':
    kw='毒枭'
    w=tw116()
    for m in w.search(kw):
        print(m.ma)
        #for s in m.ms:
        #    print(s)
    