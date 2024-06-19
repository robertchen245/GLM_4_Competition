import requests
import json
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_company_info",
            "description": "根据提供的公司名称查询该公司的基本信息",
            "parameters": {
                "type": "object",
                "properties": {
                    "company_name": {
                        "type": "string",
                        "description": "公司名称",
                    }
                },
                "required": ["company_name"],
            },
        },
    },
        {
        "type": "function",
        "function": {
            "name": "get_company_register",
            "description": "根据提供的公司名称查询该公司的注册信息",
            "parameters": {
                "type": "object",
                "properties": {
                    "company_name": {
                        "type": "string",
                        "description": "公司名称",
                    }
                },
                "required": ["company_name"],
            },
        },
    },
        {
        "type": "function",
        "function": {
            "name": "get_company_info_and_register",
            "description": "根据提供的公司名称，如果需求的条目既包含基本信息，又包含注册信息，则使用这个",
            "parameters": {
                "type": "object",
                "properties": {
                    "company_name": {
                        "type": "string",
                        "description": "公司名称",
                    }
                },
                "required": ["company_name"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "search_company_name_by_info",
            "description": "根据提供的一般信息的某个字段的某个值查询具体公司的名称,可以选择这个工具查找可能为非公司全称的，公司简称、或者名称、曾用简称",
            "parameters": {
                "type": "object",
                "properties": {
                    "key": {
                        "type": "string",
                        "description": "'公司简称', '英文名称', '关联证券', '公司代码', '曾用简称', '所属市场', '所属行业', '上市日期', '法人代表', '总经理', '董秘', '邮政编码', '注册地址', '办公地址', '联系电话', '传真', '官方网站', '电子邮箱', '入选指数', '主营业务', '经营范围', '机构简介', '每股面值', '首发价格', '首发募资净额', '首发主承销商'",
                    },
                    "value": {
                        "type": "string",
                        "description": "值"
                    },
                },
                "required": ["key", "value"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "search_company_name_by_register",
            "description": "根据提供的'注册信息'的某个字段的某个值查询具体公司的名称",
            "parameters": {
                "type": "object",
                "properties": {
                    "key": {
                        "type": "string",
                        "description": "'公司名称', '登记状态', '统一社会信用代码', '注册资本', '成立日期', '省份', '城市', '区县', '注册号', '组织机构代码', '参保人数', '企业类型', '曾用名'",
                    },
                    "value": {
                        "type": "string",
                        "description": "值",
                    },
                },
                "required": ["key", "value"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_sub_company_info",
            "description": "根据子公司名称获得其母公司的所有关联子公司信息",
            "parameters": {
                "type": "object",
                "properties": {
                    "company_name": {
                        "type": "string",
                        "description": "公司名称",
                    },
                },
                "required": ["company_name"],
            },
        },
    },
]
def get_company_info(args,origin_url,headers):
    url = origin_url+'get_company_info'
    rsp = requests.post(url, json=json.loads(args), headers=headers)
    return rsp
def get_company_register(args,origin_url,headers):
    url = origin_url+'get_company_register'
    rsp = requests.post(url, json=json.loads(args), headers=headers)
    return rsp
def get_company_info_and_register(args,origin_url,headers):
    """根据公司的名称：得到基本信息和注册信息"""
    rsp1 = get_company_info(args,origin_url,headers)
    rsp2 = get_company_register(args,origin_url,headers)
    rsp={**rsp1.json(),**rsp2.json()}
    return rsp
def get_brief_name(args,origin_url,headers):
    pass
def search_company_name_by_info(args,origin_url,headers):
    url = origin_url+'search_company_name_by_info'
    rsp = requests.post(url, json=json.loads(args), headers=headers)
    return rsp
def get_sub_company_info(args,origin_url,headers):
    url = origin_url+'get_sub_company_info'
    rsp = requests.post(url, json=json.loads(args), headers=headers)
    return rsp
def search_company_name_by_register(args,origin_url,headers):
    url = origin_url+'search_company_name_by_register'
    rsp = requests.post(url, json=json.loads(args), headers=headers)
    return rsp
def use_the_tool(tool_calls:str,origin_url:str,headers:dict):
    if tool_calls is not None:
        function = tool_calls[0].function
        func_args = function.arguments
        func_name = function.name

        func_tools={
            "get_company_info":get_company_info,
            "get_company_register":get_company_register,
            "get_company_info_and_register":get_company_info,
            "search_company_name_by_info":search_company_name_by_info,
            "search_company_name_by_register":search_company_name_by_register,
            "get_sub_company_info":get_sub_company_info
        }
        return func_tools[func_name](func_args,origin_url,headers)
    else:
        return None