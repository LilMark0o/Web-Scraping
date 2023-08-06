import mysql.connector
from DataStructures import Job
import config

db = mysql.connector.connect(
    host=config.host,
    user=config.user,
    passwd=config.passwd,
    database=config.database
)
myCursor = db.cursor()


def createDB():
    myCursor.execute("CREATE DATABASE JobsDB")


def createTables():
    str = "CREATE TABLE Jobs (link VARCHAR(254) PRIMARY KEY, profession VARCHAR(40) NOT NULL,salary int UNSIGNED NOT NULL, place VARCHAR(25), modality VARCHAR(25));"
    myCursor.execute(str)

# createDB()
# createTables()


def checkDataGeneral():
    myCursor.execute("Select * from Jobs;")
    for x in myCursor:
        print(x)


def insertData(Job: Job):
    try:
        myCursor.execute(
            "INSERT INTO Jobs (link, profession, salary, place, modality) VALUES " +
            "(%s,%s,%s,%s,%s);", (Job.link, Job.profession,
                                  Job.salary, Job.place, Job.modality)
        )
        db.commit()
    except:
        pass


def deleteData(Job: Job):
    myCursor.execute("DELETE FROM Jobs WHERE link= %s;", (Job.link,))


def avergPerJob():
    # query = "SELECT profession, modality, avg( salary ) as avg_salary FROM `Jobs` GROUP BY profession, modality;"
    query = "SELECT profession, avg( salary ) as avg_salary FROM `Jobs` GROUP BY profession ORDER BY avg_salary ASC;"
    myCursor.execute(query)
    professions = []
    salaryAVG = []
    for tuple in myCursor:
        professions.append(tuple[0])
        salaryAVG.append(tuple[1])

    return (professions, salaryAVG)


# pepe = Job(profession="Hostelero", link="a",
#            salary="$ 3,500,000.00 (Mensual)", place="Bogotá, DC")
# insertData(pepe)
# checkDataGeneral()
# deleteData(pepe)
# checkDataGeneral()
avergPerJob()
