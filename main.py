import pathlib
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from random import randrange





posts_file = open('posts.txt')
interacted_posts = []  # you can leave this alone
for x in posts_file:
    add = x.split()
    for y in add:
        interacted_posts.append(y)

posts_file.close()
#print(postsArr)


comment_arr = [
                        ['this', 'the', 'your'],
                       ['photo', 'picture', 'pic'],
                       ['is', 'looks', 'is really'],
                       ['great', 'awesome', 'good', 'cool', 'fantastic']
            ]

class InstaBot :
    def __init__(self, username, password): # need username and pw, take these as inputs
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

        max_likes_per_day = 5
        max_comments_per_day = 0
        hashtag_arr = ['wieners']  # this is the array of hashtags the app will interact with
        max_like_per_tag = 50
        follows_per_day = 50
        follow_time = 1 * 60
        unfollow_per_day = 50
        unfollow_break_min = 15 # in minutes
        unfollow_break_max = 50
        # this is the array of comments the bot will comment on posts it interacts with



        # self.login()


        sleep(4)

        rand_num = randrange(0, len(hashtag_arr))
        self.search_hashtags(hashtag_arr[rand_num])

        new_posts = []
        self.collect_links(new_posts)

        sleep(4)
        print(new_posts)



        like_count = 0
        while like_count < max_likes_per_day: # should have 2nd nested while for likes per tag?
            rand_num = randrange(0, len(new_posts)) # need to pop off elements from new post when they've been interacted with
            self.interact(new_posts[rand_num], new_posts, rand_num)
            like_count += 1

        # Should have new posts and previously interacted posts arr


        self.driver.close()



    def login(self):
        self.driver.get("https://instagram.com")
        sleep(4)
        self.driver.find_element_by_xpath("//input[@name='username']").send_keys('')
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys('')
        self.driver.find_element_by_xpath("//button[@type='submit']").click()

    def interact(self, url, arr, index):
        self.like_post(url)
        #self.comment(url)
        print(arr)
        print(index)
        arr.pop(index)
        f = open('posts.txt', 'a')
        f.write(url + '\n')
        f.close()
        print('test interaction')

    def like_post(self, url):  # like certain posts based on hash or username
        print('test like post')
        self.driver.get(url)
        # xpath of the like button
        # /html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button
        #self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()
        sleep(3)

    def follow(self):
        print('test following')
        # assuming we're on a post page, we have to:
        # 1: click their profile link
        # 2: find the follow button
        # 3: click it

        profile_link = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/header/div[2]/div[1]/div[1]/span/a')
        profile_link.click()
        sleep(4)
        follow_button = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[2]/div/div/div/button')
        follow_button.click()





    def comment(self, url): # This works!!! don't change it for now!!!
        print('test comment')
        comment_text = self.gen_comment()
        comment_box = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea')
        comment_box.clear()
        comment_box.click()

        comment_box = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea')
        sleep(4)
        comment_box.send_keys(comment_text)
        # post button
        # /html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button

    def gen_comment(self):
        print('test comment gen')
        comment = ''
        for x in range(len((comment_arr))):
            y = randrange(0, len(comment_arr[x]))
            comment += " " + comment_arr[x][y]

        print(comment)
        return comment

    def search_hashtags(self, hashtag):
        print('test hashtags')
        self.driver.get("https://instagram.com/explore/tags/" + hashtag)

    def collect_links(self, arr): # figure out how much to scroll to repeat this without adding duplicates
        print('testing link gathering')
        for x in range(8): # past 8 the rest haven't loaded yet
            for y in range(3):
                # find the tag using the xpath
                link = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div/div[" + str(x+1) + "]/div[" + str(y+1) + "]/a").get_attribute('href')

                if(link not in interacted_posts):
                    arr.append(link)
                    #f = open('posts.txt', 'a')
                    #f.write(link + '\n')
                    #f.close()
                else:
                    print('duplicate detected')





#   how to determine bot liking behaviour to appear
#   random, organic, and not repeat on posts/hashtags you've
#   already interacted with?
links = []
my_bot = InstaBot('billybob35341', 'notabot123')



