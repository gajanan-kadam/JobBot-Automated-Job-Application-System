# JobBot-Automated-Job-Application-System
A Python-based automated system for applying to job listings using web scraping and eligibility parsing.
# Automated Job Application System Using Web Scraping and Eligibility Parsing

## Project Description
Developed a Python-based automated system that scrapes job listings, parses job descriptions, checks eligibility based on predefined criteria, and applies for open positions without user intervention. The system logs application status (applied/not applied) and reasons for ineligibility in both CSV and text file formats for tracking purposes.

## Key Features
- **Web Scraping**: Automated extraction of job listings, job IDs, and job descriptions from career websites using libraries like BeautifulSoup and Selenium.
- **Eligibility Parsing**: Custom logic to parse job descriptions and match them against predefined eligibility criteria (e.g., skills, years of experience).
- **Automated Job Application**: Automatically applies for jobs that match eligibility criteria.
- **Data Logging**: Tracks and logs all applications, including applied and not-applied jobs, with reasons for ineligibility, in CSV and text formats for easy analysis.
- **File Handling**: Systematically organizes applied job data for future reference and auditing.

## Skills Used
- Python (Web Scraping, Automation)
- Selenium, BeautifulSoup
- File Handling (CSV, TXT)
- Regular Expressions (Regex) for parsing eligibility
- Data Logging and Organization

## Impact
- Reduced manual effort in job applications by automating the process.
- Improved efficiency by ensuring only eligible jobs are applied to.
- Enhanced ability to track and audit job applications.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/automated-job-application-system.git
   cd automated-job-application-system
2. ```bash
   pip install -r requirements.txt
3. ```bash
   python main.py


