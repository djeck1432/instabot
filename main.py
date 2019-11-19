from instabot import Bot
from dotenv import load_dotenv
import argparse
import re
import os



def get_search(comments):
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




def get_liked_and_commented(username_and_id):
    liked_and_commented = []
    for user_name,id_user in username_and_id:
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
    #load .env file
    load_dotenv()

    #get variable from .env file
    secret_user_name = os.getenv("INSTAGRAM_USER_NAME")
    sercer_user_password = os.getenv("INSTAGRAM_PASSWORD")

    #conection to instabot
    bot = Bot()

    #login in your insta account
    bot.login(username=secret_user_name, password=sercer_user_password)

    #create a describe arpgparse paramter
    parser = argparse.ArgumentParser(
        description='Проверяет, кто выполнил условие конкурса в инстаграме'
    )
    parser.add_argument('user_id', help='Введите ссылку на пост розыграша')
    args = parser.parse_args()

    #get user_id
    user_id = bot.get_media_id_from_link(args.user_id)

    #get comments from user_id
    user_comments = bot.get_media_comments(user_id)

    #get users, who leaved comment
    users = get_search(user_comments)

    #get list of username
    username_and_id = get_users_id_username(users)

    #get users, who liked
    all_users_who_liked = bot.get_media_likers(user_id)

    #get user, who made all contributions
    username_of_participants = get_liked_and_commented(username_and_id)

    #print out result
    check_followers = get_username_of_participants(username_of_participants)
    print(get_check_followers(check_followers))
