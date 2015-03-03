# User data for grade_card

from myuw_selenium.test.myuw import link

grade_card_values = {
    'javerage' : {
        'courses' : {
            'PHYS 121 A' : '4.0',
            'PHYS 121 AC': '4.0',
            'PHYS 121 AQ': '3.5',
            'TRAIN 100 A': 'P',
            'TRAIN 101 A': 'HP'
        },
        'links' : [
            link("Grade Report", 'https://sdb.admin.washington.edu/students/uwnetid/grades.asp'),
            link("Degree Audit Reporting System (DARS)", "https://uwstudent.washington.edu/student/myplan/audit?methodToCall=audit&viewId=DegreeAudit-FormView"),
            link("Unofficial Transcript", "https://sdb.admin.washington.edu/students/uwnetid/unofficial.asp")
        ]
    },
    'eight' : {
        'courses' : {
            'ARCTIC 200 A': 'W',
            'ASL 101 A'   : 'X',
            'PHYS 121 A'  : 'No grade',
            'PHYS 121 AC' : 'No grade',
            'PHYS 121 AQ' : 'No grade',
            'ROLING 310 A': 'No grade',
            'TRAIN 100 A' : 'No grade',
            'TRAIN 101 A' : 'No grade'
        },
        'links' : None
    },
    'none' : None,
}
