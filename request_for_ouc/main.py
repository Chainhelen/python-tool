import requests

geturl = "http://www.ouc.edu.cn/_control/validateimage?tt=Wed%20Apr%2029%2019:48:07%20CST%202015"
r1 = requests.get(geturl)
validateCode  = r1.cookies["validateImageValue"]
cookies = r1.cookies



posturl = "http://www.ouc.edu.cn/login.jsp?_p=YXM9MSZwPTEmbT1OJg__"
payload = {
    "userName" : "22222",
    "password" : "33333",
    "isSubmitted" : '1',
    "validateCode": validateCode
}

r2 = requests.post(posturl, data = payload, cookies = cookies)
print r2.text
