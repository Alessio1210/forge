import sqlalchemy
import typer
from sqlalchemy.exc import SQLAlchemyError

app = typer.Typer()



def testcpnnection():
    engine_type = input("welche engine? (postgres/mysql/mariadb/sqlserver/sqlite): ").lower()

    if engine_type == "sqlite":
        db = input("sqlite file path, or :memory:: ")
        url = f"sqlite:///{db}"

    else:
        server = input("was ist dei ip oder der server: ")
        db = input("wie heißt die datenbank: ")
        username = input("was ist der username: ")
        pw = input("was ist das password: ")

        if engine_type == "postgres":
            url = f"postgresql+psycopg2://{username}:{pw}@{server}:5432/{db}"

        elif engine_type == "mysql":
            url = f"mysql+pymysql://{username}:{pw}@{server}:3306/{db}"

        elif engine_type == "mariadb":
            url = f"mysql+pymysql://{username}:{pw}@{server}:3306/{db}"

        elif engine_type == "sqlserver":
            url = (
                f"mssql+pyodbc://{username}:{pw}@{server}/{db}"
                "?driver=ODBC+Driver+18+for+SQL+Server"
            )

        else:
            print("engine kenn ich nicht")
            return

    try:
        engine = sqlalchemy.create_engine(url)

        with engine.connect():
            print("connection hat geklappt")

    except Exception as e:
        print("connection fehlgeschlagen")
        print(e)



if __name__ == "__main__":
    testcpnnection()


"""
db querys = shows all querys that are used in the project and says what the results will be and from where the data comes
"""
