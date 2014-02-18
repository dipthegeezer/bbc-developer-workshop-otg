import unittest
from unittest import TestCase

import json
from datetime import datetime

# Go and import the source path
import os
import sys

src_path = os.path.join(os.path.dirname(__file__), "../src/")
sys.path.insert(0, src_path)
fixture_file = os.path.join(os.path.dirname(__file__), "fixture.json")

import lib


class LibraryTest(TestCase):
    def setUp(self):
        json_data = open(fixture_file)
        self.data = json.load(json_data)
        json_data.close()

    def test_extract_episode_data(self):
        json_array = lib.extract_episode_data(self.data)
        self.assertEquals(len(json_array.get('episodes')), 2)

        first_expected_episode = {'subtitle': 'Sochi 2014, Day 8',
                                  'title': 'Winter Olympics: Today at the Games',
                                  'online_availability_window': '7 days, 0:59:00'}
        second_expected_episode = {'subtitle': 'Sochi 2014, Day 8, Part 3',
                                   'title': 'Winter Olympics',
                                   'online_availability_window': '7 days, 2:59:00'}

        self.assertEquals(first_expected_episode,
                          json_array.get('episodes')[0])

        self.assertEquals(second_expected_episode,
                          json_array.get('episodes')[1])

    def test_string_to_datetime(self):
        string = "2014-02-14T22:00:00Z"
        expected = datetime(2014, 2, 14, 22, 00)
        actual = lib.string_to_datetime(string)
        self.assertEquals(expected, actual)


class TimeAvailableTest(TestCase):
    
    def test_broadcast_is_same_as_available(self):
        broadcast_date = datetime(2014, 02, 23, 19, 05, 00)
        available_until = datetime(2014, 02, 23, 19, 05, 00)

        time_since = lib.get_online_availability_window(broadcast_date, available_until)

        expected = "0:00:00"
        self.assertEquals(expected, time_since)

    def test_available_under_a_day(self):
        
        expected = "1:00:00"
        self.assertEquals(expected, time_since)

    def test_available_more_than_one_day(self):
 
    def test_available_more_than_two_days(self):
   

if __name__ == '__main__':
    unittest.main()
