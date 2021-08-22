from TikTokApi import TikTokApi 
import os
from os.path import join, dirname
from dotenv import load_dotenv   
import pandas as pd
 
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path) 

api = TikTokApi().get_instance(use_text_endpoints=True, custom_verifyFp=os.environ.get("verifyFp"))

# get any amount (default is 30) yet 100 is specified of videos under the hashtag #funny
 
hash_tag_name = "funny"

hash_tags = api.by_hashtag(hash_tag_name, count=100)

def simple_dict(tiktok_dict):
    to_return = {}
    to_return["author_id"] = tiktok_dict["author"]["id"]
    to_return["author_uniqueId"] = tiktok_dict["author"]["uniqueId"]
    to_return["author_nickname"] = tiktok_dict["author"]["nickname"]
    to_return["author_avatarThumb"] = tiktok_dict["author"]["avatarThumb"]
    to_return["author_signature"] = tiktok_dict["author"]["signature"] 
    to_return["author_verification"] = tiktok_dict["author"]["verified"]
    to_return["author_privateAccount"] = tiktok_dict["author"]["privateAccount"]
    to_return["author_followingCount"] = tiktok_dict["authorStats"]["followingCount"]
    to_return["author_followerCount"] = tiktok_dict["authorStats"]["followerCount"]
    to_return["author_heartCount"] = tiktok_dict["authorStats"]["heartCount"]
    to_return["author_videoCount"] = tiktok_dict["authorStats"]["videoCount"]
    to_return["author_diggCount"] = tiktok_dict["authorStats"]["diggCount"]
    to_return["author_heart"] = tiktok_dict["authorStats"]["heart"]
    to_return["video_id"] = tiktok_dict["id"]
    to_return["video_desc"] = tiktok_dict["desc"]
    to_return["video_duration"] = tiktok_dict["video"]["duration"]
    to_return["video_cover"] = tiktok_dict["video"]["cover"]
    to_return["video_link"] = "https://www.tiktok.com/@{}/video/{}?lang=en".format(to_return["author_uniqueId"], to_return["video_id"])
    to_return["video_format"] = tiktok_dict["video"]["format"]
    to_return["video_quality"] = tiktok_dict["video"]["videoQuality"]
    to_return["video_definition"] = tiktok_dict["video"]["definition"]
    to_return["video_stats"] = tiktok_dict["stats"]["diggCount"]
    to_return["video_shareCount"] = tiktok_dict["stats"]["shareCount"]
    to_return["video_commentCount"] = tiktok_dict["stats"]["commentCount"]
    to_return["video_playCount"] = tiktok_dict["stats"]["playCount"]
    to_return["video_originalItem"] = tiktok_dict["originalItem"]
    to_return["video_officialItem"] = tiktok_dict["officalItem"]
    to_return["video_secret"] = tiktok_dict["secret"]
    to_return["video_forFriend"] = tiktok_dict["forFriend"]
    to_return["video_stitchEnabled"] = tiktok_dict["stitchEnabled"]
    to_return["video_shareEnabled"] = tiktok_dict["shareEnabled"]
    to_return["video_isAd"] = tiktok_dict["isAd"]
    to_return["music_id"] = tiktok_dict["music"]["id"]
    to_return["music_title"] = tiktok_dict["music"]["title"]
    to_return["music_playUrl"] = tiktok_dict["music"]["playUrl"]
    to_return["music_coverThumb"] = tiktok_dict["music"]["coverThumb"]
    to_return["music_authorName"] = tiktok_dict["music"]["authorName"]
    to_return["music_originality"] = tiktok_dict["music"]["original"]
    to_return["music_duration"] = tiktok_dict["music"]["duration"]

    return to_return 

hash_tags = [simple_dict(v) for v in hash_tags]
hash_tags_df = pd.DataFrame(hash_tags)
hash_tags_df.to_csv('tiktok_{}_hashtag_videos.csv'.format(hash_tag_name), index=False)

# hmm keep getting this error

"""TikTokApi.exceptions.TikTokCaptchaError: TikTok blocks this request displaying a Captcha
Tip: Consider using a proxy or a custom_verifyFp as method parameters"""

print("Success!")