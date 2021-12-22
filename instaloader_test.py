import instaloader

USERNAME = "johnthuc03101997"
PASSWORD = 'John@Thuc@0310'

L = instaloader.Instaloader()
L.login(USERNAME, PASSWORD)

profile = instaloader.Profile.from_username(L.context, USERNAME)

for saved_post in profile.get_saved_posts():
    L.download_post(saved_post, saved_post.shortcode)
