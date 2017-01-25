import praw, time, smtplib

def bot_main():
        reddit = praw.Reddit('craiova_crawler')
        done = []

        for submission in reddit.subreddit('world_news+romania').new(limit=25): # Grab 25 new posts from /r/romania and /r/world_news
                if 'craiova' in submission.title.lower() and submission.id not in done: # This will need to be refined but should be good for now
                        done.append(submission.id)
                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.starttls()
                        server.login('email', 'pass')
                        msg = 'https://redd.it/%s has mentioned Craiova!' % submission.id
                        server.sendmail('my@email.com', 'my@email.com', msg)
                        server.quit()

        time.sleep(10)
        bot_main()

bot_main()

