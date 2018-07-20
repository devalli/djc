#!/usr/bin/python3
# -*- coding: utf8 -*-

import re
import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":

	url = "https://www.stepstone.de/5/ergebnisliste.html?ws=Karlsruhe&of=100&suid=7633a95c%2Db3bf%2D48ad%2Da66b%2D9414e513cf6d&an=paging%5Fnext"		
	r = requests.get(url)
	soup = BeautifulSoup(r.content, "html.parser")
	job_rows = soup.find_all("div", class_="job-element-row")
	job_titles = []
	job_urls = []
	job_company = []
	for job_row in job_rows:
		job_titles.append(job_row.find("h2", class_="job-element__body__title").get_text().strip())
		job_urls.append(job_row.find("a", class_="job-element__url")['href'].strip())
		job_company.append(job_row.find("div", class_="job-element__body__company").get_text().strip())
	for i in range(len(job_titles)):
		info = '{}\n	{}\n	{}\n'.format(job_company[i],job_titles[i],job_urls[i])
		print(info)
		
		
		
