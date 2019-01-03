import unittest
import requests
import os
import csv

from requests_toolbelt.multipart import encoder


def transform_data(resp):
    arr = resp.text.split('\n')
    arr = arr[1:len(arr)-1]
    answers = []
    for key in arr:
        (_words, answer) = key.split(',')
        answers.append(answer)

    return answers


def check_equality(answers, file_name):
    index = 0
    count = 0
    f = open(file_name, 'r')
    file_data = csv.reader(f)
    for row in file_data:
        if(row[0] == answers[index]):
            count += 1
        index += 1
    f.close()
    return count


def test_case_layout(file_name, solution_file_name):
    url = os.getenv('BASE_URL', None)
    if url is None:
        raise "Base url is not export in the enviorment."

    with open(file_name, 'rb') as f:
        form = encoder.MultipartEncoder({
            "df_file": (file_name, f, "text/csv")
        })
        headers = {"Content-Type": form.content_type}
        resp = requests.post(url, headers=headers, data=form)
        answers = transform_data(resp)
        count = check_equality(
            answers, solution_file_name)

        return (answers, count)

class TestMlApplication(unittest.TestCase):

    def test_classifier_small(self):
        (answers, count) = test_case_layout('TestCases/test_case_1.csv', 'TestCases_Solutions/test_case_1_solutions.csv')
        assert (count >= len(answers)/2)

    def test_classifier_medium(self):
        (answers, count) = test_case_layout('TestCases/test_case_2.csv', 'TestCases_Solutions/test_case_2_solutions.csv')
        assert (count >= len(answers)/2)

    def test_classifier_large(self):
        (answers, count) = test_case_layout('TestCases/test_case_3.csv', 'TestCases_Solutions/test_case_3_solutions.csv')
        assert (count >= len(answers)/2)

    
if __name__ == '__main__':
    unittest.main()
