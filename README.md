# Что умеет Instabot, краткое описание 
 Данный скрипт предназначен для приложение Instagram.С помощью instabot мы проверяем выполнение условия конкурса в интсаграме :<br>
<ul>
  <li>подписка на акаунт, который что-то разыгрывает;</li>
  <li>лайк на посте о розыгрыше;</li>
  <li>соответствующие комментарии, а именно отметить одного и более друзей или знакомых;</li>
</ul>

# Требования к окружению
 Python 3.5> <br>
 terminal (MacOs)<br>
 console (Linux) <br>
 акаунт зарегистрированный в Instagram(желательно не основной) 
 
# How to install
Python3 have to be already installed. Then use pip (or pip3, there is a contravention with Python2) to install dependencies: :<br>

``` git clone https://github.com/djeck1432/instabot.git ```

After you downloaded the repository open a folder ```instabot``` using next command: <br>

```cd instabot```

Now all of the required libraries and modules have to be installed:<br>

```pip install -r requirements.txt ```<br>

Now we are ready for the script.

# Настройки окружения 

Для того, что бы код работал правильно, вам нужно будет ввести  две переменные:<br>
```INSTAGRAM_USER_NAME ``` - логин/имейл вашего акаунта в Instagram <br>
```INSTAGRAM_PASSWORD ``` - пароль от вашего акаунта в Instagram <br>
Эти переменные нужны для того, что бы ```InstaBot ```, работал от имени вашего акаунта.

# Примеры запуска скриптов
Запускаем наш скрипт :
```
(env) MacBook-Air:instabot user_name$ python3 main.py https://www.instagram.com/p/BrbkCltHo2K/ beautybar.rus
```
```https://www.instagram.com/p/BrbkCltHo2K/``` - ссылка на конкурсный пост; <br>
```beautybar.rus``` - название страницы, где проводится конкурс;

Результат получим следующий : 
```
2019-11-20 19:44:40,015 - INFO - Instabot Started
['vyvyonthatbeat', 'betweenballoons', 'wanderfordelicious', 'wong.foodie', 'galaxyoverlord', 'exobrandi', 'neverneutral', 'sundaeonasunday_', 'mariseeezy', 'bvcktrack', 'worldismymenu', '_cfooddiet', 'chips_chipster', 'foodiema', 'foodandsachi', 'createwithmi', 'louie.the.foodie']
2019-11-20 19:44:55,171 - INFO - Total requests: 208
```
Где ```['vyvyonthatbeat', 'betweenballoons', 'wanderfordelicious', 'wong.foodie', 'galaxyoverlord', 'exobrandi', 'neverneutral', 'sundaeonasunday_', 'mariseeezy', 'bvcktrack', 'worldismymenu', '_cfooddiet', 'chips_chipster', 'foodiema', 'foodandsachi', 'createwithmi', 'louie.the.foodie']``` - это список участников, которые выполнили условия конкурса.






 
  
 
