import requests
import lxml
from bs4 import BeautifulSoup
import smtplib


url = "https://www.amazon.in/Bose-SoundLink-Bluetooth-Portable-Waterproof/dp/B099T738ZC/ref=pb_allspark_dp_sims_pao_desktop_session_based_d_sccl_2_5/260-5131021-3978714?pd_rd_w=Y8rNf&content-id=amzn1.sym.0c2e13d1-3874-45db-864e-478422a97adc&pf_rd_p=0c2e13d1-3874-45db-864e-478422a97adc&pf_rd_r=807CV2J3YW70HQ8KXER1&pd_rd_wg=B0ovo&pd_rd_r=31033af4-3d63-4aa9-9838-4d74b87fd315&pd_rd_i=B099T738ZC&th=1"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("₹")[1]
new_string = price_without_currency.replace(",", "")
price_as_float = int(float(new_string))
print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)

MY_EMAIL = "saurabh1991Tidgam@gmail.com"
MY_PASSWORD = "pfwuzmcfoybatwam"
SMTP_ADDRESS = "smtp.gmail.com"

BUY_PRICE = 10000

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="saurabh.siddtech.in",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )