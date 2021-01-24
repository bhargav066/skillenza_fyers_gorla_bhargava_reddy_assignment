import logging
from collections import defaultdict
import sys
import json

if __name__ == '__main__':
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    # checking for csv file path
    if len(sys.argv) != 2:
        logging.error('please provide csv file path in args')
        raise FileNotFoundError
    file_path = sys.argv[1]
    # setting default count as 0 using lambda function
    airport_dict = defaultdict(lambda: 0)
    max_airport_count_name = None
    max_airport_count = None
    min_airport_count_name = None
    min_airport_count = None
    with open(file_path) as csv_file:
        for line_num, line in enumerate(csv_file):
            if line_num == 0:
                # ignoring header
                continue
            # accessing only airport name
            airport_name = line.split('"')[1]
            present_count = airport_dict[airport_name]
            updated_count = present_count + 1
            airport_dict[airport_name] = updated_count
            # updating max and min airport count with first value
            if line_num == 1:
                max_airport_count_name = airport_name
                max_airport_count = updated_count
                min_airport_count_name = airport_name
                min_airport_count = updated_count
                continue
            # updating max airport name and count
            if updated_count > max_airport_count:
                if max_airport_count_name != airport_name:
                    max_airport_count_name = airport_name
                max_airport_count = updated_count
            # updating min airport and count
            if updated_count <= min_airport_count:
                if min_airport_count_name != airport_name:
                    min_airport_count_name = airport_name
                min_airport_count = updated_count
    print(json.dumps(airport_dict))
    print('%s : %d' % (max_airport_count_name, max_airport_count))
    print('%s : %d' % (min_airport_count_name, min_airport_count))
