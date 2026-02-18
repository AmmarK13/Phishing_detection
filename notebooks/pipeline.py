from feature_extraction import *
import pandas as pd
import argparse

def main(input_path,output_path):
    df=pd.read_csv(input_path)

    #Extract features

    df=add_features(df=df,url_column="url")

    download_another_csv(df,output_path)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add phishing URL features to a CSV dataset")
    parser.add_argument("-i", "--input", required=True, help="Path to input CSV file")
    parser.add_argument("-o", "--output", required=True, help="Path to save output CSV file")

    args = parser.parse_args()
    main(args.input, args.output)