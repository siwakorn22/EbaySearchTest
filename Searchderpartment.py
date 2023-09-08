from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# ระบุพาธของ ChromeDriver
chrome_driver_path = "C:/Users/jay/chromedriver.exe"

# เริ่มต้น WebDriver
driver = webdriver.Chrome()
# ขยายหน้าต่างเบราว์เซอร์ให้เต็มหน้าจอ
driver.maximize_window()

# เปิดเว็บไซต์ของคุณ
driver.get("https://online-web-mauve.vercel.app/")

try:
    # ค้นหา element ที่มีคลาส "title-name-home mt-3 mx-5"
    result_element = driver.find_element(By.XPATH, "//h4[@class='title-name-home mt-3 mx-5']")

    # ใช้ assert เพื่อตรวจสอบว่าพบ element หรือไม่
    assert result_element is not None, "Fail"

    print("Success")
except Exception as e:
    print("Fail")
    print(str(e))

time.sleep(2)
