from zhipuai import ZhipuAI
from tokens import tokens
import requests
from data_query import url as origin_url, headers
import json
from tools import tools,use_the_tool
client = ZhipuAI(api_key=tokens["glm_token"])
q='上市公司因涉嫌金融诈骗面临的法律风险有哪些？'
messages = [
    {
        "role":"system",
        "content": "你是一个通过调用企业信息相关的api给用户提供信息的助手，对于一些非查询的开放性问题，你也可以根据你的知识自己回答"
    },
    { 
        "role": "user",
        "content": f"{q}"+"请你先将问题先进行拆分，便于你自己的理解，思考一下完成任务的顺序，你一定能通过公司的名称获得信息，若信息搜不到，请尝试用工具将其转换为“全称”"
    }
]
response = client.chat.completions.create(
    model="glm-4", # 填写需要调用的模型名称
    messages=messages,
    )
print(response.choices[0].message)
messages.append(response.choices[0].message.model_dump())
messages.append({ 
        "role": "user",
        "content": f"{q}"+"参考你分解的顺序的思路，完成下面的任务"
    })
for i in range(20):
    response = client.chat.completions.create(
    model="glm-4", # 填写需要调用的模型名称
    messages=messages,
    tools=tools,
    )
    print(response.choices[0].message)
    if 'Complete' in response.choices[0].message.content:
        break
    messages.append(response.choices[0].message.model_dump())# 后文补全
    while(True):
        rsp = use_the_tool(tool_calls=response.choices[0].message.tool_calls,origin_url=origin_url,headers=headers)
        if rsp is None:
            print("找不到tools")
            break
        print("------------------------------------------")
        print(rsp.json())
        print("------------------------------------------")
        messages.append({
                    "role": "tool",
                    "content": f"{rsp.json()}",
                    "tool_call_id": response.choices[0].message.tool_calls[0].id
                })
        response = client.chat.completions.create(
                model="glm-4",  # 填写需要调用的模型名称
                messages=messages,
                tools=tools
            )
        print(response.choices[0].message)
        messages.append(response.choices[0].message.model_dump())
    messages.append({
    "role": "user",
    "content": "如果你认为你的回答令人满意，那就回复一个'Complete',如果没有任何信息，很有可能是你错误调用了工具。如果不够令人满意，请根据原始的提问，以及你得到的信息，以及你的回答，试想如何使用工具完成任务"
    })