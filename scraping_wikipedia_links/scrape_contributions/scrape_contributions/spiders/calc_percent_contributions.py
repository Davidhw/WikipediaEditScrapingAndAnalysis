# files that hold lists of users
import re,sys
from prettytable import *
import numpy as np

user_types = ['admin','bot','freq','infreq','anon']
sources = ["reddit","random","featured","popular"]

global bots,admins,freqs,user_type_dict
user_type_dict={}

def output_table(rows,collumn_headers):
    x = PrettyTable(collumn_headers)
    x.padding_width = 1 # One space between column edges and contents (default)
    for row in rows:
        x.add_row(row)
    print x

def output_results(all_source_percentages):
    # a bit round about because I had the orders stored in a manner opposite of how I want to present them
    all_sources = all_source_percentages.keys()

    # iterates a few exta times, same for each iteration
    for source in all_sources:
        user_types = all_source_percentages[source].keys()
#        break

    # dictionary. Each entry will hold a list [key, statforsrce, statforsrce..]
    user_percents_rows = {}
    for user_type in user_types:
        user_percents_rows[user_type] = []
        user_percents_rows[user_type].append(user_type)

    for source in all_sources:
        for user_type in user_types:
            user_percents_rows[user_type].append(str(100*round(all_source_percentages[source][user_type],4)))

    rows = []
    # order rows are appended in doesn't matter because label is at row[0]
    for user_type in user_types:
        rows.append(user_percents_rows[user_type])

    collumn_headers =['']+sources
    output_table(rows,collumn_headers)
#        user_types = source



def print_percentages(percentages_dict,user_types):
    i = 0
    for user_type in user_types:
        print percentages_dict[user_type]
    
def calc_percentages_for_all_sources(source_files,weighted=True):
    sources = source_files.keys()
    all_source_percentages ={}
    for source in sources:
        print source
        all_source_percentages[source] = calc_percentages(eval_contributions(source_files[source],user_types,weighted),user_types)
    return all_source_percentages

def calc_percentages(contributions_dict,user_types):
    # calculates the percent contributions to each article type by each user type
    total_contributions = 0
    for user_type in user_types:
        total_contributions += contributions_dict[user_type]
    
    percentages_dict = {}
    for user_type in user_types:
        percentages_dict[user_type] = (contributions_dict[user_type])/float(total_contributions)

    return percentages_dict



def load_list_from_file(file,lines=None):
    global bots, admins, freqs
    line_list = []
    i = 0
    with open(file,'r') as input:
        if lines == None:
            for line in input.readlines():
                line_list.append(line.strip())
        else:
            for line in input.readlines():
                if i==lines:
                    break
                elif line.strip() not in bots and line.strip() not in admins:
                    line_list.append(line.strip())
                    i+=1
    return line_list

def load_users_info(admins_f,bots_f,freqs_f,freq_ed_amount):
    global bots, admins, freqs
    bots = load_list_from_file(bots_f)
    admins = load_list_from_file(admins_f)
    freqs = load_list_from_file(freqs_f,freq_ed_amount)

def load_source_file_names():
    source_files = {}
    source_files["reddit"] = 'contributions_to_wikipedia_subreddit_links'
    source_files["random"] = 'contributions_to_random_wikipedia_links'
    source_files["featured"] = 'contributions_to_wikipedia_featured_links'
    source_files["popular"] = 'contributions_to_wikipedia_popular_links'
    return source_files

def eval_contributions(file,user_types,weighted):
    global user_type_dict
    contributions = load_list_from_file(file)
    print len(contributions)

    contributions_dict = {}
    for user_type in user_types:
        contributions_dict[user_type]=0

    for contribution in contributions:
        split = contribution.strip().split(',')
        user_splits = split[0:-1]
        user =''
        for us in user_splits:
            user+= us
        str_size = split[-1]
        if str_size =="ERROR":
            # happens for talk contributions
            contribution_size = 0

        else:
            try:
                contribution_size = int(split[-1])
            except:
                try:
                    # some names were scraped with a | in front of them
                    contribution_size = int(re.sub('[^\d]','',split[-1]))
                except:
                    print split
                    sys.exit(1)
                    print contribution_size
#        user_type = get_user_type(user)
        if user in user_type_dict:
            user_type = user_type_dict[user]
        else:
            user_type = get_user_type(user)
            user_type_dict[user] = user_type
        if weighted:
            contributions_dict[user_type]+=weigh_contribution(contribution_size)
        else:
            contributions_dict[user_type]+=1

    return contributions_dict

def weigh_contribution(contribution_size):
    if contribution_size <0:
        if contribution_size <-10:
            return 10
        else:
            return abs(contribution_size)
    else:
        return contribution_size
def get_user_type(user):
    global bots, admins, freqs
    if user in bots:
        return 'bot'
    elif user in admins:
        return 'admin'
    elif user in freqs:
        return 'freq'
    # check for ip address
    # sample ip: 94.173.122.171
    elif re.search(r'\d+\.\d+.\d+.\d+',user):
        return 'anon'
    else:
        return 'infreq'

#['admins','bots','bfreqs','anon','infreq']
def run():
    global user_type_dict
    freq_eds_amounts = [100,500,1000,1500,2000,2500,3000,3500,4000]
    for freq_ed_amount in freq_eds_amounts:
        user_type_dict = {}
        admins_f = 'admins_list'
        bots_f = 'bots_list'
    # 4 contains 500, 3 contains 2000, 5 1000
#    freqs_f = 'most_frequent_editors_list5'
        freqs_f = 'most_freq_eds_placeholder_removed'
        load_users_info(admins_f,bots_f,freqs_f,freq_ed_amount)
        print "\n Frequent Editors are top ",freq_ed_amount, " editors."
        print "weighted"
        output_results(calc_percentages_for_all_sources(load_source_file_names()))
        print "unweighted"
        output_results(calc_percentages_for_all_sources(load_source_file_names(),False))
        print "num of each type of users"
        how_many_freq()

def how_many_freq():
    global user_type_dict

    freqs_sum = 0
    admins_sum = 0
    bots_sum =0
    anons_sum = 0
    infreqs_sum = 0

    for item in user_type_dict.iterkeys():
        if user_type_dict[item]=='freq':
            freqs_sum+=1
        elif user_type_dict[item]=='admin':
            admins_sum+=1
        elif user_type_dict[item]=='bot':
            bots_sum+=1
        elif user_type_dict[item]=='anon':
            anons_sum+=1
        elif user_type_dict[item]=='infreq':
            infreqs_sum+=1

    total = float(freqs_sum+admins_sum+anons_sum+infreqs_sum+bots_sum)
    print "bots ",bots_sum ," ", 100*round(bots_sum/total,4)
    print "admins " ,admins_sum ," " ,100*round(admins_sum/total,4)
    print "freqs ",freqs_sum ," " ,100*round(freqs_sum/total,4)
    print "infreqs ",infreqs_sum ," ", 100*round(infreqs_sum/total,4)
    print "anons ",anons_sum ," ", 100*round(anons_sum/total,4)


run()

