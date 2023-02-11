"""
Instagram-Bot, Telegram Instagram Bot

Copyright (C) 2021 Zaute Km

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.
You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import os
from instaloader import Instaloader
class Config:
    API_ID = int(os.environ.get("API_ID", "7715737"))
    API_HASH = os.environ.get("API_HASH", "241e23bd490bfad03f0da62d4f5d8a20")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5677905120:AAGPqHoPfbcId9PQB9QRfZ0hrs_SoO3d0PU") 
    USER = os.environ.get("INSTAGRAM_USERNAME", "l00bd")
    OWNER = os.environ.get("OWNER_ID", "5307018300")
    INSTA_SESSIONFILE_ID = os.environ.get("INSTA_SESSIONFILE_ID", "1684511059%3A87PSFNLOnPvRaA%3A22%3AAYd70FWG9WavQvJ9EmietyljzPbq5-Nc-1PmGOcpaQ")
    S = "0"
    STATUS = set(int(x) for x in (S).split())
    L=Instaloader()
    HELP="""
You can Download almost anything From your Instagram Account.

<b>What Can Be Downloaded?:</b>

1. All posts of any Profile. (Both Public and Private,for private profiles you need to be a follower.)
2. All Posts from your feed.
3. Stories of any profile (Both Public and Private,for private profiles you need to be a follower.)
4. DP of any profile (No need to follow)
5. Followers and Followees List of any Profile.
6. List of followees who follows back the given username.
7. List of followees who are not following back the given username.
8. Stories of your Followees.
9. Tagged posts of any profile.
10. Your saved Posts.
11. IGTV videos.
12. Highlights from any profiles.
13. Any Public Post from Link(Post/Reels/IGTV)


<b>How to Download:</b>

Its Easy!!
You Need to login into your account by /login. 

You have two Options:

1. From Username:

Just send any instagram username.

For Example:
<code>zautekm</code>

2. From URL:

You can also sent a post link to download the post or video.

For Example:
<code>https://www.instagram.com/p/CL4QbUiLRNW/?utm_medium=copy_link</code>


<b>Available Commands and Usage</b>

/start - Check wheather bot alive.
/restart - Restart the bot (If you messed up anything use /restart.)
/help - Shows this menu.
/login - Login into your account.
/logout - Logout of your account.
/account - Shows the details of logged in account.

/posts <username> - Download posts of any username. Use /posts to download own posts or <code> /posts <username> </code>for others.
Example : <code>/posts samantharuthprabhuoffl</code>

/igtv <username> - Download IGTV videos from given username. If no username given, downloads your IGTV.

/feed <number of posts to download> - Downloads posts from your feed.If no number specified all posts from feed will be downloaded.
Example: <code>/feed 10</code> to download latest 10 posts from feed.

/saved <number of posts to download> - Downloads your saved posts. If no number specified all saved posts will be downloaded.
Example: <code>/saved 10</code> to download latest 10 saved posts.

/followers <username> - Get a list of all followers of given username. If no username given, then your list will be retrieved.
Example: <code>/followers samantharuthprabhuoffl</code>

/followees <username> - Get a list of all followees of given username. If no username given, then your list will be retrieved.

/fans <username> - Get a list of of followees who follow back the given username. If no username given, your list will be retrieved.

/notfollowing <username> - Get a list of followees who is not following back the given username.

/tagged <username> - Downloads all posts in which given username is tagged. If nothing given your tagged posts will be downloaded.

/story <username> - Downloads all stories from given username. If nothing given your stories will be downloaded.

/stories - Downloads all the stories of all your followees.

/highlights <username> - Downloads highlights from given username, If nothing given your highlights will be downloaded.


"""
    HOME_TEXT = """
<b>Helo, [{}](tg://user?id={})

This is a bot of [{}](www.instagram.com/{}) to manage his Instagram account. 
I can only work for my master [{}](tg://user?id={}).
But you can Deploy the same bot for your use from the below source code.

Use /help to know What I can Do?</b>
"""
    HOME_TEXT_OWNER = """
<b>Helo, [{}](tg://user?id={})
I am your assistant to manage your Instagram account.

Use /help to know what I can do for you.</b>
"""

