from TikTokApi import TikTokApi 
import os
from os.path import join, dirname
from dotenv import load_dotenv   
import pandas as pd
 
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path) 

api = TikTokApi.get_instance(use_text_endpoints=True, custom_verifyFp=os.environ.get("verifyFp"))
 
hash_tag_name = "funny"

hash_tags = api.by_hashtag(hash_tag_name)

def simple_dict(tiktok_dict):
    to_return = {}
    to_return["video_desc"] = tiktok_dict["desc"]
    to_return["video_duration"] = tiktok_dict["video"]["duration"]
    to_return["video_cover"] = tiktok_dict["video"]["cover"]
    to_return["video_format"] = tiktok_dict["video"]["format"]
    to_return["video_quality"] = tiktok_dict["video"]["quality"]
    to_return["video_definition"] = tiktok_dict["video"]["definition"]

    return to_return 

hash_tags = [simple_dict(v) for v in hash_tags]
hash_tags_df = pd.DataFrame(hash_tags)
hash_tags_df.to_csv('{}_collected_hashtag_videos.csv'.format(hash_tag_name), index=False)

# hmm keep getting this error

"""TikTokApi.exceptions.TikTokCaptchaError: TikTok blocks this request displaying a Captcha
Tip: Consider using a proxy or a custom_verifyFp as method parameters"""

print("Success!")