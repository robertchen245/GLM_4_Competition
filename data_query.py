import requests
from tokens import tokens
domain = "comm.chatglm.cn"
url = f"https://{domain}/law_api/"
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {tokens["data_token"]}'
}
data={}
data["company_name"] = "广州发展集团股份有限公司"
if __name__ == "__main__":
    url=url+'search_company_name_by_info'
    data={"key":"注册地址","value":"广东省广州市天河区临江大道3号发展中心30-32楼"}
    rsp = requests.post(url, json=data, headers=headers)
    print(rsp.json())