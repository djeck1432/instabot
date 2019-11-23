from instabot import Bot
from dotenv import load_dotenv
import argparse
import re
import os



def get_comments(comments):
  comments_from_competition = []
  for comment in comments:
    participants = re.findall('(?:@)([A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:\.(?!\.))){0,28}(?:[A-Za-z0-9_]))?)',comment['text'])
    comments_from_competition.append([comment['user_id'],participants])
  return comments_from_competition

def is_users_exist(user_name):
  return bot.get_user_id_from_username(user_name)  is not None

def get_users_id_username(users_name):
  infromation_about_users = []
  for user,comment in users_name:
    infromation_about_users.append([bot.get_username_from_user_id(user),user])
  return infromation_about_users




def get_liked_and_commented(usernames_and_ids):
    liked_and_commented = []
    for user_name,id_user in usernames_and_ids:
        if str(id_user) in all_users_who_liked:
            liked_and_commented.append(id_user)
    return liked_and_commented

def get_username_of_participants(liked_and_commented):
    username_of_participants = []
    for user in set(liked_and_commented):
        username = bot.get_username_from_user_id(user)
        username_of_participants.append(username)
    return username_of_participants

def get_check_followers(username_of_participants):
    main_instagram_followers = bot.get_user_followers('beautybar.rus')
    users_all_done = []
    for username in username_of_participants:
        if bot.get_username_from_user_id(username) in main_instagram_followers:
            users_all_done.append(username)
    return users_all_done

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
    args = parser.parse_args()

    user_id = bot.get_media_id_from_link(args.user_id)
    user_comments = bot.get_media_comments(user_id)
    users = get_comments(user_comments)
    usernames_and_ids = get_users_id_username(users)
    all_users_who_liked = bot.get_media_likers(user_id)
    username_of_participants = get_liked_and_commented(usernames_and_ids)
    check_followers = get_username_of_participants(username_of_participants)
    print(get_check_followers(check_followers))

