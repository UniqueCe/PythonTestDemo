import re, ssl
from urllib import request

class Spider():

    url = 'https://www.panda.tv/cate/lol?pdt=1.24.s1.3.7o59306rkul'
    root_pattern = '<div class="video-info">([\\s\\S]*?)</div>'
    name_pattern = '</i>([\\s\\S]*?)</span>'
    number_pattern = '<span class="video-number">([\\s\\S]*?)</span>'


    def __fetch_content(self):

        con = ssl._create_unverified_context()
        r = request.urlopen(Spider.url, context=con)
        htms = r.read()
        htms = str(htms, encoding= 'utf-8')
        return htms


    def __anakysis(self, htmls):

        root_html = re.findall(self.root_pattern, htmls)

        anchors = []
        for html in root_html:
            name = re.findall(self.name_pattern, html)
            number = re.findall(self.number_pattern, html)
            anchors.append({'name':name, 'number':number})

        return anchors


    def __refine(self, anchors):

        l = lambda anchor: {
                            'name':anchor['name'][0].strip(),
                            'number':anchor['number'][0]
                            } 
        return map(l, anchors)


    def __sort__seed(self, anchor):

        r = re.findall('\\d*', anchor['number'])
        number = float(r[0])
        
        if '万' in anchor['number']:
            number *= 10000

        return number


    def __sort(self, anchors):

        anchors = sorted(anchors, key=self.__sort__seed, reverse=True)
        return anchors


    def __show(self, anchors):

        for rank in range(0, len(anchors)):
            print('排名' 
                + ': '
                + str(rank + 1) 
                + '名 -- 主播名字: ' 
                + anchors[rank]['name'] 
                + ' -- 观看人数: ' 
                + anchors[rank]['number'] 
                + '人')
    

    def go(self):

        htmls = self.__fetch_content()
        anchors = self.__anakysis(htmls)
        anchors = list(self.__refine(anchors))
        anchors = self.__sort(anchors)
        self.__show(anchors)


if __name__ == '__main__':
    sp = Spider()
    sp.go()


'''
<div class="video-info">\n
<span class="video-title" title="抽200全皮肤0-17送人头快乐炼金">抽200全皮肤0-17送人头快乐炼金</span>\n    
<span class="video-nickname" title="lol稳贱骨炼金">\n                                                                                    
<i class="icon-host-level icon-host-level-10" data-level="10">
</i>\n lol稳贱骨炼金 </span>\n                                                    
<span class="video-number">13.4万</span>\n                                                   
<span class="video-station-info">\n                            
<i class="video-station-num">68人</i>\n                                                        
</span>\n                                                  
</div>


{'name': ['\n Lok795224', '\n'], 'number': ['15']}
'''