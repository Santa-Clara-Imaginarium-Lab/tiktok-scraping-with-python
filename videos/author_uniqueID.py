# for getting trending author metadata
from TikTokApi import TikTokApi
import os
from os.path import join, dirname
from dotenv import load_dotenv
import pandas as pd
 
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

verifyFp = os.environ.get("verifyFp")

api = TikTokApi.get_instance(custom_verifyFp=verifyFp, use_text_endpoints=True)

tiktoks = api.trending()

trending_rank = []
trending_nicknames = []
trending_avatars = []
trending_signature = []
trending_verified = []

for tiktok in tiktoks:
    trending_rank.append(tiktok["author"]["uniqueId"])
    trending_nicknames.append(tiktok["author"]["nickname"])
    trending_avatars.append(tiktok["author"]["avatarThumb"])
    trending_signature.append(tiktok["author"]["signature"])
    trending_verified.append(tiktok["author"]["verified"])

df = pd.DataFrame({"Author Unique ID": trending_rank, "Author Nickname": trending_nicknames, "Avatar Thumbnail": trending_avatars, "Signature": trending_signature, "Verified?": trending_verified})   
df.to_csv("tiktok_test.csv")

print("Success!")