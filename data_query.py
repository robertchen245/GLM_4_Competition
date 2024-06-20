import requests
from tokens import tokens
domain = "comm.chatglm.cn"
url = f"https://{domain}/law_api/"
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {tokens["data_token"]}'
}
data={}
#data["company_name"] = "广东天昊药业有限公司"
if __name__ == "__main__":
    url=url+'search_company_name_by_info'
    data={"key":"","value":"青海华鼎实业股份有限公司"}
    rsp = requests.post(url, json=data, headers=headers)
    print(rsp.json())