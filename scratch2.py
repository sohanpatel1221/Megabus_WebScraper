from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from datetime import date,timedelta
import smtplib
from datetime import date


def buildDriver():
    day = date.today() + timedelta(days=5)
    url = "https://us.megabus.com/journey-planner/journeys?days=1&concessionCount=0&departureDate=" + str(day) + "&destinationId=142&inboundOtherDisabilityCount=0&inboundPcaCount=0&inboundWheelchairSeated=0&nusCount=0&originId=299&otherDisabilityCount=0&pcaCount=0&totalPassengers=1&wheelchairSeated=0"
    location = r'C:\Users\sohan\Lib\site-packages\selenium\webdriver\chromedriver.exe'
    settings = Options()
    settings.add_argument("--headless")
    settings.add_argument("--window-size=60000,3000")
    global driver
    driver = Chrome(options=settings, executable_path=location)
    driver.get(url)

def sendemail(from_addr, to_addr_list, cc_addr_list,subject, message,login, password,smtpserver='smtp.mailtrap.io:587'):
    header = 'From: %s' % from_addr
    header += 'To: %s' % ', '.join(to_addr_list)
    header += 'Cc: %s' % ', '.join(cc_addr_list)
    header += 'Subject: %s' % subject
    message = header + message

    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login, password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    # sendemail("gs.pateltutoring@gmail.com", "sohanpatel1221@gmail.com","", "hello","hello", "b880f6349b02c4", "34f4140cfb6586")

def collectinfo():
    elements = driver.find_elements(By.XPATH, '//span[@class="ng-star-inserted"]')
    elementskv = {}
    for i in range(0, len(elements), 2):
        elementskv[elements[i].text] = elements[i + 1].text

    print(elementskv)