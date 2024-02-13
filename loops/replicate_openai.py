# Use of Dall-e 2 API taken from https://www.makeuseof.com/generate-images-using-openai-api-dalle-python/
# Use of Replicate image-to-text API taken from official documentation

import openai
import replicate

import os
import requests
from dotenv import load_dotenv
from PIL import Image

load_dotenv()


class ImageGenerator:
    def __init__(self) -> str:
        self.image_url: str
        openai.api_key = "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"
        self.APIKey = openai.api_key
        self.name = None

    def generateImage(self, Prompt, ImageCount, ImageSize):
        try:
            self.APIKey
            response = openai.Image.create(
            prompt=Prompt,
            n=ImageCount,
            size=ImageSize,
            )
            self.image_url = response['data']

            self.image_url = [image["url"] for image in self.image_url]
            # print(self.image_url)
            return self.image_url
        except openai.error.OpenAIError as e:
            print(e)
            print(e.error)

    def downloadImage(self, names, fname) -> None:
        try:
            self.name = names
            for url in self.image_url:
                image = requests.get(url)
            for name in self.name:
                with open("Multichannel/loops/" + fname + "/{}.png".format(name), "wb") as f:
                    f.write(image.content)
        except:
            print("An error occured")
            return self.name

# Instantiate the class
imageGen = ImageGenerator() 

i = 1
a = 1

e = 0
d = 0
m = 1

filen = 'genloopres'

# format of generated images, currently set up for a folder with two different images, doing one iteration for each
while (1):

    mi = i%10
    di = i//10
    ei = i//100

    # Text description of input image
    output = replicate.run(
        "pharmapsychotic/clip-interrogator:a4a8bafd6089e1716b06057c42b19378250d008b80fe87caa5cd36d40c1eda90",
        input={"image": open("Multichannel/loops/" + filen + "/Pres{}{}{}.png".format(ei,di,mi), "rb"), "clip_model_name": "ViT-L-14/openai", "mode": "fast"} #ViT-H-14/laion2b_s32b_b79k, ViT-L-14/openai
    )


    # Generate image:
    imageGen.generateImage(
    Prompt = output,
    ImageCount = 1,
    ImageSize = '1024x1024'#'512x512'
    )

    i+=1
    a=i+1
    m = a%10
    d = a//10
    e = a//100

    # Download the images:
    imageGen.downloadImage(names=[
    "Pres{}{}{}".format(e,d,m)
    ], fname=filen)

    

  

