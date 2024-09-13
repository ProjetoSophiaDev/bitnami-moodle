# Faker is a Python package that generates fake data for you.
from faker import Faker
fake = Faker()
# fake = Faker('pt_BR')

import csv
import random

# https://docs.moodle.org/404/en/Upload_users
# field names 
# username;firstname;lastname;email;password
# Optional user fields
# institution,department,city,country,lang,auth,timezone,idnumber,icq,phone1,phone2,address,url,description,mailformat,maildisplay,maildigest,htmleditor,autosubscribe,interests,theme
fields = ['username', 'firstname', 'lastname', 'email','password','cohort1','idnumber'] 
        
# name of csv file 
filename = "tsaimport.csv"
# groups = ["Student", "Teacher", "Admin"]
gcohort = ["Students", "Teachers", "Admins"]
groups = ["s","t","a"] 
nusersgroup= [10,5,1] # number os users per group
gpass = [fake.password(),fake.password(),fake.password()] # Same password per group
gmail = ["student.test", "teacher.test", "admin.test"]

Faker.seed(0)
# writing to csv file 
with open(filename, 'w',newline='\n') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile,delimiter=',') 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    for n in range(len(groups)):
        nusers=nusersgroup[n] # Number of users in group
        gname=groups[n] # Group name
        for u in range(nusers):
            sname=gname+str(u+1) # User short name
            fname=sname+'fn'
            lname=sname+'ln'
            nome=fname+" "+lname
            username=sname
            email=username+"@"+gmail[n]
            csvwriter.writerows([[username,fname,lname,email,gpass[n],gcohort[n],fake.msisdn()]])
            # ['username', 'firstname', 'lastname', 'email','password','cohort1','idnumber'] 
            