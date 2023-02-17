from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import io
from PIL import Image
import time

path = 'C:\\Program Files (x86)\\chromedriver.exe'
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(path)

pokemon = 'Jigglypuff'
url = ("https://archives.bulbagarden.net/wiki/Category:{s}")
driver.get(url.format(s=pokemon))

def scroll():
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(5)

def download_image(download_path, url, file_name):
	try:
		image_content = requests.get(url).content
		image_file = io.BytesIO(image_content)
		image = Image.open(image_file)
		file_path = download_path + file_name

		with open(file_path, "driver") as f:
			image.save(f, "png")

		print("Success")
	except Exception as e:
		print('FAILED -', e)

img_list = []
max_images = 100
thumbnails = driver.find_elements(By.CLASS_NAME, "image")
for img in thumbnails:
    img_list.append(img.get_attribute('src'))

'''
while(len(img_list) < max_images):
    scroll()
    thumbnails = driver.find_elements(By.CLASS_NAME, "image")
    for img in thumbnails[len(img_list): max_images]:
        #try:
         #   img.click()
          #  time.sleep(5)
        #except:
         #   continue

        images = driver.find_elements(By.CLASS_NAME, "image")
        for image in images:
            if image.get_attribute('src') in img_list:
                max_images += 1
                break
            if image.get_attribute('src') and 'http' in image.get_attribute('src'):
                img_list.add(image.get_attribute('src'))
                print(f"Found {len(img_list)} images")
    break
'''
for i, url in enumerate(img_list):
    download_image(f"C:\\Users\\Johna\\OneDrive\\Desktop\\PokemonImageRecognitionProject\\Pokemon_Image_Recognition\\{pokemon}\\", url, str(i) + ".jpg")

driver.quit()

