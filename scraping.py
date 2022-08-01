import requests
from bs4 import BeautifulSoup
website_url = "https://infopark.in/companies/jobs"
keywords = ["data analyst"]
output_file = open("jobs.txt","w")
res = requests.get(website_url)
soup = BeautifulSoup(res.text,'lxml')
jobs = soup.find_all("div",{"class":"row company-list joblist"})
for job in jobs:
    title_element = job.find("a")
    title = title_element.text
    link = title_element["href"]
    company_name = job.find("div",{"class":"jobs-comp-name"}).text
    last_date = job.find("div",{"class":"job-date"}).text
    if any( word.lower() in title.lower() for word in keywords):
        # print(title,company_name,last_date)
        output_file.write("Job Title: " + title + " " + "\nCompany Name: " + company_name + " " + "\nLast Date to apply: " + last_date +"\nLINK:" +link + "\n\n\n")