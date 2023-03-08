import praw
import random
import openai
reddit = praw.Reddit(client_id ='your_client_id',
					client_secret ='your_client_secret',
					user_agent ='your_user_agent',
					username ='your_username',
					password ='your_password')

subreddit= reddit.subreddit("subreddit")
while True:
    hot_posts = subreddit.hot(limit=7)
    list_posts = list(hot_posts)
    the_post=random.choice(list_posts)
    comment_count=len(the_post.comments)
    print(comment_count)
    if comment_count>0:
        print(the_post.title)
        break
    else: continue

comment = the_post.comments[random.randint(0,comment_count-1)]

print(comment.body)
openai.api_key = "YOUR API KEY"

prompt = comment.body
response = openai.Completion.create(
        engine="text-davinci-003",
    prompt=prompt,
    max_tokens=50
    )
generated_text = response.choices[0].text
print("******")
print(generated_text)
comment.reply(generated_text)
