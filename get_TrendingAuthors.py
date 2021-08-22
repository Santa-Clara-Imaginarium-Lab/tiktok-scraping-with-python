# for getting trending authors (default is 30) yet 100 is specified

from TikTokApi import TikTokApi
import os
from os.path import join, dirname
from dotenv import load_dotenv
import pandas as pd
import random
import string
 
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path) 

api = TikTokApi().get_instance(custom_verifyFp=os.environ.get("verifyFp"), use_text_endpoints=True, device_id="".join(random.choice(string.digits) for num in range(19)))

tiktoks = api.by_trending(count=100)

trending_rank = []
trending_nicknames = []
trending_avatars = []
trending_signature = []
trending_verified = [] 
trending_privateAccount = []

for tiktok in tiktoks: 
    trending_rank.append(tiktok["author"]["uniqueId"])
    trending_nicknames.append(tiktok["author"]["nickname"])
    trending_avatars.append(tiktok["author"]["avatarThumb"])
    trending_signature.append(tiktok["author"]["signature"])
    trending_verified.append(tiktok["author"]["verified"])
    trending_privateAccount.append(tiktok["author"]["privateAccount"])

    """ other data points in tiktok dictionary (via trending method) are: id, avatarMedium, avatarLarger, secUid, secret, 
    ftc, relation, opoenFavorite, commentSetting, duetSetting, and stitchSetting but just have these ones for now"""

df = pd.DataFrame({"Author Unique ID": trending_rank, "Author Nickname": trending_nicknames, "Avatar Thumbnail": trending_avatars, "Signature": trending_signature, "Verified?": trending_verified, "Private Account?": trending_privateAccount})   
df.to_csv("trending_authors.csv")

print("Success!")