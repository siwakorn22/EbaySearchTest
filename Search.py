from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
from datetime import datetime

# สร้าง instance ของเบราว์เซอร์
driver = webdriver.Chrome()  # ต้องมี Chrome WebDriver ใน PATH

# เปิดหน้าเว็บ eBay
driver.get("https://www.ebay.com")

# ขยายหน้าต่างเบราว์เซอร์ให้เต็มจอ
driver.maximize_window()

# ค้นหาคำว่า "car" ในช่องค้นหา
search_box = driver.find_element("name", "_nkw")
search_box.send_keys("psvita")
search_box.send_keys(Keys.RETURN)

# รอให้ผลการค้นหาปรากฏขึ้น
driver.implicitly_wait(10)  # รอไม่เกิน 10 วินาที

# เก็บ URL ของหน้าเว็บที่เรียกใช้งาน
current_url = driver.current_url

# ตรวจสอบว่ามีข้อความ "OLED" ปรากฏในหน้าเว็บหรือไม่
if "OLED" in driver.page_source:
    result = "pass"
    reason = "Test passed successfully. Keyword 'OLED' found on the page."
else:
    result = "failed"
    reason = "Test failed. Keyword 'OLED' not found on the page."

# ปิดหน้าเว็บ eBay
driver.quit()

# ตรวจสอบการผ่านหรือไม่ผ่าน
# เช็คโดย url 
if "psvita" in current_url:
    result = "pass"
    reason = "Test passed successfully."
else:
    result = "failed"
    reason = "Test failed. Keyword 'psvita' not found in URL."



# เพิ่มข้อมูลลงในไฟล์ CSV
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
csv_row = [timestamp, current_url, result, reason]

with open("test_history.csv", "a", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(csv_row)
