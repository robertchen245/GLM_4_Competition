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
        "content": "请问德艺文化创意集团股份有限公司成立的准确日期，同时能否告知其注册办公地点及联系方式。"
    }
]
for i in range(10):
    response = client.chat.completions.create(
        model="glm-4", # 填写需要调用的模型名称
        messages=messages,
        tools=tools,
    )
    print(response.choices[0].message)
    if 'Complete' in response.choices[0].message.content:
        break
    messages.append(response.choices[0].message.model_dump())# 后文补全
    rsp = use_the_tool(tool_calls=response.choices[0].message.tool_calls,origin_url=origin_url,headers=headers)
    if rsp is None:
        print("找不到tools")
        break
    print(rsp.json())
    messages.append({
                "role": "tool",
                "content": f"{rsp.json()}",
                "tool_call_id": response.choices[0].message.tool_calls[0].id
            })
    response = client.chat.completions.create(
            model="glm-4",  # 填写需要调用的模型名称
            messages=messages,
            tools=tools,
        )
    print(response.choices[0].message)
    messages.append(response.choices[0].message.model_dump())
    messages.append({
        "role": "user",
        "content": "如果你认为你的回答足够令人满意，那就回复一个'Complete',如果不够令人满意，请根据原始的提问，以及你得到的信息，以及你的回答，试想如何使用工具完成任务"
    })