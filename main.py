from zhipuai import ZhipuAI
from tokens import tokens
import requests
from data_query import url as origin_url, headers
import json
from tools import tools,use_the_tool
client = ZhipuAI(api_key=tokens["glm_token"])
messages = [
    {
        "role": "user",
        "content": "请帮我了解浙江百达精工股份有限公司所属的行业领域"
    }
]
while(True):
    response = client.chat.completions.create(
        model="glm-4", # 填写需要调用的模型名称
        messages=messages,
        tools=tools,
    )
    print(response.choices[0].message)
    messages.append(response.choices[0].message.model_dump())# 后文补全
    rsp = use_the_tool(tool_calls=response.choices[0].message.tool_calls,origin_url=origin_url,headers=headers)
    messages.append({
                "role": "tool",
                "content": f"{rsp.json()}",
                "tool_call_id": response.choices[0].message.tool_calls[0].id
            })
    response = client.chat.completions.create(
            model="glm-4",  # 填写需要调用的模型名称
            messages=messages,
            tools=tools,
        ).choices[0].message
    print(response)
    messages.append(response.choices[0].message.model_dump())