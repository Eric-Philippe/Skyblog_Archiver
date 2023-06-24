import requests
from bs4 import BeautifulSoup
from Scrapper import *
from PostsToHTML import *
from ProgressBar import *

"""
    Archivers class
    This class will be used to archive a skyblog and make the link between the user input and the scrapper
"""
class Archivers(object):
    def __init__(self):
        self.posts = []

    """
        Start the archiving process
    """
    def start(self):
        print("Please enter the username of the skyblog you want to archive : ")
        self.username = input(">>> ")

        articles_div = self.load_articles()
        if articles_div is None:
            print("This skyblog does not exist")
            exit()
        else: self.articles_div = articles_div

        self.load_posts()

        # Print in green
        print("\033[92m")
        print("Posts loaded successfully")

        convert = PostsToHTML(self.posts)
        convert.run(self.username)

        print("\033[92m")
        print("Images loaded successfully")

        # End
        print("\033[92m")
        print("Done !")
    
        # Find your archive here : {full path}
        print("\033[0m")
        folderPath = os.getcwd()
        # Remove the src/
        folderPath = folderPath[:-4]
        folderPath += "/" + convert.get_user_folder_name()
        print("Find your archive here : " + folderPath)

        print("\n")
        self.hoster = input("Do you want to host your archive locally on a website ? (y/n) ")
        if self.hoster == "y":
            self.host_local()
        else:
            exit()

    """
        Load the articles div from the skyblog
    """
    def load_articles(self):
        url = "https://" + self.username + ".skyrock.com/1.html"
        response = requests.get(url)
        html_content = response.text
        self.soup = BeautifulSoup(html_content, "html.parser")
        articles_div = self.soup.find("div", id="articles_container")

        # Get the highest page number
        pagination = self.soup.find("form", class_="pagination")
        self.pages = 1
        if pagination is not None:
            options = pagination.find_all("option")
            numPageStr = options[-1].get_text().split(" ")[1]
            self.pages = int(numPageStr[2:])
        
        return articles_div

    """
        Load the posts from the articles div
    """
    def load_posts(self):
        # We expect to have self.pages * 5 posts to load
        # Make a progress bar in the console that will show the progress replacing . with #
        print("Loading posts...")

        progress_bar = ProgressBar(self.pages * 5)
        # Loop trough the 1.html to the self.pages.html
        for i in range(1, self.pages + 1):
            url = "https://" + self.username + ".skyrock.com/" + str(i) + ".html"
            response = requests.get(url)
            html_content = response.text
            soup = BeautifulSoup(html_content, "html.parser")
            articles_div = soup.find("div", id="articles_container")
            posts = get_posts(articles_div)
            self.posts += posts
            
            progress_bar.update(i * 5)

            if i != self.pages:
                print("\033[93m", end="")
            else:
                print("\033[92m", end="")

    """
        Return the posts
    """
    def get_posts(self):
        return self.posts
    
    """
        Host the archive on a local server
    """
    def host_local(self):
        print("Hosting your archive on a local server...")

        #os.system("python3 -m http.server 8000 --directory " + os.getcwd() + "/" + self.username + "_Skyblog_Archive")
        folderAdress = os.getcwd() + "/"
        # Remove the src/ from the path /home/ericp/Desktop/Skyblog_Archiver/src/leeloo3189_Skyblog_Archive
        folderAdress = folderAdress[:-4]
        folderAdress += self.username + "_Skyblog_Archive"

        os.system("python3 -m http.server 8000 --directory " + folderAdress + " > /dev/null 2>&1 &")
        print("\033[92m")
        print("Done !")
        print("Find your archive here : http://localhost:8000/")