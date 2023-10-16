from playwright.sync_api import Playwright, sync_playwright, expect
from configparser import ConfigParser
import sys
import calendar

'''
input command in command line:
python main.py d.m.yyyy
eg. Today is 03/08/2023 then the command will be: python main.py 3.8.2023
'''
script, today = sys.argv
first_weekday, days_count = calendar.monthrange(int(today.split(".")[2]),int(today.split(".")[1])-1)

#Customer list provided by Dirk
CWID_LIST = ["001.15916604","002.01008206549","002.01008206536","002.01008206576","002.01008206605","002.01008206560","002.01008206569",
                 "002.01008206598","002.01008206596","002.01008206592","002.01008206584","002.01008206612","002.01008206619","002.01008206624",
                 "002.01008206629","002.01008206610","002.01008206642","002.01008206650","002.01008206653","002.01008206664","002.01008206679",
                 "002.01008426326","002.01009001310"]

def _get_credential_info():
    config = ConfigParser()
    config.read('secrets.ini')
    return (config['scoutaccount']['username'],config['scoutaccount']['password'],config['scoutaccount']['token'])

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://web.is24-commercial-success-report.s24cloud.net/")
    page.goto("https://web.is24-commercial-success-report.s24cloud.net/sign-in?return_to=%2F")
    page.goto("https://login.microsoftonline.com/56198f48-9c36-4c13-9f9e-f686123d07b5/oauth2/v2.0/authorize?response_type=code&client_id=9267dde9-8ac6-42e5-8b36-fcbfe43f49c0&scope=openid%20email&state=lrUeaR4Erq84gW0Vxdwr_qRJXV8e7qV8xR8FltcLt5o%3D&redirect_uri=https://auth.immobilienscout24.de/login/oauth2/code/&nonce=NZLYUGCEetYD9yZe_FGBqpdEnWUdn4Cs6ROVVfjqbHc")
    page.get_by_placeholder("Email, phone, or Skype").click()
    page.get_by_placeholder("Email, phone, or Skype").fill(_get_credential_info()[0])
    page.get_by_placeholder("Email, phone, or Skype").press("Enter")
    page.locator("#i0118").fill(_get_credential_info()[1])
    page.locator("#i0118").press("Enter")
    page.goto(f"https://web.is24-commercial-success-report.s24cloud.net/auth?token={_get_credential_info()[2]}")
    page.goto("https://web.is24-commercial-success-report.s24cloud.net/")
    # page.locator("div").nth(1).click()
    page.get_by_placeholder("Hier Kunden ID (CWID) eingeben").click()
    page.get_by_placeholder("Hier Kunden ID (CWID) eingeben").click()
    page.get_by_placeholder("Hier Kunden ID (CWID) eingeben").fill(CWID_LIST[0])
    page.get_by_role("button", name="Report generieren").click()

    page.get_by_placeholder(f"z.B. {today}").click() #1.6.2023
    page.get_by_role("button", name="1", exact=True).first.click()
    page.get_by_role("button", name=str(days_count)).nth(1).click() #"31"
 

    page.get_by_role("button", name="OK").click()
    with page.expect_download() as download_info:
        page.get_by_test_id("download-button").click()
    download = download_info.value
    # print(download.path())
    download.save_as(f'/Users/hta/Downloads/success_report_{CWID_LIST[0]}.xlsx')
    for i in range(1,len(CWID_LIST)):
        page.get_by_role("button", name="+ Neuer Report").click()
        page.get_by_placeholder("Hier Kunden ID (CWID) eingeben").fill(CWID_LIST[i])
        page.get_by_role("button", name="Report generieren").click()
        page.get_by_placeholder(f"z.B. {today}").click()
        page.get_by_role("button", name="1", exact=True).first.click()
        page.get_by_role("button", name=str(days_count)).nth(1).click()
        # page.get_by_role("button", name=str(days_count)).click()
        page.get_by_role("button", name="OK").click()
        with page.expect_download() as download1_info:
            page.get_by_test_id("download-button").click()
        download1 = download1_info.value
        download1.save_as(f'/Users/hta/Downloads/success_report_{CWID_LIST[i]}.xlsx')

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
