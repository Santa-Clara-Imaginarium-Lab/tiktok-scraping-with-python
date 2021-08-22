from TikTokApi import TikTokApi
import pandas as pd

# collect videos liked by a given user (that is the official tiktok account) which defaults to 30 yet 100 is specified
 
username = "tiktok" 
liked_videos = TikTokApi().user_liked_by_username(username, count=100)

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

# Then, we can go from the API-outputted "liked_videos" list to a nice, clean table
 
liked_videos = [simple_dict(v) for v in liked_videos]
liked_videos_df = pd.DataFrame(liked_videos)
liked_videos_df.to_csv('{}_collected_liked_videos.csv'.format(username), index=False)

print("Success!")