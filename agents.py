from zhipuai import ZhipuAI
from tokens_ import tokens
import json
sub_info="""
你是一个专精于帮助总结子公司信息、帮助计算的助手。请你根据提供给你的子公司名单，以及问题，对关键字，进行总结
要求一：格式要求仅保留'上市公司关系'、'上市公司参股比例'、'上市公司投资金额'、 '公司名称'，以列表返回。
要求二：根据问题决定是否按某些数值排序，如投资金额、参股比例。
要求三：如果提问主要投资者，那么只需要返回投资金额最大的一家公司即可！
要求四：除非满足要求三，你应该完整的返回所有公司信息
你的返回格式：[\{\},\{\}]
"""
categories=f"""
你是一个帮助专精于将给定的“问题”进行“分类”的助手，请你对这个问题进行多分类，即可能包含1个或者多个类别
类别：1.母公司查找子公司，涉及投资信息 2.子公司查找母公司 3.根据公司的名称查找公司信息 4.法律文书判决相关 5. 给定了母公司，查询其子公司的控股、投资比例 6.开放性问题 7.先得知主体企业的行业类型，再根据行业的类型，查找属于该行业的所有企业\n
下面是3个问答的例子：
例1:你接收到的问题：想问问，浙江杰克成套智联科技有限公司、上海三菱电梯有限公司、潍坊西能宝泉天然气有限公司分别属于哪家公司旗下。分析：2.问题分类：子公司查找母公司。 主体：浙江杰克成套智联科技有限公司、上海三菱电梯有限公司、潍坊西能宝泉天然气有限公司
例2:你接收到的问题：劲拓股份拥有哪些子公司？分析：1.母公司查找子公司。主体：劲拓股份
例3:你接收到的问题：请问Beijing Comens New Materials Co., Ltd.全资控股的子公司有哪些？或 持股超过50%的子公司有哪些？分析：5.查询子公司的控股投资比例，主体：Beijing Comens New Materials Co., Ltd.
例4:你接收到的问题：广汇能源股份有限公司的主要投资者是哪一家企业？分析：5. 给定了母公司，查询其子公司的控股、投资比例。主体：广汇能源股份有限公司
例5:你接收到的问题：帮忙找下无锡上机数控股份有限公司的企业主承销商以及首次公开发行募集资金净额。分析：3.根据公司的名称查找公司信息。主体：无锡上机数控股份有限公司
例6:你接收到的问题：关于案号为(2019)鄂01民初4724号的案件，能否提供原告和被告的详细身份信息，并阐述该案件的具体诉讼理由？分析：4.法律文书判决相关。主体:(2019)鄂01民初4724号

请你严格按照例子的格式给出分类，不允许进行推测以及额外信息
"""

def agent_question(question, model_type="glm-4-air"):
    agent_question = ZhipuAI(api_key=tokens["glm_token"])
    messages_q = [
        {"role": "system", "content": categories},
        {"role": "user", "content": f"你接收到的问题：{question}"},
    ]
    response = agent_question.chat.completions.create(
        model=model_type,
        messages=messages_q,
    )
    return response.choices[0].message.content


def agent_sub_info(question, sub_list, model_type="glm-4-air"):
    agent_sub_info = ZhipuAI(api_key=tokens["glm_token"])
    messages_sub = [
        {"role": "system", "content": sub_info},
        {"role": "user", "content": f"你接收到的问题：{question},子公司列表{json.dumps(sub_list, ensure_ascii=False)}"},
    ]
    response = agent_sub_info.chat.completions.create(
        model=model_type,
        messages=messages_sub,
    )
    return response.choices[0].message.content
