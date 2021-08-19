from TikTokApi import TikTokApi 
import os
from os.path import join, dirname
from dotenv import load_dotenv   
import pandas as pd
 
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path) 

api = TikTokApi().get_instance(use_text_endpoints=True, custom_verifyFp=os.environ.get("verifyFp"))

# get any amount of videos under the hashtag #funny
 
hash_tag_name = "funny"

hash_tags = api.by_hashtag(hash_tag_name)

def simple_dict(tiktok_dict):
    to_return = {}
    to_return["video_desc"] = tiktok_dict["desc"]
    to_return["video_duration"] = tiktok_dict["video"]["duration"]
    to_return["video_cover"] = tiktok_dict["video"]["cover"]
    to_return["video_format"] = tiktok_dict["video"]["format"]
    to_return["video_quality"] = tiktok_dict["video"]["videoQuality"]
    to_return["video_definition"] = tiktok_dict["video"]["definition"]
    to_return["author_uniqueId"] = tiktok_dict["author"]["uniqueId"]
    to_return["author_nickname"] = tiktok_dict["author"]["nickname"]
    to_return["author_avatarThumb"] = tiktok_dict["author"]["avatarThumb"]
    to_return["author_signature"] = tiktok_dict["author"]["signature"] 
    to_return["author_verification"] = tiktok_dict["author"]["verified"]
    to_return["author_privateAccount"] = tiktok_dict["author"]["privateAccount"]
    to_return["music_title"] = tiktok_dict["music"]["title"]
    to_return["music_playUrl"] = tiktok_dict["music"]["playUrl"]
    to_return["music_coverThumb"] = tiktok_dict["music"]["coverThumb"]
    to_return["music_authorName"] = tiktok_dict["music"]["authorName"]
    to_return["music_originality"] = tiktok_dict["music"]["originality"]
    to_return["music_duration"] = tiktok_dict["music"]["duration"]

    return to_return 

hash_tags = [simple_dict(v) for v in hash_tags]
hash_tags_df = pd.DataFrame(hash_tags)
hash_tags_df.to_csv('tiktok_{}_hashtag_videos.csv'.format(hash_tag_name), index=False)

# hmm keep getting this error

"""TikTokApi.exceptions.TikTokCaptchaError: TikTok blocks this request displaying a Captcha
Tip: Consider using a proxy or a custom_verifyFp as method parameters"""

print("Success!")