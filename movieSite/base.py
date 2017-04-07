import urllib,urllib.parse,urllib.request
import re
import logging

class MovieSource(object):
    def __init__(self,type,url):
        self.type=urllib.parse.unquote(type)
        self.url=urllib.parse.unquote(url)
    
    def __str__(self):
        return '\ntype:\t'+self.type+'\turl:\t'+self.url
        
class Movie(object):
    def __init__(self,ma,ms):
        self.ma=ma
        self.ms=ms
        
    def __doc__(self):
        return 'Information for a movie, ma stands for metadata, ms stands for movie source'
        
    def __str__(self):
        return str(self.groupDict)+'\n'+str(ms for ms in self.sources)
    
class Website(object):
    
    def sd(self):
        return True
    def ld(self, d):
        if self.sd():
            print(d)
        
    def baseUrl(self):
        return 'path.to.overwrite'
    
    def searchHref(self):
        return 'search.href.to.overwrite'
    
    def searchData(self, kw):
        return {}
    
    def searchPageRegex(self):
        return 'search.page.regex.to.overwrite'
    
    def movieHrefGroupName(self):
        return 'movieHref'
    
    def search(self, kw):
        data=self.searchData(kw)
        self.ld('reqData:'+str(data))
        data=urllib.parse.urlencode(data).encode('ascii')
        url=self.baseUrl()+self.searchHref()
        f=urllib.request.urlopen(url,data=data)
        self.ld('url:'+url)
        r=f.read().decode('utf-8')
        f.close()
        self.moviePages=[]
        self.ld('regex:'+self.searchPageRegex())
        movies=[]
        for i in re.finditer(self.searchPageRegex(),r):
            movieHref=i.group(self.movieHrefGroupName())
            self.ld('movie-href:'+movieHref)
            movie=self.movieFromMoviePage(movieHref)
            if movie!=None:
                movies.append(movie)
        return movies
    
    def movieMetadataRegex(self):
        return 'movie.metadata.regex.to.overwrite'
    
    def playerHrefRegex(self):
        return 'player.href.regex.to.overwrite'
    
    def playerHrefGroupName(self):
        return 'playerHref'
    
    def movieFromMoviePage(self, movieHref):
        self.ld('In movieFromMoviePage')
        url=self.baseUrl()+movieHref
        self.ld('full-url:'+url)
        f=urllib.request.urlopen(url)
        r=f.read().decode('utf-8').replace('\n','')
        f.close()
        
        #Get metadata
        reg=self.movieMetadataRegex()
        self.ld('movieMetadataRegex:'+reg)
        i=re.search(reg,r)
        ma=None
        if i!=None:
            ma=i.groupdict()
            self.ld('metadata:'+str(ma))
        
        #Get player page href
        reg=self.playerHrefRegex()
        self.ld('playerHrefRegex:'+reg)
        i=re.search(reg,r)
        if i is None:
            return None
        
        #Get movie source
        return Movie(ma, self.movieSourceFromPlayerPage(i.group(self.playerHrefGroupName())))
    
    def playerPageRegex(self):
        return 'player.page.regex.to.overwrite'
    
    
    def sourceTypeGroupName(self):
        return 'msType'
    
    def sourceUrlGroupName(self):
        return 'msUrl'
    
    def movieSourceFromPlayerPage(self,pHref):
        self.ld('In movieSourceFromPlayerPage')
        url=self.baseUrl()+pHref
        self.ld('full-url:'+url)
        f=urllib.request.urlopen(url)
        r=f.read().decode('utf-8')
        f.close()
        mss=[]
        reg=self.playerPageRegex()
        self.ld('playerPageRegex:'+reg)
        for i in re.finditer(reg,r):
            ms=MovieSource(i.group(self.sourceTypeGroupName()),i.group(self.sourceUrlGroupName()))
            self.ld('ms:'+str(ms))
            mss.append(ms)
        return mss
