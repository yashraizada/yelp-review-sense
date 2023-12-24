import requests

github_base = "https://raw.githubusercontent.com/yashraizada/yelp-review-sense/main/images/"
business_logo_dir = "business%20logo/"
business_stars_dir = "stars/"
user_avatars_dir = "avatars/"
image_format = ".png"

def is_image(image_url: str) -> bool:
    image_formats = ["image/png", "image/jpg", "image/jpeg"]
    
    if requests.head(image_url).headers["content-type"] in image_formats:
        return True
    return False

def get_business_logo_url(business_name: str) -> str:
    business_logo_url = github_base + business_logo_dir + business_name + image_format
    yelp_logo_url = github_base + business_logo_dir + "yelp" + image_format
    
    if is_image(business_logo_url):
        return business_logo_url
    return yelp_logo_url

def get_business_stars_url(business_stars: str) -> str:
    return github_base + business_stars_dir + str(business_stars) + image_format

def get_user_avatar_url(user_id: str) -> str:
    return github_base + user_avatars_dir + "default" + image_format