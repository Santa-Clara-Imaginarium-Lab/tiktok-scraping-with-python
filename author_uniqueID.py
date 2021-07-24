# for getting author and their unique id
from TikTokApi import TikTokApi

verifyFp = "verify_kq02cje3_QxorNTrh_UCSw_47Yj_9fs8_VJ7XXKQ8adNb" 

api = TikTokApi.get_instance(custom_verifyFp=verifyFp, use_text_endpoints=True)

tiktoks = api.trending()

for tiktok in tiktoks:
    print(tiktok["author"]["uniqueId"]) 