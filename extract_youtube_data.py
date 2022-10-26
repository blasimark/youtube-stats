import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
import pandas as pd
import datetime
import sqlalchemy
import sqlite3
import pickle


load_dotenv()
API_KEY = os.getenv("API_KEY")
DATABASE_LOCATION = "sqlite:///youtube_stats.sqlite"


def channel_stats(channel_id):

    query = build("youtube", "v3", developerKey=API_KEY)
    request = query.channels().list(
        part="statistics",
        id=channel_id
    )

    return request.execute()["items"][0]["statistics"]


def check_if_valid_data(df):
    if df.empty:
        print("No data downloaded. Finishing execution")
        return False

    if df.isna().values.any():
        raise Exception("Missing values found")

    return True


def main():
    name = []
    view_count = []
    subscriber_count = []
    video_count = []
    today = datetime.datetime.now().strftime("%Y-%m-%dT%H")
    date = []

    with open("channel_dict.pkl", "rb") as file:
        channel_dict = pickle.load(file)

    for channel, id in channel_dict.items():
        date.append(today)
        name.append(channel)
        response = channel_stats(id)
        view_count.append(int(response["viewCount"]))
        subscriber_count.append(int(response["subscriberCount"]))
        video_count.append(int(response["videoCount"]))

    data_dict = {
        "Date": date,
        "Name": name,
        "View count": view_count,
        "Subscriber count": subscriber_count,
        "Video count": video_count
        }

    df = pd.DataFrame(data_dict)

    if check_if_valid_data(df):
        print("Data valid, proceed to Load stage")

    engine = sqlalchemy.create_engine(DATABASE_LOCATION)
    con = sqlite3.connect("youtube_stats.sqlite")
    cur = con.cursor()

    sql_query = """
    CREATE TABLE IF NOT EXISTS youtube_stats(
        Date VARCHAR(200),
        Name VARCHAR(200),
        View count INT,
        Subscriber count INT,
        Video count INT
    )
    """
    cur.execute(sql_query)
    # from sqlalchemy import inspect
    # inspector = inspect(engine)
    # print(inspector.get_table_names())
    try:
        df.to_sql("youtube_stats", engine, index=False, if_exists="append")
        print("Data successfully put into database")
    except Exception:
        print("Data already exists in the database")

    con.close()
    print("Database closed successfully")


if __name__ == "__main__":
    main()
