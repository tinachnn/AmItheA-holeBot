import praw

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit('AmItheAsshole')

def get_hottest_post():
    for submission in subreddit.hot():
        if not submission.stickied:
            if submission.num_comments > 0:
                judgement =  get_judgement(submission.comments[0].body)
            else:
                judgement = 'No comments found'
            sentence = f'JUDGEMENT : {judgement.upper()}'
            msg = submission.title + '\n\n' + submission.selftext + '\n\n\n' + sentence
            if len(msg) < 1440:
                return msg
    return 'No posts available.'

def get_judgement(text):
    text = text.lower()
    if 'yta' in text or 'ywbta' in text:
        return 'yta'
    elif 'nta' in text or 'ywnbta' in text:
        return 'nta'
    elif 'esh' in text:
        return 'esh'
    elif 'nah' in text:
        return 'nah'
    elif 'info' in text:
        return 'info'
    else:
        return 'not found'