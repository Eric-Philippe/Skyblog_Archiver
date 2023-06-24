import shutil
from Post import Post
from ProgressBar import ProgressBar

"""
    Posts to HTML class
    This class will be used to convert the posts to html
"""
class PostsToHTML:
    def __init__(self, posts: list[Post]):
        self.posts = posts

    """
    Run the conversion
    """
    def run(self, username: str):
        self.username = username
        self.copy_template()
        self.fillIndexHtml()

    """
    Copy the archiver_template folder and rename it to the username
    """
    def copy_template(self):
        user_folder_name = self.username + "_Skyblog_Archive"
        shutil.copytree("archiver_template", "../" + user_folder_name)
        self.user_folder_name = user_folder_name

    """
    Replace every {{ username }} in the index.html file with the username
    And fill the div with the id "posts" with the posts
    """
    def fillIndexHtml(self):
        # Open the index.html file
        index_file = open("../" + self.user_folder_name + "/index.html", "r")
        # Read the content
        index_content = index_file.read()
        # Replace the {{ username }} with the username
        index_content = index_content.replace("{{ username }}", self.username)
        # Fill the div with the id "posts" with the posts
        posts_html = ""

        print("\033[33m", end="")
        print("Downloading images ...")
        length = len(self.posts)

        progress_bar = ProgressBar(length)

        for i, post in enumerate(self.posts):
            post = self.posts[i]
            posts_html += post.toHTML(self.user_folder_name)

            progress_bar.update(i + 1)
        
        index_content = index_content.replace("{{ posts }}", posts_html)

        # Close the file
        index_file.close()
        # Open the file in write mode
        index_file = open("../" + self.user_folder_name + "/index.html", "w")
        # Write the new content
        index_file.write(index_content)
        # Close the file
        index_file.close()
    
    """
    Return the user folder name
    """
    def get_user_folder_name(self):
        return self.user_folder_name