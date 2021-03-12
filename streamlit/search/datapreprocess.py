from datetime import datetime
import csv
import pytz
import pandas as pd

captions = pd.read_csv("results.csv", sep="delimeter")
captions["image_name| comment_number| comment"] = [
    x.split(" ")[2:] for x in captions["image_name| comment_number| comment"]
]
captions["image_name| comment_number| comment"] = captions[
    "image_name| comment_number| comment"
].str.join(",")
captions["image_name| comment_number| comment"] = captions[
    "image_name| comment_number| comment"
].str.replace(",", " ")
captions.rename(
    columns={"image_name| comment_number| comment": "Caption"}, inplace=True
)
captions.insert(1, "Time", datetime.now(pytz.timezone("Asia/Kolkata")))
captions.insert(2, "Camera", 1)
