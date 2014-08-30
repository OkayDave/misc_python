#!/usr/bin/env python

from ReddiWrap import ReddiWrap

reddit = ReddiWrap(user_agent='ReddiWrap')

USERNAME = ''
PASSWORD = ''

reddit.load_cookies("cookies.txt")

if not reddit.logged_in or reddit.user.lower() != USERNAME.lower():
  login = reddit.login(user=USERNAME, password=PASSWORD)
  if login != 0:

    print('unable to log in: %d' % login)
    exit(1)

  reddit.save_cookies('cookies.txt')

info = reddit.user_info()

if info.has_mail: 
	output = "ORANGERED!!!"
else:
  output = "L:%(link)d C:%(comment)d" % {"link": info.link_karma, "comment": info.comment_karma}

print(output)
