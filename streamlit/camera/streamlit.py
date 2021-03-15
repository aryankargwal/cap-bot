import streamlit as st
import cv2
import csv
from PIL import Image
import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
import time
from datetime import datetime
from cap_generator import *

# To display the webcam feed
FRAME_WINDOW = st.image([])
TOKENIZER = Tokenizer(num_words=1000, oov_token="<UNK>")

@st.cache(show_spinner=False)
class CSVWorker:
    def __init__(self):
        self.fields = [
            "w1",
            "w2",
            "w3",
            "w4",
            "w5",
            "w6",
            "w7",
            "w8",
            "w9",
            "w10",
            "time",
            "camera",
        ]
        self.filename = "results.csv"
        self.create_csv()

        # self.word_idx = None
        self.token_fit()

    def preprocess(self, text, tokenizer):
        sequences = tokenizer.texts_to_sequences(text)
        return sequences

    def token_fit(self):
        captions = pd.read_csv("flickr_captions.csv", sep="delimeter")
        captions["image_name| comment_number| comment"] = [
            x.split(" ")[2:] for x in captions["image_name| comment_number| comment"]
        ]
        captions["image_name| comment_number| comment"] = captions[
            "image_name| comment_number| comment"
        ].str.join(",")
        captions["image_name| comment_number| comment"] = captions[
            "image_name| comment_number| comment"
        ].str.replace(",", " ")
        captions["image_name| comment_number| comment"] = captions[
            "image_name| comment_number| comment"
        ].str.replace("  ", " ")
        captions.rename(
            columns={"image_name| comment_number| comment": "Caption"}, inplace=True
        )
        TOKENIZER.fit_on_texts(list(captions["Caption"]))
        # Get our training data word index
        # self.word_idx = self.Tokenizer.word_index

    def create_csv(self):
        df = pd.DataFrame(list(), columns=self.fields)
        df.to_csv(self.filename)

    def write(self, pred):
        df = pd.read_csv(self.filename)
        pred = self.preprocess(pred, TOKENIZER)
        if len(pred) >= 10:
            entry = [
                pred[0],
                pred[1],
                pred[2],
                pred[3],
                pred[4],
                pred[5],
                pred[6],
                pred[7],
                pred[8],
                pred[9],
                datetime.now(),
                1,
            ]
        elif len(pred) < 10:
            entry = []
            for i in range(len(pred)):
                entry.append(pred[i])
            for i in range(len(entry) - 1, 11):
                entry.append("")
            entry.append(datetime.now)
            entry.append(1)
        with open(self.filename, "a") as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)
            # writing data rows
            csvwriter.writerow(entry)


def run_app():
    vid = cv2.VideoCapture(0)
    # Starts the app, when the button is clicked
    run = st.checkbox("Run", key="start")
    show_frame = st.checkbox("Show frames", key="frame")
    csvw = CSVWorker()
    while run:
        _, frame = vid.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        if show_frame:
            FRAME_WINDOW.image(frame)
        img = Image.fromarray(frame)
        img = img.resize((224, 224))
        pred = test(img)
        csvw.write(pred)
        st.write(pred)
        time.sleep(5)
    vid.release()
    cv2.destroyAllWindows()


def main():
    run_app()

if __name__ == "__main__":
    main()
