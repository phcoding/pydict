#!/usr/bin/python3

from urllib import request, parse
import json
import sys

def show_help():
    print('help...')

def main():
    if len(sys.argv) < 2:
        show_help()
        return
    words = sys.argv[1]
    post_data = parse.urlencode({
        "from":"zh",
        "to":"en",
        "query":words,
        # "query":"键盘",
        "transtype":"translang",
        "simple_means_flag":"3"
        })
    requ = request.Request('http://fanyi.baidu.com/v2transapi')
    requ.add_header('Host', 'fanyi.baidu.com')
    requ.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0')
    requ.add_header('Accept', '*/*')
    requ.add_header('Accept-Language', 'en-US,en;q=0.5')
    requ.add_header('Accept-Encoding', 'en-US,en;q=0.5')
    requ.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
    requ.add_header('X-Requested-With', 'XMLHttpRequest')
    requ.add_header('Referer', r'http://fanyi.baidu.com/translate?aldtype=16047&query=%E5%B8%AE%E5%8A%A9&keyfrom=baidu&smartresult=dict&lang=auto2zh')
    requ.add_header('Content-Length', '78')
    requ.add_header('Cookie', r'BAIDUID=F49EF7F92D1F9D27EBC7CFB34A5EB604:FG=1; BIDUPSID=EB895CEBA4E3BAD19DC355A2ED379DED; PSTM=1481521457; H_PS_PSSID=21764_1456_21085_17001_21554_20928; PSINO=1; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1481991435,1481991979; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1481991979; MANUBANNER=1; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; sideAdClose=17152')
    requ.add_header('Connection', 'keep-alive')
    resp = request.urlopen(requ, post_data.encode('utf-8'))
    print(json.loads(resp.read().decode('utf-8')).get('liju_result').get('tag'))

if __name__ == "__main__":
    main()
