# clean group urls into group_number_list

import pandas as pd
import re

groups_df = pd.read_csv('SupportGroupNumbers.csv', header=None)
groups_lst = groups_df[0].values.tolist()


def extract_nums(url_list):
    group_number_list = []
    for i in range(0, len(groups_lst)):
        group_number_list.append(re.findall(r'\d+', groups_lst[i]))
    return group_number_list

group_number_list = extract_nums(groups_lst)
group_number_list
