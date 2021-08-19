from TikTokApi import TikTokApi
import os
from os.path import join, dirname
from dotenv import load_dotenv    

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path) 

api = TikTokApi().get_instance(use_text_endpoints=True, custom_verifyFp=os.environ.get("verifyFp")) 

tiktok_id = api.get_user("tiktok")["userInfo"]["user"]["id"]
suggested = api.get_suggested_hashtags_by_id_crawler(startingId=tiktok_id) 

print(suggested)

# hmm keep getting this error

"""TikTokApi.exceptions.TikTokCaptchaError: TikTok blocks this request displaying a Captcha
Tip: Consider using a proxy or a custom_verifyFp as method parameters"""

print("Success!")