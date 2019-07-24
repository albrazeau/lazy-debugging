from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def search_error(error):
    """Opens chrome, searchs for the error and opens each stackoverflow answer in a new tab"""
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    driver.maximize_window()
    search = driver.find_element_by_name("q")
    search.send_keys(f"stackoverflow {error}")
    search.send_keys(Keys.RETURN)
    elems = driver.find_elements_by_xpath("//a[@href]")
    all_results = []
    for elem in elems:
        link = elem.get_attribute("href")
        if "stackoverflow.com/questions" in link:
            if not "webcache" in link:
                all_results.append(link)
    for url in all_results:
        driver.execute_script(f"""window.open("{url}","_blank");""")
    return
