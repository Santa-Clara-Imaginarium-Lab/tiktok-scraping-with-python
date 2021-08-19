from TikTokApi import TikTokApi 
import os
from os.path import join, dirname
from dotenv import load_dotenv 
import logging
 
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path) 

api = TikTokApi.get_instance(logging_level=logging.INFO)

getHashtag = api.byHashtag("tiktok", custom_verifyFp=os.environ.get("verifyFp"), use_text_endpoints=True)

print("Success!")

print(getHashtag)