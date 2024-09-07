from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import shutil
import os
from process import is_face_match

app = FastAPI()

# Directory where images will be temporarily saved
TEMP_DIR = "temp_images/"

# Ensure the directory exists
if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR)

# Pydantic model to parse the image URLs
class ImageURLs(BaseModel):
    image_url_1: str
    image_url_2: str

@app.post("/compare-faces")
async def compare_faces(urls: ImageURLs):
    try:
        # Download the images from the provided URLs
        file1_path = download_image(urls.image_url_1, "IDImage.jpg")
        file2_path = download_image(urls.image_url_2, "SelfImage.jpg")

        # Use the face matcher function to compare the images
        match = is_face_match(file1_path, file2_path)

        # Clean up the saved files
        # os.remove(file1_path)
        # os.remove(file2_path)

        # Return the result
        return {"match": match}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing the images: {str(e)}")

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
        raise HTTPException(status_code=400, detail=f"Could not download image from {url}")

# To run the FastAPI server:
# $ uvicorn app:app --reload
