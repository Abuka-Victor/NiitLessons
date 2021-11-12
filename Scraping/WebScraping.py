from bs4 import BeautifulSoup
import requests

url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation="
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, "lxml")
job_lists = soup.findAll('li', class_="clearfix job-bx wht-shd-bx")
for job in job_lists:
    job_role = job.find('a').text
    print(job_role)
    company_name = job.find('h3', class_='joblist-comp-name').text
    print(company_name)
    job_desc = job.find('ul', class_="list-job-dtl clearfix").find('li').text
    print(job_desc)
    apply_link = job.find('a', class_="waves-effect waves-light btn").get('href')
    print(apply_link)



