#coding: utf-8
import requests
import os
import time
import json

def display_data(data1,data2):
    print_data = ''
    for i in range(len(data1)-1):
        print_data += data2[i+1]+'\n'+data1[i+1]+'\n'
    return data1[0],print_data


def trans_word(data):
    datas = str(data)
    url = f'https://dict.youdao.com/suggest?num=5&ver=3.0&doctype=json&cache=false&le=en&q={datas}'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
    response = requests.get(url,headers=header)
    result = json.loads(response.text)['data']['entries']
    data_explain = []
    data_entry = []
    for qy in result:
        data_explain.append(qy['explain'])
        data_entry.append(qy["entry"])
    put1,put2 = display_data(data_explain,data_entry)
    print(put1)
    return put1,put2


def trans_text(text_data):
    text_datas = str(text_data)
    url = 'https://dict.youdao.com/jsonapi_s?doctype=json&jsonversion=4'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
    data = {'q': text_datas,
    'le':'en',
    'client':'web',
    'keyfrom': 'webdict'}
    response = requests.post(url = url,headers=header,data=data)
    result = json.loads(response.text)["fanyi"]["tran"]
    print(result)
    return result

def trans_baidu(data_word):
    data_words = data_word
    data = {'kw': data_words}
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
    url = 'https://fanyi.baidu.com/sug'
    response = requests.post(url,headers=header,data=data)
    result = response.json()['data']
    data_explain = []
    data_entry = []
    for qy in result:
        data_explain.append(qy['v'])
        data_entry.append(qy["k"])
    put1,put2 = display_data(data_explain,data_entry)
    print(put1)
    return put1,put2

data = {
'from': 'zh',
'to': 'en',
'query': '月入过万是什么水平',
'transtype': 'translang',
'simple_means_flag': '3',
'sign': '816679.562454',
'token': 'e9e4b9771dbfb4e73fd1b208f0d341cc',
'domain': 'common'}
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36','Cookie': 'BIDUPSID=27603618680047008EB238DC627F3760; PSTM=1605191454; BDUSS_BFESS=Hhpc1RWcElpdVZZYmpxU0Z6UWdhTUl1eGNrLS1CMnh6WkdFVkh3VXdHQzB5MWhrRUFBQUFBJCQAAAAAAAAAAAEAAAD1Jcldxq7D7L2js9UAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALQ-MWS0PjFkN; BAIDUID=C288B4E6287E9430FC98201D3D16207B:FG=1; BAIDUID_BFESS=C288B4E6287E9430FC98201D3D16207B:FG=1; ZFY=pvrT3shOawh92y4gDlG28ASBckcqTwatRgXB2UshdeI:C; BDRCVFR[wjT78r1YDGs]=IdAnGome-nsnWnYPi4WUvY; BA_HECTOR=8lalagal85a084al0g208hfn1i47t711n; PSINO=2; delPer=0; BCLID=6595020432667317902; BCLID_BFESS=6595020432667317902; BDSFRCVID=pH0OJexroG07VWbf8YYitKq72uweG7bTDYrE1k12eFgi6oAVFe3JEG0Pts1-dEu-S2OOogKK0mOTHvKF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; BDSFRCVID_BFESS=pH0OJexroG07VWbf8YYitKq72uweG7bTDYrE1k12eFgi6oAVFe3JEG0Pts1-dEu-S2OOogKK0mOTHvKF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tRAOoC_-tDvtHJrwMDTD-tFO5eT22-us-g-j2hcHMPoosIt63lJDb6k4WfrJBb_ftjTf0l05KfbUotoHDt4aD4LzbUuq2Mop3DIeaq5TtUJMqIDzbMohqqJXXPnyKMnitIj9-pnKWhQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKu-n5jHjQ0DGuH3j; H_BDCLCKID_SF_BFESS=tRAOoC_-tDvtHJrwMDTD-tFO5eT22-us-g-j2hcHMPoosIt63lJDb6k4WfrJBb_ftjTf0l05KfbUotoHDt4aD4LzbUuq2Mop3DIeaq5TtUJMqIDzbMohqqJXXPnyKMnitIj9-pnKWhQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKu-n5jHjQ0DGuH3j; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1682175216; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1682175216; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDRCVFR[S6sX_uClGsn]=mk3SLVN4HKm; BDRCVFR[S4-dAuiWMmn]=nQF83UoKQn0fj63njb1nWRkg1Tsgv99; H_PS_PSSID=38516_36546_38470_38351_38468_38485_37932_38356_26350_38185; ariaDefaultTheme=null; RT="z=1&dm=baidu.com&si=d04e98d6-2416-4acd-a5af-3b010ce591de&ss=lgs4tm40&sl=1&tt=2d4&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=35q&ul=3ve&hd=3vu"; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; ab_sr=1.0.1_YmFjMmU3MDQ1OWU0YTRkZDNhZTU1NjdhZDZiZGRhMDcwZjFiMDg2NDMyOGI0MGM1N2IyMTFmZDM3NzU1MTg0YmNhMDJkYTVlZWJmMTQ2OTNhNTgwY2NlMDQwMzBhOTk4NDgyYjZhNjhlNWU4N2Q4MDhhZTNhMmVlZDkyN2MxZTM2YmVlYjU0YzEwYmY0M2MyYzRlNWI1MDY5OWU5YTJiNzE2ZDBjOWU5NTJmNTlmMTU2NDU3NGUyODAxMjk2YWMw'}
url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'
response = requests.post(url,headers=header,json=data)
print(response.json())
# trans_word()
# trans_text_en('Unable to read a single word')
