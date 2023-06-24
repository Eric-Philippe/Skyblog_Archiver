import os
import requests
from bs4 import Tag

"""
    Skyblog Post class
"""
class Post(object):
    def __init__(self, text: Tag, imageURL: str, date: str):
        self.text = text
        self.imageURL = imageURL
        self.date = date

    """
        Text getter
    """
    def get_texte(self):
        return self.text
    
    """
        Image getter
    """
    def get_image(self):
        return self.imageURL
    
    """
        Date getter
    """
    def get_date(self):
        return self.date
    
    """
        Convert the post to html
    """
    def toHTML(self, folderName: str):
        htmlContent = "<div class=\"post\">"
        if self.imageURL is not None:
            # Locally save the image inside the img folder itself inside the folderName
            imgName = self.imageURL.split("/")[-1]
            imgPath = folderName + "/img/" + imgName
            self.saveImgToFolder("../" + folderName, self.imageURL)
            # Add the image to the html
            htmlContent += "<a href=\"img/" + imgName + "\" class=\"lightbox\" data-lightbox=\"post-images\"><img src=\"img/" + imgName + "\" /></a>"
        
        # Add the text to the html
        htmlContent += self.text.prettify()

        # Add the date to the html
        htmlContent += "<p class=\"date\">" + self.date + "</p>"
        htmlContent += "</div>"

        return htmlContent
    
    """
        Save the image to the folder
    """
    def saveImgToFolder(self, folderName: str, url:str):
        filename = url.split("/")[-1]
        folder_path = os.path.join(folderName, "img")
        save_path = os.path.join(folder_path, filename)
        response = requests.get(url)
        if response.status_code == 200:
        # Save the image to the specified path
            with open(save_path, 'wb') as file:
                file.write(response.content)
        else:
            print(f"Failed to download image. Status code: {response.status_code}")