import requests
import shutil
import os
TEMP_DIR = "temp_images/"


def download_image(url, filename):
    # Path to save the downloaded image
    file_path = os.path.join(TEMP_DIR, filename)
    
    # Send GET request to the image URL
    response = requests.get(url, stream=True)
    
    if response.status_code == 200:
        # Write the image content to a file
        with open(file_path, "wb") as out_file:
            shutil.copyfileobj(response.raw, out_file)
        return file_path
    else:
        # raise HTTPException(status_code=400, detail=f"Could not download image from {url}")
        print("Error")


download_image("https://res.cloudinary.com/di8ui03yr/image/upload/v1725744806/product-images/photo_zac0km.png", 'yoyo.jpg')