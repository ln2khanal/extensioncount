
import os
import optparse
import csv

from collections import defaultdict


def __read_file_types(target_directory):
    """
    files without extension will be written as WE_fineName
    :param target_directory: dict, file type details
    :return: dict, file types
    """
    file_types = defaultdict(int)
    for root, dirs, files in os.walk(target_directory):
        for f in files:
            file_name_extension = f.rsplit(".", 1)
            if len(file_name_extension) == 2:
                file_types[file_name_extension[1]] += 1
            else:
                file_types["WE_%s" % file_name_extension[0]] += 1

    return file_types


def __write_to_csv(dict_content):
    """
    writes dict objects to a csv file: extension,count
    :param dict_content: dict, file type details
    :return: None
    """
    with open("file_types.csv", "w") as f:
        headers = [
            "extension",
            "count"
        ]
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for key, value in sorted(dict_content.iteritems(), key=lambda (k, v): (v, k)):
            writer.writerow({headers[0]: key, headers[1]: value})


def main():
    options, arguments = optparse.OptionParser(__doc__).parse_args()

    assert len(arguments) > 0

    target_dir = str(arguments[0]).strip()
    file_types = __read_file_types(target_dir)

    __write_to_csv(file_types)


if __name__ == "__main__":
    main()
