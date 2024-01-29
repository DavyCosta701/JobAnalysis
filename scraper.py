import time
import constants
import DataClass
from playwright.sync_api import sync_playwright
import random


def get_jobs(job_name:str):
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(user_agent=random.choice(constants.USERAGENTS))
        page = context.new_page()
        
        page.goto(f'https://www.google.com/search?q={job_name.replace(' ', '+')}+&sca_esv=593914606&ei=acGLZamaOMLT1sQPpbyr2As&uact=5&oq={job_name.replace(' ', '+')}+jobs&gs_lp=Egxnd3Mtd2l6LXNlcnAiGGVuZ2VuaGVpcm8gZGUgZGFkb3Mgam9iczIGEAAYFhgeSP8LUIMCWIELcAJ4AZABAJgBuQGgAbgGqgEDMC41uAEDyAEA-AEBwgIKEAAYRxjWBBiwA8ICDRAAGIAEGIoFGEMYsAPCAgUQABiABMICChAAGIAEGIoFGEPiAwQYACBBiAYBkAYK&sclient=gws-wiz-serp&ibp=htl;jobs&sa=X&ved=2ahUKEwjG9LiB_K6DAxVGppUCHVy8CeQQutcGKAF6BAgZEAY#fpstate=tldetail&htivrt=jobs&htilrad=-1.0&htidocid=Watm9UEt-j4nuqDlAAAAAA%3D%3D',
                timeout=30000)
        page.wait_for_timeout(5000)
        
        page.locator('//*[@id="VoQFxe"]/div[1]/div/ul/li[1]/div/div[1]/div[2]/div/div/div[2]').click()
        
        for _ in range(20):
            page.mouse.wheel(0, 15000)
            time.sleep(1)
            
        first_description = page.locator('.HBvzbc').all()
        second_description = page.locator('.WbZuDe').all()
        string_to_store = '\n'.join([item.inner_text() for item in first_description]) + \
            '\n'.join([item.inner_text() for item in second_description])
        
        with open(f'raw/{job_name.replace(" ", "_")}.txt', 'w', encoding="utf-8") as f:
            f.write(string_to_store)
                
        

if __name__  == '__main__':
    
    for job in constants.JOBLIST:
        get_jobs(job)  