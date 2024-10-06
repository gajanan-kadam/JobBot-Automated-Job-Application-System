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
   git clone https://github.com/gajanan-kadam/JobBot-Automated-Job-Application-System.git
   cd JobBot-Automated-Job-Application-System
2. ```bash
   pip install -r requirements.txt
3. ```bash
   python main.py

### Step 4: Create Diagrams and Flowcharts

1. **Flowchart**: 

   - **Start**
   - **Fetch Job Listings**
   - **For Each Job**:
     - **Parse Job Description**
     - **Check Eligibility**
       - **If Eligible**: Apply for Job
       - **Log Application Status**
     - **If Not Eligible**: Log Reason
   - **End**
     ![image](https://github.com/user-attachments/assets/ba30c899-8a48-4fa4-be27-5e58ef544c0c)


2. **Architecture Diagram**: This diagram should show the system architecture, including components like:
   - Web Scraping Module
   - Eligibility Parsing Module
   - Application Logging Module
   - File Handling

### Step 5: Add Your Code

- **main.py**: Write your main script where the web scraping, eligibility checking, and application logic reside.
- **requirements.txt**: List the Python libraries your project depends on. For example:
    ```
    beautifulsoup4
    requests
    selenium
    pandas
    ```

### Step 6: Commit and Push Your Changes

1. **Add Files to Your Repository**:
   ```bash
   git add .


