#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[1]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[1]:


pip install --upgrade selenium


# In[2]:


driver=webdriver.Chrome()


# Q10: Write a python program to display list of 50 Most expensive cars in the world (i.e. Car name and Price) from https://www.motor1.com/
# This task will be done in following steps:
# 1. First get the webpage https://www.motor1.com/
# 2. Then You have to type in the search bar ’50 most expensive cars’
# 3. Then click on 50 most expensive carsin the world..
# 4. Then scrap the mentioned data and make the dataframe.

# In[3]:


driver.get("https://www.motor1.com/")


# In[4]:


search=driver.find_element(By.XPATH,'/html/body/div[10]/div[2]/div/div/div[3]/div/div/div/form/input')
search.send_keys("50 most expensive cars")


# In[6]:


Enter=driver.find_element(By.XPATH,"/html/body/div[10]/div[2]/div/div/div[3]/div/div/div/form/button[1]")
Enter.click()


# In[7]:


Enter_Cars=driver.find_element(By.XPATH,"/html/body/div[10]/div[9]/div/div[1]/div/div/div[2]/div/div[1]/h3/a")
Enter_Cars.click()


# In[8]:


car_name=[]
price_dollar=[]


# In[9]:


title_tags=driver.find_elements(By.XPATH,'//h3[@class="subheader"]')
for i in title_tags:
    title=i.text
    car_name.append(title)


# In[10]:


value_tags=driver.find_elements(By.XPATH,'//strong["/html/body/div[10]/div[7]/div[2]/div[1]/div[2]/div[2]/p[4]"]')
for i in value_tags:
    price=i.text
    price_dollar.append(price)
                                
                                


# In[11]:


print(len(car_name),len(price_dollar))


# In[12]:


df=pd.DataFrame({'car_name':car_name,'price':price})
df


# Q9: Write a python program to display list of respected former Prime Ministers of India(i.e. Name, Born-Dead, Term of office, Remarks) from https://www.jagranjosh.com/.
# This task will be done in following steps:
# 1. First get the webpagehttps://www.jagranjosh.com/
# 2. Then You have to click on the GK option
# 3. Then click on the List of all Prime Ministers of India
# 4. Then scrap the mentioned data and make theDataFrame.

# In[13]:


driver=webdriver.Chrome()


# In[14]:


driver.get("https://www.jagranjosh.com/")


# In[15]:


Enter_GK=driver.find_element(By.XPATH,"/html/body/div/header/nav/div/div/div[3]/ul/li[3]/a")
Enter_GK.click()


# In[16]:


Enter_PM=driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div[10]/div/div/ul/li[2]/a")
Enter_PM.click()


# In[18]:


PM_NAME=[]
Born_Dead=[]
Term_of_office=[]
Remarks=[]


# In[ ]:


Name = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[3]/table/tbody/tr[2]/td[2]/p/strong/a')
for i in Name:
    PM=i.text
    PM_NAME.append(PM)
    
            


# In[ ]:


title_tags=driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[3]/table/tbody/tr[2]/td[2]/p/strong/a')
for i in title_tags:
    title=i.text
    title_tags.append(title)


# Q8: Write a python program to scrape data for Top 1000 Quotes of All Time.
# The above task will be done in following steps:
# 1. First get the webpagehttps://www.azquotes.com/
# 2. Click on TopQuotes
# 3. Than scrap a) Quote b) Author c) Type Of Quotes

# In[8]:


driver=webdriver.Chrome()


# In[9]:


driver.get("https://www.azquotes.com/")


# In[10]:


Enter_Top=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div[3]/ul/li[5]/a")
Enter_Top.click()


# 500 - Internal server error $ click on TopQuotes page didn't open

# Q7: Go to webpage https://www.amazon.in/ Enter “Laptop” in the search field and then click the search icon. Then set CPU Type filter to “Intel Core i7” as shown in the below image:
# After setting the filters scrape first 10 laptops data. You have to scrape 3 attributes for each laptop:
# 1. Title
# 2. Ratings
# 3. Price

# In[26]:


driver=webdriver.Chrome()


# In[27]:


driver.get("https://www.amazon.in/")


# In[28]:


Search=driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
Search.send_keys('Laptop')


# In[29]:


Enter=driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input")
Enter.click()


# In[30]:


click_i7=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[6]/span[10]/li/span/a/span")
click_i7.click()


# In[31]:


laptop_Title=[]
Rating=[]
Price=[]


# In[32]:


Title_tags=driver.find_elements(By.XPATH,'//div[@class="a-section a-spacing-none puis-padding-right-small s-title-instructions-style"]')
for i in Title_tags[0:10]:
    laptop=i.text
    laptop_Title.append(laptop)


# In[33]:


rating_tags=driver.find_elements(By.XPATH,'//span[@class="a-size-base puis-bold-weight-text"]')
for i in rating_tags[0:10]:
    rats=i.text
    Rating.append(rats)


# In[34]:


price_tags=driver.find_elements(By.XPATH,'//span[@class="a-price"]')
for i in price_tags[0:10]:
    rupees=i.text
    Price.append(rupees)


# In[35]:


print(len(laptop_Title),len(Rating),len(Price))


# In[36]:


df=pd.DataFrame({'laptop_Title':laptop_Title,'Rating':Rating,'Price':Price})
df


# Q6: Scrape data forfirst 100 sneakers you find whenyou visit flipkart.com and search for “sneakers” in the search field.
# You have to scrape 3 attributes of each sneaker:
# 1. Brand
# 2. ProductDescription
# 3. Price

# In[3]:


driver=webdriver.Chrome()


# In[4]:


driver.get("https://www.flipkart.com")


# In[5]:


search=driver.find_element(By.CLASS_NAME,"Pke_EE")
search.send_keys('sneakers')


# In[6]:


Enter=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/header/div[1]/div[2]/form/div/button")
Enter.click()


# In[7]:


Brand=[]
ProductDescription=[]
Price=[]


# In[8]:


#Brand
start=0
end=3
for page in range(start,end):
    titles=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    for i in titles[0:100]:
        Brand.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(4)
    


# In[9]:


len(Brand)


# In[10]:


start=0
end=3
for page in range(start,end):
    titles=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
    for i in titles[0:100]:
        ProductDescription.append(i.text)
    for i in titles:
        
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(4)


# In[11]:


len(ProductDescription)


# In[12]:


start=0
end=3
for page in range(start,end):
    titles=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
    for i in titles[0:100]:
        Price.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(4)


# In[13]:


len(Price)


# In[15]:


df=pd.DataFrame({'Brand':Brand,'Price':Price})
df


# Q5: Scrape 100 reviews data from flipkart.com for iphone11 phone. You have to go the link:https://www.flipkart.com/apple-iphone-11-black-64-gb/productreviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&marketplace=FLIPKART.
# As shown in the above page you have to scrape the tick marked attributes. These are:
# 1. Rating
# 2. Review summary
# 3. Full review
# 4. You have to scrape this data for first 100reviews.

# In[16]:


driver=webdriver.Chrome()


# In[17]:


driver.get("https://www.flipkart.com/apple-iphone-11-black-64-gb/productreviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&marketplace=FLIPKART")


# #### Unfortunately the page you are looking for has been moved or deleted

# Q4: Scrape data of first 100 sunglasses listings on flipkart.com. You have to scrape four attributes:
# 1 Brand
# 2ProductDescription
# 3Price
# The attributes which you have to scrape is ticked marked in the below image.
# To scrape the data you have to go through following steps:
# 1. Go to Flipkart webpage by url :https://www.flipkart.com/
# 2. Enter “sunglasses” in the search fieldwhere “search for products, brands and more” is written and
# click the search icon
# 3. After that you will reach to the page having a lot of sunglasses. From this page you can scrap the
# required data as usual.

# In[18]:


driver=webdriver.Chrome()


# In[19]:


driver.get("https://www.flipkart.com/")


# In[20]:


search=driver.find_element(By.CLASS_NAME,"Pke_EE")
search.send_keys('sunglasses')


# In[21]:


Enter=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/header/div[1]/div[2]/form/div/button")
Enter.click()


# In[22]:


Brand=[]
ProductDescription=[]
Price=[]


# In[23]:


#Brand
start=0
end=3
for page in range(start,end):
    titles=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    for i in titles[0:100]:
        Brand.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(4)


# In[24]:


len(Brand)


# In[25]:


# ProductDescription
start=0
end=3
for page in range(start,end):
    titles=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
    for i in titles[0:100]:
        ProductDescription.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(4)


# In[26]:


len(ProductDescription)


# In[27]:


#Price
start=0
end=3
for page in range(start,end):
    titles=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
    for i in titles[0:100]:
        Price.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(4)


# In[28]:


len(Price)


# In[29]:


df=pd.DataFrame({'Brand':Brand,'Price':Price})
df


# Q1: Write a python program to scrape data for “Data Analyst” Job position in “Bangalore” location. You
# have to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10
# jobs data.
# This task will be done in following steps:
# 1. First get the webpage https://www.shine.com/
# 2. Enter “Data Analyst” in “Job title, Skills” field and enter “Bangalore” in “enter the location” field.
# 3. Then click the searchbutton.
# 4. Then scrape the data for the first 10 jobs results you get.
# 5. Finally create a dataframe of the scraped data.

# In[13]:


driver=webdriver.Chrome()


# In[14]:


driver.get("https://www.shine.com/")


# In[18]:


designation=driver.find_element(By.CLASS_NAME,"form-control ")
designation.send_keys("Data Analyst")


# In[19]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[2]/div/input")
location.send_keys('Banglore')


# In[20]:


search=driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div[2]/div[2]/div/form/div/div[2]/div/button")
search.click()


# In[21]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[22]:


# Scraping Job title from the given page
title_tags=driver.find_elements(By.XPATH,'//h2[@itemprop="name"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)


# In[23]:


# Scraping Job location from the given page
location=driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]')
for i in location[0:10]:
    location=i.text
    job_location.append(location)


# In[24]:


# Scraping Company name from the given page
company_tags=driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_cName__mYnow"]')
for i in company_tags:
    company=i.text
    company_name.append(company)


# In[25]:


# Scraping experience required from the given page
experience_tags=driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_jobIcon__3FB1t"]')
for i in experience_tags[0:10]:
    experience=i.text
    experience_required.append(experience)


# In[27]:


print(len(job_title),len(job_location),len(experience_required))


# In[28]:


df=pd.DataFrame({'job_title':job_title,'job_location':job_location,'experience_required': experience_required})
df


# Q2:Write a python program to scrape data for “Data Scientist” Job position in“Bangalore” location. You
# have to scrape the job-title, job-location, company_name. You have to scrape first 10 jobs data.
# This task will be done in following steps:
# 1. First get the webpage https://www.shine.com/
# 2. Enter “Data Scientist” in “Job title, Skills” field and enter “Bangalore” in “enter thelocation” field.
# 3. Then click the search button.
# 4. Then scrape the data for the first 10 jobs results you get.
# 5. Finally create a dataframe of the scraped data.
# 

# In[2]:


driver=webdriver.Chrome()


# In[3]:


driver.get("https://www.shine.com/")


# In[4]:


designation=driver.find_element(By.CLASS_NAME,"form-control ")
designation.send_keys("Data Scientist")


# In[6]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[2]/div/input")
location.send_keys('Banglore')


# In[7]:


search=driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div[2]/div[2]/div/form/div/div[2]/div/button")
search.click()


# In[8]:


job_title=[]
job_location=[]
company_name=[]


# In[22]:


# Scraping Job title from the given page
title_tags=driver.find_elements(By.XPATH,'/html/body/div[1]/div[1]/div[5]/div/div[1]/div[1]/div/div/div[1]/div[1]/div[1]/h2')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)


# In[10]:


# Scraping Job location from the given page
location=driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]')
for i in location[0:10]:
    location=i.text
    job_location.append(location)


# In[11]:


# Scraping Company name from the given page
company_tags=driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_cName__mYnow"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)


# In[23]:


print(len(job_title),len(job_location),len(company_name))


# In[24]:


df=pd.DataFrame({'job_title':job_title,'job_location':job_location,'company_name': company_name})
df


# Q3: In this question you have to scrape data using the filters available on the webpage
#  You have to use the location and salary filter.
# You have to scrape data for “Data Scientist” designation for first 10 job results.
# You have to scrape the job-title, job-location, company name, experience required.
# The location filter to be used is “Delhi/NCR”. The salary filter to be used is “3-6” lakhs
# The task will be done as shown in the below steps:
# 1. first get the web page https://www.shine.com/
# 2. Enter “Data Scientist” in “Skill, Designations, and Companies” field.
# 3. Then click the search button.
# 4. Then apply the location filter and salary filter by checking the respective boxes
# 5. Then scrape the data for the first 10 jobs results you get.
# 6. Finally create a dataframe of the scrapeddata.

# In[25]:


driver=webdriver.Chrome()


# In[27]:


driver.get("https://www.shine.com/")


# In[29]:


designation=driver.find_element(By.CLASS_NAME,"form-control  ")
designation.send_keys('Data Scientist')


# In[30]:


search=driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div[2]/div[2]/div/form/div/div[2]/div/button")
search.click()


# In[32]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[4]/div/div[1]/div/div[2]/div/ul/li[1]/button")
location.click()


# In[33]:


location_search=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[4]/div/div[1]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div/ul/li[1]/input")
location_search.send_keys('Delhi')


# In[34]:


Tick_location=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[4]/div/div[1]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div/ul/li[2]")
Tick_location.click()


# In[35]:


Salary=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[4]/div/div[1]/div/div[2]/div[2]/div/div/div/div[3]/div/ul/li[3]")
Salary.click()


# In[36]:


Tick_salary=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[4]/div/div[1]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div/ul/li[3]/span/label")
Tick_salary.click()


# In[37]:


Show_result=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[4]/div/div[1]/div/div[2]/div[2]/div/div/div/div[4]/button[2]")
Show_result.click()


# In[38]:


job_title=[]
company_name=[]
experience_required=[]


# In[39]:


# Scraping Job title from the given page
title_tags=driver.find_elements(By.XPATH,'//h2[@itemprop="name"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)


# In[40]:


# Scraping Company name from the given page
company_tags=driver.find_elements(By.CLASS_NAME,"jobCard_jobCard_cName__mYnow")
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)


# In[54]:


# Scraping experience required from the given page
experience_tags=driver.find_elements(By.XPATH,"/html/body/div[1]/div[1]/div[5]/div/div[1]/div[1]/div/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
for i in experience_tags:
    exp=i.text
    experience_required.append(exp)


# In[55]:


print(len(job_title),len(company_name),len(experience_required))


# In[56]:


df=pd.DataFrame({'job_title':job_title,'company_name':company_name,'experience_required':experience_required})
df


# In[ ]:




