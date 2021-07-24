# for getting videos 

from TikTokApi import TikTokApi
import string
import random

verifyFp = "verify_kq02cje3_QxorNTrh_UCSw_47Yj_9fs8_VJ7XXKQ8adNb"   
did = "".join(random.choice(string.digits) for num in range(19))

api = TikTokApi.get_instance(custmom_verifyFp=verifyFp, use_text_endpoints=True, custom_did=did)

tiktoks = api.trending()
 
video_bytes = api.get_Video_By_TikTok(tiktoks[0])

with open("test.mp4", "wb") as o:
    o.write(video_bytes)