import requests,json
from AuthV3Util import addAuthParams

# 您的应用ID
APP_KEY = ''
# 您的应用密钥
APP_SECRET = ''

class Youdao_Translation:

    def __init__(self):
        pass
    
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

    #OUTPUT_NODE = False

    CATEGORY = "Youdao"

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

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "Youdao_Translation": Youdao_Translation
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "Youdao_Translation": "中文-有道翻译"
}
