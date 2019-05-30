import time, selenium.webdriver

print('Start')
# driver = selenium.webdriver.Chrome()
driver = selenium.webdriver.Firefox()
print('Terminated: set driver')
driver.set_window_size(1024, 768)
filename = 0

for url in open("websites.txt"):
    driver.get(url)
    print(driver.title)
    time.sleep(5)
    driver.save_screenshot("%03d.png"%(filename))
    filename += 1

driver.quit()
