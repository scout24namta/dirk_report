from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://web.is24-commercial-success-report.s24cloud.net/")
    page.goto("https://web.is24-commercial-success-report.s24cloud.net/sign-in?return_to=%2F")
    page.goto("https://login.microsoftonline.com/56198f48-9c36-4c13-9f9e-f686123d07b5/oauth2/v2.0/authorize?response_type=code&client_id=9267dde9-8ac6-42e5-8b36-fcbfe43f49c0&scope=openid%20email&state=mSSdJ1o5mqFEj7LL5ndaT2n4hs9m81bZM9XNtGr6zeE%3D&redirect_uri=https://auth.immobilienscout24.de/login/oauth2/code/&nonce=st5Dt8AxEjTDbHodPgSfZKl3gmetxp83bVq4WebwDS8")
    page.get_by_placeholder("Email, phone, or Skype").click()
    page.get_by_placeholder("Email, phone, or Skype").fill("hai.ta@scout24.com")
    page.get_by_placeholder("Email, phone, or Skype").press("Enter")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("Thanhninhtahainam112358")
    page.get_by_placeholder("Password").press("Enter")
    page.goto("https://web.is24-commercial-success-report.s24cloud.net/auth?token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJoYWkudGFAc2NvdXQyNC5jb20iLCJleHAiOjE2OTY1NTc1NzAsImlhdCI6MTY5NjUxNDM3MH0.12FPBvSes5Lx3ynKXNwXouz1jXNgb5cVXP1uiKzNuE4h7JWLHRQ6j9qKrfIwiixcDatFcRc-EGl86B9NTPx4rA&return_to=%2F")
    page.goto("https://web.is24-commercial-success-report.s24cloud.net/")
    page.get_by_placeholder("Hier Kunden ID (CWID) eingeben").click()
    page.get_by_placeholder("Hier Kunden ID (CWID) eingeben").fill("001.15916604")
    page.get_by_role("button", name="Report generieren").click()
    page.get_by_placeholder("z.B. 5.10.2023").click()
    page.get_by_role("button", name="1", exact=True).first.click()
    page.get_by_role("button", name="30").nth(1).click()
    page.get_by_role("button", name="OK").click()
    with page.expect_download() as download_info:
        page.get_by_test_id("download-button").click()
    download = download_info.value
    page.get_by_role("button", name="+ Neuer Report").click()
    page.get_by_placeholder("Hier Kunden ID (CWID) eingeben").click()
    page.get_by_placeholder("Hier Kunden ID (CWID) eingeben").fill("001.15916604")
    page.get_by_role("button", name="Report generieren").click()
    page.get_by_placeholder("z.B. 5.10.2023").click()
    page.get_by_role("button", name="1", exact=True).first.click()
    page.get_by_role("button", name="30").nth(1).click()
    page.get_by_role("button", name="OK").click()
    with page.expect_download() as download1_info:
        page.get_by_test_id("download-button").click()
    download1 = download1_info.value

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
