from TikTokApi import TikTokApi
import os
from os.path import join, dirname
from dotenv import load_dotenv    
import random
import string
 
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path) 

api = TikTokApi().get_instance(custom_verifyFp=os.environ.get("verifyFp"), use_text_endpoints=True, device_id="".join(random.choice(string.digits) for num in range(19)))

# Gets array of trending music objects
trendingMusic = api.discover_music()

for tiktok in trendingMusic:
    print(tiktok)

# Gets array of trending challenges (hashtags)
trendingChallenges = api.discover_hashtags()

for tiktok in trendingChallenges:
    print(tiktok)