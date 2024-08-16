import requests,json
from AuthV3Util import addAuthParams

# 您的应用ID
APP_KEY = ''
# 您的应用密钥
APP_SECRET = ''

class Youdao_Translation:

    def __init__(self):
        pass

    CATEGORY = "Youdao"

    @classmethod
    def INPUT_TYPES(s):

        return {
            "required": {
                "text": ("STRING", {"multiline": True})
            },
        }

    RETURN_TYPES = ("STRING",)
    #RETURN_NAMES = ("image_output_name",)

    FUNCTION = "Translation"


    def Translation(self, text):
        q = text
        lang_from = 'auto'
        lang_to = 'e n'
        data = {'q': q, 'from': lang_from, 'to': lang_to}

        addAuthParams(APP_KEY, APP_SECRET, data)

        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        res = requests.post('https://openapi.youdao.com/api', data, header)
        content_str = res.content.decode('utf-8')
        result = json.loads(content_str)
        text = result['translation'][0]
        return (text)

    OUTPUT_NODE = True  # 表明它是一个输出节点
    # 输出的数据类型，需要大写
    RETURN_TYPES = ("STRING",)
    # 自定义输出名称
    RETURN_NAMES = ("文本",)

    FUNCTION = "Translation"


    def Translation(self, text):
        q = text
        lang_from = 'auto'
        lang_to = 'e n'
        data = {'q': q, 'from': lang_from, 'to': lang_to}

        addAuthParams(APP_KEY, APP_SECRET, data)

        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        res = requests.post('https://openapi.youdao.com/api', data, header)
        content_str = res.content.decode('utf-8')
        result = json.loads(content_str)
        text = result['translation'][0]
        return (text)
    