import requests
import json
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_company_info",
            "description": "根据提供的公司名称（只能接受明显是公司的具体全称）查询该公司的基本信息（不包含控股信息）",
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
            "description": "根据提供的公司名称（只能接受明显是公司的具体全称）查询该公司的注册信息（不包含控股信息）",
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
            "description": "根据提供的公司名称查询该公司的基本信息和注册信息（不包含控股信息）",
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
            "description": "根据提供的一般信息字段所属行业和值(如所属行业等)查询公司的具体名称。建议在其他工具无法找到信息时使用，特别是当输入的是公司简称时。",
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
            "description": "根据提供的注册信息字段和值查询公司的具体名称。",
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
            "description": "当提供的是子公司名称时，获取母公司的信息以及母公司对该子公司的投资信息。如果获得了大量子公司信息，应该依次使用这个工具来获取他们和母公司之间的投资信息。",
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
    {
        "type": "function",
        "function": {
            "name": "search_company_name_by_sub_info",
            "description": "当提供的是母公司名称时，查询其控股的子公司名称。本工具只能搜索到子公司名称，具体投资信息请使用其他工具。",
            "parameters": {
                "type": "object",
                "properties": {
                    "key": {
                        "type": "string",
                        "description": "key固定为'关联上市公司全称',并非实际名称",
                    },
                    "value": {
                        "type": "string",
                        "description": "公司的实际全称",
                    },
                },
                "required": ["key","value"],
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
def search_company_name_by_sub_info(args,origin_url,headers):
    url = origin_url+'search_company_name_by_sub_info'
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
            "get_sub_company_info":get_sub_company_info,
            "search_company_name_by_sub_info":search_company_name_by_sub_info,
        }
        return func_tools[func_name](func_args,origin_url,headers)
    else:
        return None