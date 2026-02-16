#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import ipaddress
from urllib.parse import urlparse
import re
from collections import Counter



def path_to_length_ratio(url):
    try:
        url = str(url).strip()
        if not url:
            return 0.0

        parsed = urlparse(url)
        total_length = len(url)
        if total_length == 0:
            return 0.0

        path_length = len(parsed.path)
        return path_length / total_length
    except Exception:
        return 0.0


def length_of_url(url):
    return len(url)


def special_char_ratio(url):
    special_chars = ".-@?=&_%/#"
    special_count = sum(1 for char in url if char in special_chars)
    return special_count / len(url)


def suspicious_char_count(url):
    return sum(1 for char in url if not char.isalnum())


def slash_count(url):
   slash='/' 
   slash_cunt=sum(1 for char in url if char in slash)
   return slash_cunt


def tokenize(url):
    url=url.lower()
    token= re.split(r'[-/?=&]',url)
    return [t for t in token if t]


def count_suspicious_keywords(url, suspicious_keywords):
    tokens = tokenize(url)
    return sum(1 for token in tokens if token in suspicious_keywords)


def no_dot_present(url):
   dot='.'
   dot_count=sum(1 for char in url if char in dot)
   return dot_count

def has_query(url):
    try:
        url = str(url).strip()
        if not url:
            return 0

        parsed = urlparse(url)
        return int(bool(parsed.query))
    except Exception:
        return 0


def no_question_marks(url):
    meow='?'
    question_count= sum(1 for char in url if char in meow )
    return question_count


def countDashesInUrls(url):
    mark = '-'
    count = 0
    for i in url:
        if i == mark:
            count+=1
    return count


def countAtInUrls(url):
    mark = '@'
    count = 0
    for i in url:
        if i == mark:
            count+=1
    return count


def findASymbolAtLast(url):
    if url[-1] == '/':
        return 0
    if not url[-1].isalnum():
        return 1
    return 0


def checkHttpInMiddle(url):
    substr = 'http'
    url = url[4:]
    for i in range(len(url)-len(substr)+1):
        if url[i:i+len(substr)] == substr:
            return True
    return False


def has_ip_address(url):
    if not url:
        return False
    candidates = re.findall(r"(?:\d{1,3}\.){3}\d{1,3}", url)
    for candidate in candidates:
        try:
            ipaddress.ip_address(candidate)
            return True
        except ValueError:
            continue
    return False


def has_unicode_chars(url):
    if not url:
        return False
    return any(ord(ch) > 127 for ch in url)


def has_port_number(url):
    if not url:
        return False
    return re.search(r":\d{1,5}\b", url) is not None



from feature_extraction import *
import pandas as pd
import numpy as np


def add_features(df, url_column="url"):

    print("Making new features :)")

    # -----------------------------
    # Vectorizable features
    # -----------------------------

    print("Creating url_length...")
    df["url_length"] = df[url_column].str.len()  

    print("Creating num_slashes...")
    df["num_slashes"] = df[url_column].str.count(r"/")

    print("Creating num_dots...")
    df["num_dots"] = df[url_column].str.count(r"\.")

    print("Creating num_question_marks...")
    df["num_question_marks"] = df[url_column].str.count(r"\?")

    print("Creating num_dashes...")
    df["num_dashes"] = df[url_column].str.count(r"-")

    print("Creating num_at...")
    df["num_at"] = df[url_column].str.count(r"@")

    print("Creating has_query...")
    df["has_query"] = df[url_column].apply(has_query)  

    print("Creating path_to_length_ratio...")
    df["path_to_length_ratio"] = df[url_column].apply(path_to_length_ratio)  

    print("Creating special_char_ratio...")
    df["special_char_ratio"] = df[url_column].apply(special_char_ratio)  

    print("Creating suspicious_char_count...")
    df["suspicious_char_count"] = df[url_column].apply(suspicious_char_count)  

    print("Creating symbol_at_end...")
    df["symbol_at_end"] = df[url_column].apply(findASymbolAtLast) 

    print("Creating http_in_middle...")
    df["http_in_middle"] = df[url_column].apply(checkHttpInMiddle)  

    print("Creating has_ip...")
    df["has_ip"] = df[url_column].apply(has_ip_address) 

    print("Creating has_unicode...")
    df["has_unicode"] = df[url_column].apply(has_unicode_chars)  

    print("Creating has_port...")
    df["has_port"] = df[url_column].apply(has_port_number)  

    print("All features created successfully ✅")

    return df


def download_csv(df, path):
    df.to_csv(path, index=False)
    print(f"File saved successfully at: {path}")



