import urllib.request
import urllib.parse
import json
import time


def main():
    weibo = [{'title': '暖医', 'link': 'https://s.weibo.com/weibo?q=%23%E6%9A%96%E5%8C%BB%23&Refer=new_time'}, {'title': '刘昊然陈都灵提名金扫帚奖', 'link': 'https://s.weibo.com/weibo?q=%23%E5%88%98%E6%98%8A%E7%84%B6%E9%99%88%E9%83%BD%E7%81%B5%E6%8F%90%E5%90%8D%E9%87%91%E6%89%AB%E5%B8%9A%E5%A5%96%23&Refer=top'}, {'title': '电子结婚证不具法律效力', 'link': 'https://s.weibo.com/weibo?q=%23%E7%94%B5%E5%AD%90%E7%BB%93%E5%A9%9A%E8%AF%81%E4%B8%8D%E5%85%B7%E6%B3%95%E5%BE%8B%E6%95%88%E5%8A%9B%23&Refer=top'}]

    tianqi = [[['19日（今天）', '小雨', '', '17℃'], ['20日（明天）', '小雨转多云', '23℃', '16℃'], ['21日（后天）', '阵雨转多云', '26℃', '16℃'], ['22日（周四）', '多云转小雨', '28℃', '15℃'], ['23日（周五）', '小雨转多云', '21℃', '15℃'], ['24日（周六）', '晴转多云', '29℃', '16℃'], ['25日（周日）', '多云', '26℃', '15℃']], [['19日（今天）', '晴', '', '29℃'], ['20日（明天）', '晴', '38℃', '29℃'], ['21日（后天）', '晴', '38℃', '29℃'], ['22日（周四）', '晴', '38℃', '29℃'], ['23日（周五）', '晴', '38℃', '30℃'], ['24日（周六）', '晴转多云', '38℃', '30℃'], ['25日（周日）', '多云', '36℃', '29℃']], [['19日（今天）', '晴', '', '23℃'], ['20日（明天）', '多云转晴', '32℃', '24℃'], ['21日（后天）', '多云', '34℃', '24℃'], ['22日（周四）', '多云', '34℃', '25℃'], ['23日（周五）', '多云', '34℃', '25℃'], ['24日（周六）', '多云', '34℃', '24℃'], ['25日（周日）', '多云', '30℃', '23℃']], [['19日（今天）', '雷阵雨', '', '26℃'], ['20日（明天）', '雷阵雨转阴', '31℃', '26℃'], ['21日（后天）', '雷阵雨', '32℃', '26℃'], ['22日（周四）', '雷阵雨', '32℃', '27℃'], ['23日（周五）', '雷阵雨', '34℃', '27℃'], ['24日（周六）', '雷阵雨', '33℃', '27℃'], ['25日（周日）', '雷阵雨', '33℃', '27℃']]]
    
    law = {'view': [['Use of Blockchain Technology in Cross-Border Legal Cooperation', 'http://conflictoflaws.net/2019/use-of-blockchain-technology-in-cross-border-legal-cooperation/'], ['Service of Process abroad: Lost in Translation', 'http://conflictoflaws.net/2019/service-of-process-abroad-lost-in-translation/'], ['First impressions from Kirchberg on the EAPO Regulation – Opinion of AG Szpunar in Case C-555/18', 'http://conflictoflaws.net/2019/first-impressions-from-kirchberg-on-the-eapo-regulation-opinion-of-ag-szpunar-in-case-c-555-18/']], 'new': [['The Role of Academia in Latin American Private International Law – September 10', 'http://conflictoflaws.net/2019/the-role-of-academia-in-latin-american-private-international-law-september-10/'], ['Vacancy at the Permanent Bureau of the HCCH: Administrative Assistant (Legal)', 'http://conflictoflaws.net/2019/vacancy-at-the-permanent-bureau-administrative-assistant-legal/'], ['Singapore Convention on Mediation', 'http://conflictoflaws.net/2019/singapore-convention-on-mediation/']]}
    
    def law_translate(law):
        url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
        head = {}
        head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3738.400'

        view_str = []
        view_content = law.get('view')
        for v_content in view_content:
            view_str.append(v_content[0])

        new_str = []
        new_content = law.get('new')
        for n_content in new_content:
            new_str.append(n_content[0])

        translation = []
        for each in view_str:
            data = {}
            data['i'] = each
            data['from'] = 'AUTO'
            data['to'] = 'AUTO'
            data['smartresult'] = 'dict'
            data['client'] = 'fanyideskweb'
            data['salt'] = '15658686268937'
            data['sign'] = 'ee53369f775bc53f8be7328d3afb3631'
            data['ts'] = '1565868626893'
            data['bv'] = 'b9bd10e2943f377d66e859990bbee707'
            data['doctype'] = 'json'
            data['version'] = '2.1'
            data['keyfrom'] = 'fanyi.web'
            data['action'] = 'FY_BY_REALTlME'
    
            data = urllib.parse.urlencode(data).encode('utf-8')
            req = urllib.request.Request(url, data, head)
            response = urllib.request.urlopen(req)
            html = response.read().decode('utf-8')
            target = json.loads(html)
            result = target['translateResult'][0][0]['tgt']
            translation.append(result)
        
        for each in new_str:
            data = {}
            data['i'] = each
            data['from'] = 'AUTO'
            data['to'] = 'AUTO'
            data['smartresult'] = 'dict'
            data['client'] = 'fanyideskweb'
            data['salt'] = '15658686268937'
            data['sign'] = 'ee53369f775bc53f8be7328d3afb3631'
            data['ts'] = '1565868626893'
            data['bv'] = 'b9bd10e2943f377d66e859990bbee707'
            data['doctype'] = 'json'
            data['version'] = '2.1'
            data['keyfrom'] = 'fanyi.web'
            data['action'] = 'FY_BY_REALTlME'
    
            data = urllib.parse.urlencode(data).encode('utf-8')
            req = urllib.request.Request(url, data, head)
            response = urllib.request.urlopen(req)
            html = response.read().decode('utf-8')
            target = json.loads(html)
            result = target['translateResult'][0][0]['tgt']
            translation.append(result)

        law_translate = []
        i = 0
        for l in law.get('view'):
            law_translate.append(l[0])
            law_translate.append(translation[i])
            law_translate.append(l[1])
            i += 1
        for l in law.get('new'):
            law_translate.append(l[0])
            law_translate.append(translation[i])
            law_translate.append(l[1])
            i += 1
        return law_translate

    law_translate = law_translate(law)
  
    weibo_text = []
    for w in weibo:
        w_text = '%s>>>%s' % (w.get('title'), w.get('link'))
        weibo_text.append(w_text)

    tianqi_city = []
    for t in tianqi[0]: 
        t_lanzhou = '兰州%s天气为%s，最高气温%s，最低气温%s' % (t[0], t[1], t[2], t[3])
        tianqi_city.append(t_lanzhou)
    for t in tianqi[1]:
        t_changsha = '长沙%s天气为%s，最高气温%s，最低气温%s' % (t[0], t[1], t[2], t[3])
        tianqi_city.append(t_changsha)
    for t in tianqi[2]:
        t_nanjing = '南京%s天气为%s，最高气温%s，最低气温%s' % (t[0], t[1], t[2], t[3])
        tianqi_city.append(t_nanjing)
    for t in tianqi[3]:
        t_hainan = '海南%s天气为%s，最高气温%s，最低气温%s' % (t[0], t[1], t[2], t[3])
        tianqi_city.append(t_hainan)

    text = ['天气>>>']
    for each in tianqi_city:
        text.append(each)
    text.append('微博热搜>>>')
    for each in weibo_text:
        text.append(each)
    text.append('Conflict of Laws>>>')
    for each in law_translate:
        text.append(each)

if __name__ == '__main__':
    main()