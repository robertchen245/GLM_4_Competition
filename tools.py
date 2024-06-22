import requests
import json
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_company_info",
            "description": "根据提供的公司名称（全称）查询该公司的基本信息，可以得知所属行业（不包含控股信息）",
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
            "description": "根据提供的公司名称（全称）查询该公司的注册信息（不包含控股信息）",
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
            "description": "根据提供的一般信息字段和值(如所属的行业信息，行业类别、市场、上市时间等)查询公司的具体名称。建议在其他工具无法找到信息时使用，特别是当输入的是公司简称、英文名称时。",
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
            "name": "search_company_name_by_info_industry",
            "description": "根据行业的类型，查找属于该行业的企业",
            "parameters": {
                "type": "object",
                "properties": {
                    "key": {
                        "type": "string",
                        "description": "所属行业",
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
            "description": "子公司查找母公司：当提供的是子公司名称时，查询控股其的母公司名称",
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
            "description": "母公司查找子公司：当提供的是母公司名称时，查询其控股、投资的子公司名单",
            "parameters": {
                "type": "object",
                "properties": {
                    "key": {
                        "type": "string",
                        "description": "key必须为'关联上市公司全称'",
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
    {
        "type": "function",
        "function": {
            "name": "get_legal_document",
            "description": "可以根据“案号“例：(1234)某1234某某1234号，（请注意括号的格式应以提问为准）即案件的编号的查找一个法律文书、案件档案、判决的具体有关的详细内容。输入：案号，返回：该案的具体信息",
            "parameters": {
                "type": "object",
                "properties": {
                    "case_num": {
                        "type": "string",
                        "description": "正确格式：(1234)某1234某某1234号\n错误格式：（1234）某1234某某1234号",
                    },
                },
                "required": ["case_num"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "search_case_num_by_legal_document",
            "description": "法律文书搜索工具：根据法律文书、案件的具体内容某个字段是某个值来查询具体的案号。输入：非案号的键值，返回：案号",
            "parameters": {
                "type": "object",
                "properties": {
                    "key": {
                        "type": "string",
                        "description": "'标题', '文书类型', '原告', '被告', '原告律师', '被告律师', '案由', '审理法条依据', '涉案金额', '判决结果', '胜诉方', '文件名'",
                    },
                    "value": {
                        "type": "string",
                        "description": "字段对应的值",
                    },
                },
                "required": ["key","value"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "investment_information",
            "description": "给定了母公司，查询其子公司的控股、投资比例有关的信息",
            "parameters": {
                "type": "object",
                "properties": {
                    "key": {
                        "type": "string",
                        "description": "key:'关联上市公司全称'",
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
categories=f"""
你是一个帮助专精于将给定的“问题”进行“分类”的助手，请你对这个问题进行多分类，即可能包含1个或者多个类别
类别：1.母公司查找子公司，涉及投资信息 2.子公司查找母公司 3.根据公司的名称查找公司信息 4.法律文书判决相关 5. 给定了母公司，查询其子公司的控股、投资比例 6.开放性问题 7.先得知主体企业的行业类型，再根据行业的类型，查找属于该行业的所有企业\n
下面是3个问答的例子：
例1:你接收到的问题：想问问，浙江杰克成套智联科技有限公司、上海三菱电梯有限公司、潍坊西能宝泉天然气有限公司分别属于哪家公司旗下。分析：2.问题分类：子公司查找母公司。 主体：浙江杰克成套智联科技有限公司、上海三菱电梯有限公司、潍坊西能宝泉天然气有限公司
例2:你接收到的问题：劲拓股份拥有哪些子公司？分析：1.母公司查找子公司。主体：劲拓股份
例3:你接收到的问题：请问Beijing Comens New Materials Co., Ltd.全资控股的子公司有哪些？或 持股超过50%的子公司有哪些？分析：5.查询子公司的控股投资比例，主体：Beijing Comens New Materials Co., Ltd.
例4:你接收到的问题：广汇能源股份有限公司的主要投资者是哪一家企业？分析：5. 给定了母公司，查询其子公司的控股、投资比例。主体：广汇能源股份有限公司
例5:你接收到的问题：帮忙找下无锡上机数控股份有限公司的企业主承销商以及首次公开发行募集资金净额。分析：3.根据公司的名称查找公司信息。主体：无锡上机数控股份有限公司
例6:你接收到的问题：关于案号为(2019)鄂01民初4724号的案件，能否提供原告和被告的详细身份信息，并阐述该案件的具体诉讼理由？分析：4.法律文书判决相关。主体：(2019)鄂01民初4724号

请你严格按照例子的格式给出分类，不允许进行推测以及额外信息
"""
def get_company_info(args,origin_url,headers):
    url = origin_url+'get_company_info'
    rsp = requests.post(url, json=json.loads(args), headers=headers)
    return rsp.json()
def get_company_register(args,origin_url,headers):
    url = origin_url+'get_company_register'
    rsp = requests.post(url, json=json.loads(args), headers=headers)
    return rsp.json()
def get_company_info_and_register(args,origin_url,headers):
    """根据公司的名称：得到基本信息和注册信息"""
    rsp1 = get_company_info(args,origin_url,headers)
    rsp2 = get_company_register(args,origin_url,headers)
    rsp={**rsp1.json(),**rsp2.json()}
    return rsp.json()
def get_brief_name(args,origin_url,headers):
    pass
def search_company_name_by_info(args,origin_url,headers):
    url = origin_url+'search_company_name_by_info'
    rsp = requests.post(url, json=json.loads(args), headers=headers)
    return rsp.json()
def get_sub_company_info(args,origin_url,headers):
    url = origin_url+'get_sub_company_info'
    rsp = requests.post(url, json=json.loads(args), headers=headers)
    return rsp.json()
def search_company_name_by_register(args,origin_url,headers):
    url = origin_url+'search_company_name_by_register'
    rsp = requests.post(url, json=json.loads(args), headers=headers)
    return rsp.json()
def search_company_name_by_sub_info(args,origin_url,headers):
    url = origin_url+'search_company_name_by_sub_info'
    rsp = requests.post(url, json=json.loads(args), headers=headers)
    return rsp.json()
def get_legal_document(args,origin_url,headers):
    url = origin_url+'get_legal_document'
    rsp = requests.post(url, json=json.loads(args), headers=headers)
    return rsp.json()
def search_case_num_by_legal_document(args,origin_url,headers):
    url = origin_url+'search_case_num_by_legal_document'
    rsp = requests.post(url, json=json.loads(args), headers=headers)
    return rsp.json()
def investment_information(args,origin_url,headers):
    url = origin_url+'search_company_name_by_sub_info'
    rsp = requests.post(url, json=json.loads(args), headers=headers)
    rsp=rsp.json()
    sub_info_list=[]
    for sub_company in rsp:
        url=origin_url+'get_sub_company_info'
        sub={"company_name":sub_company["公司名称"]}
        rsp_sub = requests.post(url, json=sub, headers=headers)
        sub_info_list.append(rsp_sub.json())
    return sub_info_list
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
            "search_company_name_by_info_industry":search_company_name_by_info,
            "search_company_name_by_register":search_company_name_by_register,
            "get_sub_company_info":get_sub_company_info,
            "search_company_name_by_sub_info":search_company_name_by_sub_info,
            "get_legal_document":get_legal_document,
            "search_case_num_by_legal_document":search_case_num_by_legal_document,
            "investment_information":investment_information
        }
        return func_tools[func_name](func_args,origin_url,headers)
    else:
        return None