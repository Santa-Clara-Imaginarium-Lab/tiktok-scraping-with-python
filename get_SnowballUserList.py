from TikTokApi import TikTokApi

tiktok_id = TikTokApi.get_user("tiktok")["userInfo"]["user"]["id"]
suggested = TikTokApi.get_suggested_hashtags_by_id_crawler(startingId=tiktok_id) 

print(suggested)

# getting this error hmmm

"""TypeError: get_user() missing 1 required positional argument: 'username'"""

print("Success!")