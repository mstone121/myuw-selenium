#!/usr/bin/python

from myuw_selenium.test.myuw import link

# Dictionary of resource links. 
resLinks = {
    'seattle': {
        'academics' : {
            'Registration' : [
                link('Academic Calendar', 'http://www.washington.edu/students/reg/calendar.html'),
                link('Course Catalog', 'http://www.washington.edu/students/crscat/'),
                link('Degree Audit Reporting System (DARS)', 'https://sdb.admin.washington.edu/students/uwnetid/dars.asp'),
                link('MyPlan', 'https://uwstudent.washington.edu/student/myplan'),
                link('Registration', 'https://sdb.admin.washington.edu/students/uwnetid/register.asp'),
                link('Schedule Finder', 'https://sdb.admin.washington.edu/timeschd/uwnetid/findschd.asp'),
                link('UW Seattle Time Schedule', 'http://www.washington.edu/students/timeschd/')
            ], 
            'Advising & Tutoring' : [
                link('Career Center', 'http://careers.washington.edu/'),
                link('Center for Learning and Undergraduate Enrichment (CLUE)', 'http://depts.washington.edu/aspuw/clue/home/'),
                link('International Student Services (ISS)', 'http://iss.washington.edu/'),
                link('Odegaard Writing & Research Center', 'http://depts.washington.edu/owrc'),
                link('Undergraduate Academic Advising (Pre-major)', 'http://www.washington.edu/uaa/advising/'),
                link('Study Abroad', 'http://studyabroad.washington.edu/'),
            ],
            'Grades & Transcripts' : [
                link('GPA Calculator', 'http://www.washington.edu/uaa/advising/general-education-requirements/gpa-calculator/'),
                link('Grade Report', 'https://sdb.admin.washington.edu/students/uwnetid/grades.asp'),
                link('Order Official Transcripts', 'https://sdb.admin.washington.edu/students/uwnetid/official.asp'),
                link('Unofficial Transcript', 'https://sdb.admin.washington.edu/students/uwnetid/unofficial.asp')
            ],
            'Libraries' : [
                link('Electronic Course Reserves', 'https://eres.lib.washington.edu/'),
                link('UW Libraries', 'http://lib.washington.edu/')
            ],
            'Graduation' : [
                link('Application for Graduation', 'http://www.washington.edu/students/reg/grad.html')
            ]
        },
        'finances' : {
            'Financial Aid' : [
                link('Financial Aid and Scholarships', 'http://www.washington.edu/students/osfa/'),
                link('Financial Aid Status', 'https://sdb.admin.washington.edu/students/uwnetid/finaidstatus.asp')
            ],
            'Taxes' : [
                link('Form 1098-T', 'https://sdb.admin.washington.edu/sisStudents/uwnetid/irs1098tconsent.aspx'),
                link('Student Tax Information', 'http://f2.washington.edu/fm/sfs/tax')
            ],
            'Tuition' : [
                link('Tuition Overview', 'http://f2.washington.edu/fm/sfs/tuition')
            ]
        },
        'studentcampuslife' : {
            'Housing & Dining' : [
                link('Add Funds to Husky Card', 'https://www.hfs.washington.edu/olco/Secure/AccountSummary.aspx'),
                link('Campus Dining', 'https://www.hfs.washington.edu/dining/'),
                link('Check HFS Balance', 'https://www.hfs.washington.edu/myhfs/ledger.aspx'),
                link('Student Housing', 'https://www.hfs.washington.edu/housing/')
            ],
            'Health & Wellness' : [
                link('Counseling Center', 'http://www.washington.edu/counseling/'),
                link('Hall Health Center', 'http://depts.washington.edu/hhpccweb/'),
                link('Recreational Sports Programs (IMA)', 'http://depts.washington.edu/ima/'),
                link('Student Health Insurance', 'http://www.washington.edu/ship/')
            ],
            'Support Services' : [
                link('Disability Resources', 'http://www.washington.edu/admin/dso/uw-resources.html'),
                link('Diversity Resources', 'http://www.washington.edu/omad/'),
                link('New Student Orientation', 'http://fyp.washington.edu/getting-started-at-the-university-of-washington/'),
                link('Q Center', 'http://depts.washington.edu/qcenter/wordpress/'),
                link("Women's Center", 'http://depts.washington.edu/womenctr/'),
                link('SafeCampus', 'http://www.washington.edu/safecampus/'),
                link('Sexual Assault & Relationship Violence Information Service (SARIS)', 'http://www.washington.edu/students/saris/'),
                link('Student Legal Services', 'http://depts.washington.edu/slsuw/')  
            ],
            'Campus Retail' : [
                link('HUB', 'http://hub.washington.edu/'),
                link('University Book Store', 'http://www.bookstore.washington.edu/student_faculty/student_faculty.taf?verba=uwseattle')
            ],
            'Transportation' : [
                link('Accessibility Guide', 'http://www.washington.edu/admin/ada/newada.php'),
                link('Campus Map', 'http://www.washington.edu/maps/'),
                link('Getting to Seattle Campus', 'http://www.washington.edu/facilities/transportation/commuterservices/')
            ],
            'Rules & Regulations' : [
                link('Family Educational Rights and Privacy Act (FERPA) - Privacy of Student Information', 'http://www.washington.edu/students/reg/ferpa.html'),
                link('Office of Scholarly Integrity (OSI)', 'https://ap.washington.edu/osi/'),
                link('Student Conduct Code', 'http://www.washington.edu/cssc/student-conduct-overview/student-code-of-conduct/')
            ],
        },
        'eventsactivities' : {
            'Events' : [
                link('Campus Event Calendar', 'http://www.washington.edu/calendar/'),
                link('HUB Events', 'http://depts.washington.edu/thehub/hub-events/today-in-the-hub/')
            ],
            'Student Clubs & Organizations' : [
                link('Registered Student Organizations (RSO) Directory', 'https://uws-community.symplicity.com/index.php?s=student_group')
            ],
            'Stay Connected' : [
                link('Campus News', 'http://www.washington.edu/news/'),
                link('UW Facebook Page', 'http://www.facebook.com/UofWA'),
                link('UW YouTube Channel', 'http://www.youtube.com/user/uwhuskies'),
                link('UW Instagram', 'http://instagram.com/uofwa'),
                link('UW Twitter', 'http://twitter.com/UW'),
                link('UW LinkedIn', 'http://www.linkedin.com/company/university-of-washington'),
            ]
        },
        'toolssoftware' : {
            'Teaching & Learning Tools' : [
                link('Canvas LMS', 'http://canvas.uw.edu/'),
                link('Catalyst Web Tools', 'https://catalyst.uw.edu/'),
                link('Notify.UW', 'https://notify.uw.edu/'),
                link('Panopto', 'https://panopto.uw.edu/'),
                link('SpaceScout Study Space Finder', 'http://spacescout.uw.edu/seattle'),
                link('Tableau Data Analysis Software', 'http://www.washington.edu/itconnect/wares/uware/tableau-software/'),
                link('Tegrity', 'https://uw.tegrity.com/'),
            ], 
            'Email & UW NetID' : [
                link('Alpine Mail', 'http://alpine.washington.edu/'),
                link('Email Forwarding', 'https://uwnetid.washington.edu/manage/?forward'),
                link('Gmail', 'https://mail.google.com/a/uw.edu'),
                link('Manage UW NetID Account', 'https://uwnetid.washington.edu/manage/')
            ],
            'Directory' : [
                link('UW Directory', 'http://www.washington.edu/home/directories.html')
            ]
        },
        'employment' : {
            '' : [
                link('Career Center', 'http://careers.washington.edu/'),
                link('Employee Self-Service (ESS)', 'https://www.washington.edu/ess/'),
                link('Husky Jobs', 'https://washington-csm.symplicity.com/students/index.php'),
                link('Student Employment in the Libraries', 'http://www.lib.washington.edu/about/employment/students')
            ]
        }
    },
    'bothell' : {
        'academics' : {
            'Registration' : [
                link('Bothell Academic Calendar', 'http://www.uwb.edu/calendars'),
                link('Course Catalog', 'http://www.washington.edu/students/crscatb/'),
                link('Degree Audit Reporting System (DARS)', 'https://sdb.admin.washington.edu/students/uwnetid/dars.asp'),
                link('MyPlan', 'https://uwstudent.washington.edu/student/myplan'),
                link('Registration', 'https://sdb.admin.washington.edu/students/uwnetid/register.asp'),
                link('Schedule Finder', 'https://sdb.admin.washington.edu/timeschd/uwnetid/findschd.asp'),
                link('UW Bothell Time Schedule', 'http://www.uwb.edu/registration/time')
            ], 
            'Advising & Tutoring' : [
                link('Career Services', 'http://www.bothell.washington.edu/careers'),
                link('International Student Services (ISS)', 'http://www.uwb.edu/iss'),
                link('Study Abroad', 'http://www.uwb.edu/globalinitiatives/abroad'),
                link('Undergraduate Academic Advising (Pre-major)', 'http://www.uwb.edu/cusp/advising'),
                link('Writing and Communication Center (WaCC)', 'http://www.uwb.edu/wacc'),
            ],
            'Grades & Transcripts' : [
                link('Bothell Faculty and Staff Directory', 'http://www.uwb.edu/directory'),
                link('GPA Calculator', 'http://www.washington.edu/uaa/advising/general-education-requirements/gpa-calculator/'),
                link('Grade Report', 'https://sdb.admin.washington.edu/students/uwnetid/grades.asp'),
                link('Unofficial Transcript', 'https://sdb.admin.washington.edu/students/uwnetid/unofficial.asp')
            ],
            'Libraries' : [
                link('Electronic Course Reserves', 'https://eres.bothell.washington.edu/'),
                link('UW Bothell Library', 'http://library.uwb.edu/')
            ],
            'Graduation' : [
                link('Applying for Graduation', 'https://www.uwb.edu/registration/graduation/apply')
            ],                    
        },
        'finances' : {
            'Financial Aid' : [
                link('Financial Aid and Scholarships', 'http://www.bothell.washington.edu/financialaid'),
                link('Financial Aid Status', 'https://sdb.admin.washington.edu/students/uwnetid/finaidstatus.asp')
            ],
            'Taxes' : [
                link('Form 1098-T', 'https://sdb.admin.washington.edu/sisStudents/uwnetid/irs1098tconsent.aspx'),
                link('Student Tax Information', 'http://f2.washington.edu/fm/sfs/tax')
            ],
            'Tuition' : [
                link('Tuition Overview', 'http://f2.washington.edu/fm/sfs/tuition')
            ]
        },
        'studentcampuslife' : {
            'Housing & Dining' : [
                link('Add Funds to Husky Card', 'https://www.hfs.washington.edu/olco/Secure/AccountSummary.aspx'),
                link('Campus Dining', 'http://www.uwb.edu/food'),
                link('Check HFS Balance', 'https://www.hfs.washington.edu/myhfs/ledger.aspx'),
                link('Student Housing', 'http://www.uwb.edu/housing')
            ],
            'Health & Wellness' : [
                link('Counseling Services', 'http://www.uwb.edu/studentservices/counseling'),
                link('Student Health Resource', 'http://www.uwb.edu/studentservices/health-matters'),
                link('Recreation and Wellness', 'http://www.uwb.edu/studentlife/rec-wellness'),
                link('Student Health Insurance', 'http://www.uwb.edu/studentservices/insurance')
            ],
            'Support Services' : [
                link('Disability Resources for Students (DRS)', 'http://www.bothell.washington.edu/studentservices/drs'),
                link('Diversity Resources', 'http://www.uwb.edu/diversity'),
                link('Orientation & Transition Programs', 'http://www.bothell.washington.edu/orientation'),
                link('Q Center', 'http://depts.washington.edu/qcenter/wordpress/'),
                link("Women's Center", 'http://depts.washington.edu/womenctr/'),
                link('SafeCampus', 'http://www.washington.edu/safecampus/uwb/'),
                link('Security & Campus Safety: Sexual Assualts', 'http://www.uwb.edu/getattachment/admin/procedures/sexualassaultspolicy.pdf'),
            ],
            'Campus Retail' : [
                link('Student Success Center', 'http://www.uwb.edu/studentservices/ssc'),
                link('University Book Store', 'http://www.bookstore.washington.edu/student_faculty/student_faculty.taf?verba=uwbothell')
            ],
            'Transportation' : [
                link('Mobility Map', 'http://www.uwb.edu/getattachment/admin/emergency/mobility.pdf'),
                link('Campus Map', 'http://www.uwb.edu/visitors/uw-bothell-map.pdf'),
                link('Getting to Bothell Campus', 'https://www.uwb.edu/admin/transportation')
            ],
            'Rules & Regulations' : [
                link('Family Educational Rights and Privacy Act (FERPA) - Privacy of Student Information', 'http://www.washington.edu/students/reg/ferpa.html'),
                link('Student Guide to Academic Integrity', 'http://www.uwb.edu/academic/policies/academicconduct/student-guide'),
                link('Student Conduct and Responsibility', 'http://www.uwb.edu/studentservices/studentconduct')
            ],
        },
        'eventsactivities' : {
            'Events' : [
                link('Campus Event Calendar', 'https://www.uwb.edu/calendar'),
                link('Student Life Event Calendar', 'http://www.uwb.edu/studentlife/events')
            ],
            'Student Clubs & Organizations' : [
                link('Club Directory', 'http://www.bothell.washington.edu/studentlife/clubs/directory')
            ],
            'Stay Connected' : [
                link('Campus News', 'http://www.uwb.edu/news'),
                link('UW Bothell Facebook Page', 'http://www.facebook.com/uwbothell'),
                link('UW Bothell YouTube Channel', 'http://www.youtube.com/user/uwbothell'),
                link('UW Bothell Instagram', 'http://instagram.com/UW_BOTHELL'),
                link('UW Bothell Twitter', 'http://twitter.com/UWBothell'),
                link('UW Bothell LinkedIn', 'https://www.linkedin.com/groups/University-Washington-Bothell-92858?home=&gid=92858')
            ]
        },
        'toolssoftware' : {
            'Teaching & Learning Tools' : [
                link('Canvas LMS', 'http://canvas.uw.edu/'),
                link('Catalyst Web Tools', 'https://catalyst.uw.edu/'),
                link('Notify.UW', 'https://notify.uw.edu/'),
                link('Tableau Data Analysis Software', 'http://www.washington.edu/itconnect/wares/uware/tableau-software/'),
                link('Tegrity', 'https://uw.tegrity.com/'),
                link('Panopto', 'https://panopto.uw.edu/')
            ],                     
            'Email & UW NetID' : [
                link('Gmail', 'https://mail.google.com/a/uw.edu'),
                link('Alpine Mail', 'http://alpine.washington.edu/'),
                link('Email Forwarding', 'https://uwnetid.washington.edu/manage/?forward'),
                link('Manage UW NetID Account', 'https://uwnetid.washington.edu/manage/')
            ],                    
            'Directory' : [
                link('Bothell Faculty and Staff Directory', 'http://www.uwb.edu/directory')
            ]
        },
        'employment' : {
            '' : [
                link('Career Services', 'http://www.bothell.washington.edu/careers'),
                link('Employee Self-Service (ESS)', 'https://www.washington.edu/ess/'),
                link('Husky Jobs', 'https://washington-csm.symplicity.com/students/index.php'),
                link('Student Employment in the Libraries', 'http://www.lib.washington.edu/about/employment/students')
            ]
        }
    },
    'tacoma' : {
        'academics' : {
            'Registration' : [
                link('Academic Calendar', 'http://www.washington.edu/students/reg/calendar.html'),
                link('Course Catalog', 'http://www.washington.edu/students/crscatt/'),
                link('Degree Audit Reporting System (DARS)', 'https://sdb.admin.washington.edu/students/uwnetid/dars.asp'),
                link('MyPlan', 'https://uwstudent.washington.edu/student/myplan'),
                link('Registration', 'https://sdb.admin.washington.edu/students/uwnetid/register.asp'),
                link('Schedule Finder', 'http://www.tacoma.washington.edu/enrollment_apps/timeschedule/search.cfm'),
                link('UW Tacoma Time Schedule', 'http://www.tacoma.uw.edu/uwt/enrollment-services/time-schedule-registration-guide')
            ],
            'Advising & Tutoring' : [
                link('Career Development', 'http://www.tacoma.washington.edu/studentaffairs/SS/cde_about.cfm'),
                link('Teaching and Learning Center', 'http://www.tacoma.uw.edu/teaching-learning-center/teaching-learning-center'),
                link('International Student Services (ISS)', 'http://www.tacoma.uw.edu/uwt/taxonomy/term/252'),
                link('Academic Writing Resources', 'http://www.tacoma.uw.edu/teaching-and-learning-center/writing-resources-0'),
                link('Undergraduate Academic Advising (Pre-major)', 'http://www.tacoma.uw.edu/advising'),
                link('Study Abroad', 'http://www.tacoma.uw.edu/international-programs/international-programs')
            ],
            'Grades & Transcripts' : [
                link('GPA Calculator', 'http://www.washington.edu/uaa/advising/general-education-requirements/gpa-calculator/'),
                link('Grade Report', 'https://sdb.admin.washington.edu/students/uwnetid/grades.asp'),
                link('Order Official Transcripts', 'https://sdb.admin.washington.edu/students/uwnetid/official.asp'),
                link('Unofficial Transcript', 'https://sdb.admin.washington.edu/students/uwnetid/unofficial.asp')
            ],
            'Libraries' : [
                link('Electronic Course Reserves', 'https://ereserves.tacoma.washington.edu/'),
                link('UW Tacoma Library', 'http://www.tacoma.uw.edu/library')
            ],
            'Graduation' : [
                link('Applying to Graduate', 'http://www.tacoma.uw.edu/uwt/enrollment-services/applying-graduate')
            ]
        },
        'finances' : {
            'Financial Aid' : [
                link('Financial Aid and Scholarships', 'http://www.tacoma.uw.edu/uwt/financial-aid'),
                link('Financial Aid Status', 'https://sdb.admin.washington.edu/students/uwnetid/finaidstatus.asp')
            ],
            'Taxes' : [
                link('Form 1098-T', 'https://sdb.admin.washington.edu/sisStudents/uwnetid/irs1098tconsent.aspx'),
                link('Student Tax Information', 'http://f2.washington.edu/fm/sfs/tax')
            ],
            'Tuition' : [
                link('Tuition Overview', 'http://f2.washington.edu/fm/sfs/tuition')
            ]
        },
        'studentcampuslife' : {
            'Housing & Dining' : [
                link('Add Funds to Husky Card', 'https://www.hfs.washington.edu/olco/Secure/AccountSummary.aspx'),
                link('Campus Dining', 'http://www.tacoma.uw.edu/uwt/convenience-store/welcome-0'),
                link('Check HFS Balance', 'https://www.hfs.washington.edu/myhfs/ledger.aspx'),
                link('Housing', 'http://www.tacoma.uw.edu/housing')
            ],
            'Health & Wellness' : [
                link('Student Counseling Center', 'http://www.tacoma.washington.edu/studentaffairs/SHW/scc_about.cfm'),
                link('Student Health Services (SHS)', 'http://www.tacoma.washington.edu/studentaffairs/SHW/shs_healthservices_about.cfm'),
                link('Recreation & Fitness', 'http://www.tacoma.washington.edu/studentaffairs/SI/rec_fit_about.cfm'),
                link('Student Health Insurance', 'http://www.tacoma.uw.edu/ses/health/insurance')
            ],
            'Support Services' : [
                link('Disability Support Services (DSS)', 'http://www.tacoma.washington.edu/studentaffairs/SHW/dss_about.cfm'),
                link('Diversity Resources', 'http://www.tacoma.uw.edu/diversity'),
                link('New Student Orientation', 'http://www.tacoma.washington.edu/studentaffairs/SS/nsp_nso.cfm'),
                link('Q Center', 'http://depts.washington.edu/qcenter/wordpress/'),
                link("Women's Center", 'http://depts.washington.edu/womenctr/'),
                link('SafeCampus', 'http://www.washington.edu/safecampus/uwt/'),
                link('Campus Safety & Security', 'http://www.tacoma.uw.edu/uwt/administrative-services/campus-safety')
            ],
            'Campus Retail' : [
                link('Dawg House Student Lounge', 'http://www.tacoma.washington.edu/studentaffairs/SI/rec_fit_lounge.cfm'),
                link('University Book Store', 'http://www.bookstore.washington.edu/student_faculty/student_faculty.taf?verba=uwtacoma')
            ],
            'Transportation' : [
                link('Accessibility Guide', 'http://www.tacoma.washington.edu/studentaffairs/SHW/dss_access.cfm'),
                link('Campus Map', 'http://www.tacoma.uw.edu/campus-map/campus-map'),
                link('Getting to Tacoma Campus', 'http://www.tacoma.uw.edu/getting-campus/getting-campus')
            ],
            'Rules & Regulations' : [
                link('Family Educational Rights and Privacy Act (FERPA) - Privacy of Student Information', 'http://www.washington.edu/students/reg/ferpa.html'),
                link('Student Conduct', 'http://www.tacoma.washington.edu/studentaffairs/SI/conduct_about.cfm')
            ]
        },
        'toolssoftware' : {
            'Teaching & Learning Tools' : [
                link('Canvas LMS', 'http://canvas.uw.edu/'),
                link('Catalyst Web Tools', 'https://catalyst.uw.edu/'),
                link('Notify.UW', 'https://notify.uw.edu/'),
                link('SpaceScout Study Space Finder', 'http://spacescout.uw.edu/tacoma'),
                link('Tableau Data Analysis Software', 'http://www.washington.edu/itconnect/wares/uware/tableau-software/'),
                link('Tegrity', 'https://uw.tegrity.com/'),
                link('Panopto', 'https://panopto.uw.edu/')
            ],
            'Email & UW NetID' : [
                link('Gmail', 'https://mail.google.com/a/uw.edu'),
                link('Alpine Mail', 'http://alpine.washington.edu/'),
                link('Email Forwarding', 'https://uwnetid.washington.edu/manage/?forward'),
                link('Manage UW NetID Account', 'https://uwnetid.washington.edu/manage/')
            ],
            'Directory' : [
                link('UW Directory', 'http://www.washington.edu/home/directories.html')
            ]
        },
        'eventsactivities' : {
            'Events' : [
                link('Campus Event Calendar', 'http://www.tacoma.uw.edu/calendar/calendar')
            ],
            'Student Clubs & Organizations' : [
                link('UW Tacoma Clubs & Organizations', 'https://dawgden.tacoma.uw.edu/Organizations')
            ],
            'Stay Connected' : [
                link('Campus News', 'http://www.tacoma.uw.edu/news/news-information'),
                link('UW Tacoma Facebook Page', 'http://www.facebook.com/uwtacoma'),
                link('UW Tacoma YouTube Channel', 'http://www.youtube.com/user/uwTacomaAdvancement')
            ]
        },
        'employment' : {
            '' : [
                link('Career Development', 'http://www.tacoma.washington.edu/studentaffairs/ss/cde_about.cfm'),
                link('Employee Self-Service (ESS)', 'https://www.washington.edu/ess/'),
                link('Husky Jobs', 'https://washington-csm.symplicity.com/students/index.php'),
                link('Student Employment in the Libraries', 'http://www.lib.washington.edu/about/employment/students')
            ]
        }
    }
}


# Everything should be sorted alphabetically in subcategories
for campus in resLinks.values():
    for page in campus.values():
        for subcat in page.values():
            subcat.sort()

# While testing the tests, remove known failures as we go
#resLinks['seattle'].pop('studentcampuslife')
