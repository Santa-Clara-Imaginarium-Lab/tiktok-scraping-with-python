# for getting videos from TikTok's overall trending accounts (default is 30) yet 100 is specified

from TikTokApi import TikTokApi 
import pandas as pd 

trending_videos = TikTokApi().by_trending(count=100)
  
def simple_dict(tiktok_dict):
  to_return = {}
  to_return["user_name"] = tiktok_dict["author"]["uniqueId"]
  to_return["user_id"] = tiktok_dict["author"]["id"]
  to_return["video_id"] = tiktok_dict["id"]
  to_return["video_desc"] = tiktok_dict["desc"]
  to_return["video_time"] = tiktok_dict["createTime"]
  to_return["video_length"] = tiktok_dict["video"]["duration"]
  to_return["video_link"] = "https://www.tiktok.com/@{}/video/{}?lang=en".format(to_return["user_name"], to_return["video_id"])
  to_return["n_likes"] = tiktok_dict["stats"]["diggCount"]
  to_return["n_shares"] = tiktok_dict["stats"]["shareCount"]
  to_return["n_comments"] = tiktok_dict["stats"]["commentCount"]
  to_return["n_plays"] = tiktok_dict["stats"]["playCount"]

  return to_return

trending_videos = [simple_dict(v) for v in trending_videos]
trending_videos_df = pd.DataFrame(trending_videos)
trending_videos_df.to_csv("trending_videos.csv", index=False)

print("Success!")