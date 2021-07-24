# for getting videos from the first video post from TikTok's trending accounts

from TikTokApi import TikTokApi
import string
import random
import os
from os.path import join, dirname
from dotenv import load_dotenv
import uuid
 
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

verifyFp = os.environ.get("verifyFp")

did = "".join(random.choice(string.digits) for num in range(19))

api = TikTokApi.get_instance(custmom_verifyFp=verifyFp, use_text_endpoints=True, custom_did=did)

tiktoks = api.trending()
 
video_bytes = api.get_Video_By_TikTok(tiktoks[0])

filename = str(uuid.uuid4())
with open("./videos/" + filename + "_test.mp4", "wb") as o:
    o.write(video_bytes)

print("Success!")