# for getting videos from the first video post from TikTok's trending accounts

from TikTokApi import TikTokApi
import string
import random
import os
from os.path import join, dirname
from dotenv import load_dotenv
import uuid
  
load_dotenv(join(dirname(__file__), ".env")
 
api = TikTokApi.get_instance(custmom_verifyFp=os.environ.get("verifyFp"), use_text_endpoints=True, custom_did="".join(random.choice(string.digits) for num in range(19))) 
 
video_bytes = api.get_Video_By_TikTok(api.trending()[0])

filename = str(uuid.uuid4())
with open("./videos/" + filename + "_test.mp4", "wb") as o:
    o.write(video_bytes)

print("Success!")