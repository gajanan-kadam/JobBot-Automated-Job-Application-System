import requests
import queue

def fetch_job(startSeries):
    url = (
    f"https://careers.qualcomm.com/api/apply/v2/jobs?domain=qualcomm.com&start={startSeries}&num=10"
    )

    querystring = {
        "domain": ["qualcomm.com", "qualcomm.com"],
        "profile": "",
        "location": "india",
        "skill": [
            "Python",
            "Debugging",
            "Linux",
            "C++",
            "Algorithms",
            "Coding",
            "Git",
            "Engineering",
            "Scripting",
            "Software Engineering",
            "Jira",
            "Programming",
            "C",
            "Software Development",
            "Testing",
            "Problem Solving",
            "Docker",
            "Jenkins",
            "SQL",
            "Deployments",
            "API",
        ],
        "seniority": ["Entry"],#, "Mid/Senior"],
        "sort_by": "relevance",
        "triggerGoButton": ["false", "true"],
    }
    response = requests.request(
        "GET", url, params=querystring
    )

    data = response.json()

    # Extract the 'id' from the 'positions' list
    job_queue=queue.Queue()
    for position in data.get("positions", []):
        #print(position["id"])
        job_id=position["id"]
        job_name = position['name']
        job_url = position['canonicalPositionUrl']
        job_location = position['location']
        job_queue.put({'id': job_id, 'name': job_name, 'url': job_url, 'location':job_location})

    return job_queue


