import requests,json
from .AuthV3Util import addAuthParams

# 您的应用ID
APP_KEY = '应用ID'
# 您的应用密钥
APP_SECRET = '密钥'

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

    OUTPUT_NODE = True
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("文本",)

    FUNCTION = "Translation"

    def Translation(self, text):
        q = text
        lang_from = 'zh-CHS'
        lang_to = 'en'
        data = {'q': q, 'from': lang_from, 'to': lang_to}

        addAuthParams(APP_KEY, APP_SECRET, data)

        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        res = requests.post('https://openapi.youdao.com/api', data, header)
        content_str = res.content.decode('utf-8')
        result = json.loads(content_str)
        if 'translation' in result:
            text_01 = result['translation'][0]
            print(result)
            return (text_01)
        else:
            print(result)
    