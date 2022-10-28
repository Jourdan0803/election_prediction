#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from textblob.classifiers import NaiveBayesClassifier
import pandas as pd

filename = "../archive/hashtag_joebiden.csv"


def read_info_from_dataset(filename):
    try:
        data = pd.read_csv(filename, skiprows=0, nrows=1000)
        # data = pd.read_csv(filename)
        return data
    except:
        print("CSV file read failed")
        return None


def process_data():
    support_to_Trump = 0
    support_to_Biden = 0
    data = read_info_from_dataset(filename)
    tweet = data["tweet"].values
    # likes = data["likes"].values
    # retweet_count = data["retweet_count"].values
    state_code = data["state_code"].values
    Biden_support_in_state = {'CA': 0}
    Trump_support_in_state = {'CA': 0}
    # cl = NaiveBayesClassifier()
    for i in range(len(tweet)):
        blob = TextBlob(tweet[i], analyzer=NaiveBayesAnalyzer())
        # print("Tweet {0}: {1}".format(i, tweet[i]))
        # print("like of Tweet {0}: {1}".format(i, likes[i]))
        # print("Num of reTweet: {0}".format(retweet_count[i]))
        print("Tweet #{0} : {1}".format(i, blob.sentiment[0]))
        # print("result to Tweet {0}: {1}".format(i,  blob.classify()))
        print("state code: {0}".format(state_code[i]))
        if 'Trump' or 'realDonaldTrump' in blob.words:
            if blob.sentiment[0] == 'pos':
                support_to_Trump += 1
                if Trump_support_in_state.__contains__(state_code[i]):
                    Trump_support_in_state[state_code[i]] = Trump_support_in_state.get(state_code[i]) + 1
                else:
                    Trump_support_in_state[state_code[i]] = 1
                print("sup to Trump: {0}".format(support_to_Trump))
            else:
                if Biden_support_in_state.__contains__(state_code[i]):
                    Biden_support_in_state[state_code[i]] = Biden_support_in_state.get(state_code[i]) + 1
                else:
                    Biden_support_in_state[state_code[i]] = 1
                support_to_Biden += 1
                print("sup to Biden: {0}".format(support_to_Biden))
        elif 'Biden' or 'JoeBiden' or 'Democrats' in blob.words:
            if blob.sentiment[0] == 'pos':
                support_to_Biden += 1
                if Biden_support_in_state.__contains__(state_code[i]):
                    Biden_support_in_state[state_code[i]] = Biden_support_in_state.get(state_code[i]) + 1
                else:
                    Biden_support_in_state[state_code[i]] = 1
                print("sup to Biden: {0}".format(support_to_Biden))
            else:
                support_to_Trump += 1
                if Trump_support_in_state.__contains__(state_code[i]):
                    Trump_support_in_state[state_code[i]] = Trump_support_in_state.get(state_code[i]) + 1
                else:
                    Trump_support_in_state[state_code[i]] = 1
                print("sup to Biden: {0}".format(support_to_Trump))
        else:
            print("irrelevant tweet")
        print()
    # for i in range(len(support_in_state.keys())):
    print("support to Biden: {0}\nsupport to Trump: {1}".format(support_to_Biden, support_to_Trump))
    # California
    print("CA for Trump:{0}; \tBiden:{1}".format(Trump_support_in_state.get('CA'), Biden_support_in_state.get('CA')))
    # Florida
    print("FL for Trump:{0}; \tBiden:{1}".format(Trump_support_in_state.get('FL'), Biden_support_in_state.get('FL')))
    # Georgia
    print("GA for Trump:{0}; \tBiden:{1}".format(Trump_support_in_state.get('GA'), Biden_support_in_state.get('GA')))
    # Illinois
    print("IL for Trump:{0}; \tBiden:{1}".format(Trump_support_in_state.get('IL'), Biden_support_in_state.get('IL')))
    # Michigan
    print("MI for Trump:{0}; \tBiden:{1}".format(Trump_support_in_state.get('MI'), Biden_support_in_state.get('MI')))
    # New York
    print("NY for Trump:{0}; \tBiden:{1}".format(Trump_support_in_state.get('NY'), Biden_support_in_state.get('NY')))
    # North Carolina
    print("NC for Trump:{0}; \tBiden:{1}".format(Trump_support_in_state.get('NC'), Biden_support_in_state.get('NC')))
    # Ohio
    print("OH for Trump:{0}; \tBiden:{1}".format(Trump_support_in_state.get('OH'), Biden_support_in_state.get('OH')))
    # Pennsylvania
    print("PA for Trump:{0}; \tBiden:{1}".format(Trump_support_in_state.get('PA'), Biden_support_in_state.get('PA')))
    # Texas
    print("TX for Trump:{0}; \tBiden:{1}".format(Trump_support_in_state.get('TX'), Biden_support_in_state.get('TX')))


if __name__ == '__main__':
    process_data()
