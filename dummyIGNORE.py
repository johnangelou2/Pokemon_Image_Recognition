url = ("https://archives.bulbagarden.net/wiki/Category:{s}")
# Launch the browser and open the given url in the webdriver.
driver.get(url.format(s='Jigglypuff'))

# Scroll down the body of the web page and load the images.
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(5)

# Find the images.
imgResults = driver.find_elements(By.XPATH,"//img[contains(@class,'image')]")
# Access and store the scr list of image url's.
src = []
for img in imgResults:
    src.append(img.get_attribute('src'))

# Retrieve and download the images.
for i in range(10):
    urllib.request.urlretrieve(str(src[i]),"sample_data/image{}.jpg".format(i))