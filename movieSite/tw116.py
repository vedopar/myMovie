from base import Website

class tw116(Website):
    def sd(self):
        return False
    def baseUrl(self):
        return 'http://www.tw116.com'
    def searchPageRegex(self):
        return '<dl><dt><a href=\"(?P<'+self.movieHrefGroupName()+'>.*?)\" target=\"_blank\">'
    def searchHref(self):
        return "/index.php?s=vod-search"
    def searchData(self,kw):
        return {
            'x':'name',
            'id':kw,
            'submit':'影片搜索',
            }
    def movieMetadataRegex(self):
        return '<div class=\"movie\"><img src=\"(?P<imageUrl>.*?)\".*?<>'
    def playerHrefRegex(self):
        return 'xigua</div>.*?<a href=\"(?P<'+self.playerHrefGroupName()+'>.*?)\" target=\"_blank\">'
    def playerPageRegex(self):
        return '(%2B|%24){3}(?P<'+self.sourceTypeGroupName()+'>.{1,21})%2B%2B(?P<'+\
            self.sourceUrlGroupName()+'>ftp.*?(mkv|mp4|rmvb))'
