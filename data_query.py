import requests
from tokens_ import tokens
domain = "comm.chatglm.cn"
url = f"https://{domain}/law_api/"
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {tokens["data_token"]}'
}
data={}
#data["company_name"] = "广东天昊药业有限公司"
if __name__ == "__main__":
    urll=url+'search_case_num_by_legal_document'
    data={"key":"案由","value":"不正当竞争纠纷"}
    rsp = requests.post(urll, json=data, headers=headers)
    rsp=rsp.json()
    print(rsp)
    '''for sub_company in rsp:
        urll=url+'get_sub_company_info'
        sub={"company_name":sub_company["公司名称"]}
        rsp_sub = requests.post(urll, json=sub, headers=headers)
        print(rsp_sub.json())'''