import courseClass as c
import pickle as p
fileName = 'courseSave.p'
courses = []

def loading():
    '''load the courses from a file'''

    with open(fileName,'rb') as data:
        loading = p.load(data)
        for x in loading:
            courses.append(x)


def display(givenCourse):
    '''fancy way of showing the course'''
    print("""
==================================================
==================================================
Name of course: {0}
Type of qualification: {1}
Exam board: {2}
--------------------------------------------------
--------------------------------------------------
Description:
{3}
--------------------------------------------------
--------------------------------------------------
Why study this at S6C?
{4}
--------------------------------------------------
Entry requirements:
{5}
--------------------------------------------------
Course structure:
{6}
--------------------------------------------------
Trips and visits:
{7}
--------------------------------------------------
Progression oportunities:
{8}
--------------------------------------------------
What our students think:
{9}
--------------------------------------------------
==================================================
==================================================
""".format(givenCourse.name, givenCourse.type_, givenCourse.examBoard, givenCourse.description, givenCourse.whyStudyS6C, givenCourse.entry givenCourse.structure, givenCourse.trips, givenCourse.progression, givenCourse.students)


def showAll():
    for x in courses:
        display(x)
