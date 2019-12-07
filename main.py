from instabot import Bot
from dotenv import load_dotenv
import argparse
import re
import os


#первоисточник и более расширенное описано регулярных выражений здесь:
#https://blog.jstassen.com/2016/03/code-regex-for-instagram-username-and-hashtags/

def get_comments(comments):
  comments_from_competition = []
  for comment in comments:
    participants = re.findall(r'(?:@)([A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:\.(?!\.))){0,28}(?:[A-Za-z0-9_]))?)',comment['text'])
    comments_from_competition.append([comment['user_id'],participants])
  return comments_from_competition

def is_users_exist(user_name):
  return bot.get_user_id_from_username(user_name)  is not None


if __name__ == '__main__':
    load_dotenv()
    secret_user_name = os.getenv("INSTAGRAM_USER_NAME")
    secret_user_password = os.getenv("INSTAGRAM_PASSWORD")

    bot = Bot()
    bot.login(username=secret_user_name, password=secret_user_password)

    parser = argparse.ArgumentParser(
        description='Проверяет, кто выполнил условие конкурса в инстаграме'
    )
    parser.add_argument('user_id', help='Введите ссылку на пост розыграша')
    parser.add_argument('instagram_username', help='Введите названия страницы розыграша')
    args = parser.parse_args()
    main_instagram_followers = bot.get_user_followers(args.instagram_username)
    user_id = bot.get_media_id_from_link(args.user_id)
    user_comments = bot.get_media_comments(user_id)
    users = get_comments(user_comments)
    usernames_and_ids = [[bot.get_username_from_user_id(user),user] for user,comment in users]
    all_users_who_liked = bot.get_media_likers(user_id)
    username_of_participants = [id_user for user_name,id_user in usernames_and_ids if str(id_user)]
    check_followers = [bot.get_username_from_user_id(user) for user in set(username_of_participants)]
    print([username for username in check_followers if bot.get_username_from_user_id(username) in main_instagram_followers])
