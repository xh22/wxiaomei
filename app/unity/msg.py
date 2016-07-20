# -*- coding: utf-8 -*-
import urllib
import urllib2
def sendsms(phone, code):
    url = 'https://106.ihuyi.com/webservice/sms.php?method=Submit'
    values = {'account':'cf_wuxiaomei', 'password':'0527164832157b0604f4e435bf598203',
              'mobile':phone, 'content':"您的验证码是："+code+"。请不要把验证码泄露给其他人。"
             }
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    the_page = response.read()
    print the_page
