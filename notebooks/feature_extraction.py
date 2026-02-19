#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import ipaddress
from urllib.parse import urlparse
import re
from collections import Counter
import tldextract
import math



special_keywords=['http:',
 'wp',
 'https:',
 'index.php',
 'includes',
 'content',
 'images',
 'login',
 'admin',
 'js',
 '1',
 'login.php',
 'dropbox',
 'email',
 'en',
 'plugins',
 'cmd',
 'css',
 'secure',
 'index.html',
 'themes',
 'home',
 'id',
 'rand',
 'amp;fid',
 'update',
 'n',
 'amp',
 '13inboxlightaspxn.1774256418',
 'doc',
 'amp;fav.1',
 'index.htm',
 'site',
 'file',
 'view',
 'data',
 'userid',
 '1774256418',
 'alibaba',
 'm',
 'auth',
 'sites.google.com',
 'ref',
 'account',
 '13inboxlight.aspx',
 'ii.php',
 'gate.php',
 'index',
 '4',
 'modules',
 'l',
 'document',
 'us.battle.net',
 'components',
 'login_submit',
 'files',
 'amp;id',
 'fid',
 'us',
 'new',
 'd3',
 '0',
 'media',
 'bookmark',
 'img',
 'amp;email',
 'libraries',
 'signin',
 'system',
 'amp;fid.4.1252899642',
 'amp;fid.1',
 'cp.php',
 'amp;fid.1252899642',
 'dhl',
 'amp;session',
 'user',
 'myaccount',
 'uploads',
 'amp;rand.13inboxlight.aspxn.1774256418',
 'a',
 'amp;.rand',
 'templates',
 'cgi',
 'app',
 '.rand',
 'bin',
 'web',
 'websc',
 'go',
 '...',
 'page',
 'www.paypal.com',
 '2',
 'db',
 'remax',
 'blog',
 'fav.1',
 'logs',
 '_jehfuq_vjoxk0qwhtogydw_product',
 'upload']

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


def digit_ratio_in_domain(url):
    try:
        url = str(url).strip()
        if not url:
            return 0
        hostname = urlparse(url).hostname
        if not hostname:
            return 0
        digits = sum(c.isdigit() for c in hostname)
        total_chars = len(hostname)
        return digits / total_chars if total_chars > 0 else 0
    except Exception:
        return 0
    

def num_subdomains(url):
    try:
        url = str(url).strip()
        if not url:
            return 0
        hostname = urlparse(url).hostname  
        if not hostname:
            return 0
        parts = hostname.split('.')  
        
        if len(parts) <= 2:
            return 0
        return len(parts) - 2
    except Exception:
        return 0

def has_query(url):
    try:
        url = str(url).strip()
        if not url:
            return False

        parsed = urlparse(url)
        return (bool(parsed.query))
    except Exception:
        return False


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
        return False
    if not url[-1].isalnum():
        return True
    return False


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

def domain_length(url):
    try:
        parsed = urlparse(url)
        ext = tldextract.extract(url)
        domain = ext.domain
        return len(domain)
    except Exception:
        return 0
    

def url_entropy(url):
    try:
        url = str(url)
        if not url:
            return 0.0
        counts = {}
        for c in url:
            counts[c] = counts.get(c, 0) + 1
        entropy = 0.0
        length = len(url)
        for count in counts.values():
            p = count / length
            entropy -= p * math.log2(p)
        return entropy
    except Exception:
        return 0.0


def get_tld(url):
    try:
        ext = tldextract.extract(url)
        tld = ext.suffix.lower()  # e.g., 'com', 'xyz'
        return tld if tld else ''
    except Exception:
        return ''




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

    print("Creating keyword count...")
    df["special_keyword_count"] = df["url"].apply(
    lambda x: count_suspicious_keywords(x, special_keywords)
)
    print("Creating sub domain count...")
    df["num_subdomain"]=df["url"].apply(num_subdomains)

    print("Creating digit ratio in domain....")
    df["digit_ratio_in_domain"]=df["url"].apply(digit_ratio_in_domain)

    print("Creating tld  risk ..")
    df["has_risk"]=df["url"].apply(get_tld)

    print("Creating url entropy ..")
    df["url_entropy"]=df["url"].apply(url_entropy)
    
    print("Creating domain length ..")
    df["domain_lenght"]=df["url"].apply(domain_length)

    print("All features created successfully ✅")

    return df


def download_csv(df, path):
    df.to_csv(path, index=False)
    print(f"File saved successfully at: {path}")


def download_another_csv(df, path):
    features_to_save = ['url_length', 'num_slashes', 'num_question_marks', 'num_dashes',
       'num_at', 'symbol_at_end', 'http_in_middle', 'has_ip', 'has_port','type']
    df[features_to_save].to_csv(path, index=False)
    print(f"File saved successfully at: {path}")