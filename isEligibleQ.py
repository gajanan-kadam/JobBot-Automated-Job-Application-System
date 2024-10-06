def isEligible(job_name):

    keywords = [item for part in job_name.split(',') for item in part.split()]
    avoidKeywords=["Senior","Lead","Manager","Devops","MTS 2","Senior,","Lead,","Manager,",
                   "Devops,","MTS 2,","Principal","Principal,","Data Analyst 2","Data Analyst 2,","2",
                   "Sr","Design","Architect","design"]
    


    for keyword in avoidKeywords:
        if keyword in keywords:
            return False
    return True