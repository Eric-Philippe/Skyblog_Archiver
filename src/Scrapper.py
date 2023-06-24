from bs4 import ResultSet 
from Post import *

def get_posts (div):
    # Get all div inside it with the id starting with a 'a-'
    divs = div.find_all("div", id=lambda value: value and value.startswith("a-"))
    posts = []
    # Loop
    for div in divs:
        # Get the image
        image = get_image(div)
        # Get the text
        texte = get_texte(div)
        # Get the date
        date = get_date(div)
        # Create a Post object
        post = Post(texte, image, date)
        posts.append(post)
    return posts

def get_image (resultSet: ResultSet):
    # Get the content inside the div with the class image-container
    image_container = resultSet.find("div", class_="image-container")
    if (image_container is None):
        return None
    image = image_container.find("img")
    return image.get("src")

def get_texte (resultSet: ResultSet):
    # Get the content inside the div with the class text-container
    text_container = resultSet.find("div", class_="text-image-container")
    return text_container

def get_date (resultSet: ResultSet):
    # Get the date from the <p> with the tag itemprop="dateCreated"
    date = resultSet.find("time", itemprop="dateCreated")
    return date.get_text()