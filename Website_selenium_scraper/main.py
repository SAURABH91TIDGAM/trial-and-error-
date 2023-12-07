from selenium import webdriver
from selenium.webdriver.common.by import By

# keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.in/Bose-SoundLink-Bluetooth-Portable-Waterproof/dp/B099T738ZC/ref=pd_ci_mcx_mh_mcx_views_0?pd_rd_w=Hwjvw&content-id=amzn1.sym.cd312cd6-6969-4220-8ac7-6dc7c0447352%3Aamzn1.symc.ca948091-a64d-450e-86d7-c161ca33337b&pf_rd_p=cd312cd6-6969-4220-8ac7-6dc7c0447352&pf_rd_r=Y4C21Z6VNDHD2VMFPPQW&pd_rd_wg=4YXli&pd_rd_r=00e827c5-c2e4-4aa3-bc2e-3e87572e83ad&pd_rd_i=B099T738ZC&th=1")

price_rupees = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents =driver.find_elements(By.CLASS_NAME, value="" )

print(f"The price is {price_rupees.text} ₹ rupees")

driver.close()