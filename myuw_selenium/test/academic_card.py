# User academic card data

from myuw_selenium.test.myuw import link

academic_card_values = {
    'javerage' : {
        'class' : 'SENIOR',
        'major' : 'App & Comp Math Sci (Social & Behav Sci)',
        'minor' : 'American Sign Language',
        'links' : [
            link("MyPlan", 'https://myplan.uw.edu/'),
            link("Degree Audit Reporting System (DARS)", "https://uwstudent.washington.edu/student/myplan/audit?methodToCall=audit&viewId=DegreeAudit-FormView")
        ]
    },
    'eight' : {
        'class' : 'SENIOR',
        'major' : 'Economics\nMathematics',
        'minor' : None,
        'links' : None
    },
    'jbothell' : {
        'class' : 'SOPHMORE',
        'major' : 'Premajor (Bothell Campus)',
        'minor' : None,
        'links' : None

    },
}
