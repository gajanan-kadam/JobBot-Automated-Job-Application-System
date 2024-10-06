import csv
import time
from get_All_Job_IDS import fetch_job
from isEligibleQ import isEligible
import re
from playwright.sync_api import Playwright, sync_playwright, expect
import os


def run(playwright: Playwright, url) -> None:
    ##Application User Details Starts-->
    nameForApp="" 
    lastNameForApp=""
    resumeNameWithPdf=""
    mobileNo=""
    emailAdd=""
    address=""
    city=""
    pinCode=""
    state=""
    ##<-- Application User Details Ends
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    file_path = os.path.abspath(resumeNameWithPdf)
    page.goto(url=url)
    page.locator("[data-test-id=\"apply-button\"]").click()
    page.locator('input[type="file"]').set_input_files(file_path)
    page.locator("[data-test-id=\"confirm-upload-resume\"]").click()
    page.get_by_test_id("common-text-input-first-name-input").fill(nameForApp)
    page.get_by_test_id("common-text-input-last-name-input").fill(lastNameForApp)
    page.get_by_label("Select country code").press("Tab")
    page.get_by_label("", exact=True).click()
    page.get_by_label("Select country code").fill("+91")
    page.get_by_label("🇮🇳 India (+91)").click()
    page.get_by_test_id("common-text-input-phone-input").dblclick()
    page.get_by_test_id("common-text-input-phone-input").fill(mobileNo)
    page.get_by_test_id("common-text-input-phone-input").press("Tab")
    page.get_by_test_id("common-text-input-postion-apply-input-email").fill(emailAdd)
    page.get_by_test_id("common-text-input-postion-apply-input-email").press("Tab")
    page.locator("[data-test-id=\"\\30 -additional-questions-fieldset\"]").get_by_placeholder("Select").click()
    page.get_by_role("option", name="India", exact=True).click()
    page.get_by_test_id("common-text-input-0-2-additional-questions-text-row").click()
    page.get_by_test_id("common-text-input-0-2-additional-questions-text-row").fill(address)
    page.get_by_test_id("common-text-input-0-3-additional-questions-text-row").click()
    page.get_by_test_id("common-text-input-0-3-additional-questions-text-row").fill(city)
    page.get_by_test_id("common-text-input-0-4-additional-questions-text-row").click()
    page.get_by_test_id("common-text-input-0-4-additional-questions-text-row").fill(pinCode)
    page.locator("[data-test-id=\"\\30 -additional-questions-fieldset\"]").get_by_text("State").click()
    page.get_by_role("option", name=state).click()
    page.locator("[data-test-id=\"\\31 -1-additional-questions-body\"]").click()
    page.locator("[data-test-id=\"\\31 -1-additional-questions-body\"]").fill("NOT APPLICABLE")
    page.locator("[data-test-id=\"\\31 -2-additional-questions-body\"]").click()
    page.locator("[data-test-id=\"\\31 -2-additional-questions-body\"]").fill("NOT APPLICABLE")
    page.locator("[data-test-id=\"\\31 -3-additional-questions-body\"]").click()
    page.locator("[data-test-id=\"\\31 -3-additional-questions-body\"]").fill("NOT APPLICABLE")
    page.locator("[data-test-id=\"\\31 -4-additional-questions-body\"]").click()
    page.locator("[data-test-id=\"\\31 -4-additional-questions-body\"]").fill("NOT APPLICABLE")
    page.locator("[data-test-id=\"\\32 -0-additional-questions-radio-0\"]").click()
    page.get_by_label("Position Location *").click()
    page.get_by_role("option", name="I am applying for a position outside the United States only.").click()
    page.get_by_label("Can you, upon employment, submit verification of your legal right to work in the countries to which you have applied? *", exact=True).click()
    page.get_by_role("option", name="Yes").click()
    page.locator("[data-test-id=\"\\36 -0-additional-questions-checkbox-0\"]").click()
    page.locator("[data-test-id=\"position-apply-button\"]").click()

    # ---------------------
    context.close()
    browser.close()


def load_processed_ids(file_path):
    """Load already processed job IDs from the text file into a set."""
    try:
        with open(file_path, 'r') as file:
            processed_ids = {line.strip() for line in file}
    except FileNotFoundError:
        # If the file doesn't exist, return an empty set
        processed_ids = set()
    return processed_ids

def save_processed_id(file_path, job_id):
    """Append a processed job ID to the text file."""
    with open(file_path, 'a') as file:
        file.write(f"{job_id}\n")

def save_job_to_csv(csv_file, job, applied_status):
    file_exists = False
    try:
        # Check if the file exists
        with open(csv_file, 'r'):
            file_exists = True
    except FileNotFoundError:
        pass

    # Write job details to CSV
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header if the file is newly created
        if not file_exists:
            writer.writerow(["ID", "Name", "URL", "Location", "Applied Status"])
        
        # Write job data
        writer.writerow([job['id'], job['name'], job['url'], job['location'], applied_status])
        
def process_jobs_from_queue(job_queue, file_path, csv_file_path):
    # Load the already processed job IDs from the file
    processed_ids = load_processed_ids(file_path)

    # Process each job in the queue
    while not job_queue.empty():
        job = job_queue.get()
        job_id = str(job['id'])  # Ensure job ID is a string to match the file format
        job_name=job['name']
        # Check if the job ID is already in the processed IDs
        isEligibleFlg=isEligible(job_name)
        if job_id not in processed_ids and isEligibleFlg:
            # If the job ID is not processed, process the job
            url=str(job['url'])
            print("Processing ", url)
            try:
                with sync_playwright() as playwright:
                    run(playwright,url)
                # After processing, save the job ID to the file
                applied_status = "Yes"
                save_processed_id(file_path, job_id)
                save_job_to_csv(csv_file_path, job, applied_status)
                time.sleep(2)
            except Exception as e:
                # Handle any errors during processing
                print(f"Failed to process job ID {job_id}: {e}")
                applied_status = "No"
                save_job_to_csv(csv_file_path, job, applied_status)
                
        else:
            if not isEligibleFlg:
                applied_status = "Not Eligible"
                save_job_to_csv(csv_file_path, job, applied_status)
                print("Senior/Lead/Devops/MTS2 Requirement")
            print(f"Job ID {job_id} already processed, skipping...")
        




if __name__ == "__main__":
    # Assume job_queue is already populated with job data
    #job_queue = fetch_job(10)
    # Define the file path to store processed job IDs
    file_path = "processed_job_ids.txt"
    csv_file_path = "APPLIED_STATUS.csv"
    # Process jobs and check against the file
    startIndex=10
    while True:

        try:
            print(startIndex)
            job_queue = fetch_job(startIndex)
            if job_queue.empty():
                print("ALL OPEN POSITION APLLIED")
                break
            process_jobs_from_queue(job_queue, file_path,csv_file_path)
            startIndex=startIndex+10
        
        except Exception as e:
            print("Technical Error!!!!")
            break

    



