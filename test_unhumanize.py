import unittest
from datetime import timedelta
from unhumanize import *

class UnHumanizeTest(unittest.TestCase):

  def test_past_time_intervals(self):
    self.assertEqual(timedelta(seconds=-1), unhumanize('a moment ago'))
    self.assertEqual(timedelta(seconds=-3), unhumanize('3 moments ago'))
    self.assertEqual(timedelta(seconds=-23), unhumanize('23 seconds ago'))
    self.assertEqual(timedelta(seconds=-1), unhumanize('a second ago'))
    self.assertEqual(timedelta(minutes=-27), unhumanize('27 minutes ago'))
    self.assertEqual(timedelta(minutes=-1), unhumanize('a minute ago'))
    self.assertEqual(timedelta(hours=-3), unhumanize('3 hours ago'))
    self.assertEqual(timedelta(hours=-1), unhumanize('an hour ago'))
    self.assertEqual(timedelta(days=-12), unhumanize('12 days ago'))
    self.assertEqual(timedelta(days=-1), unhumanize('a day ago'))
    self.assertEqual(timedelta(days=-7), unhumanize('a week ago'))
    self.assertEqual(timedelta(days=-42), unhumanize('6 weeks ago'))
    self.assertEqual(timedelta(days=-6 * 30), unhumanize('6 months ago'))
    self.assertEqual(timedelta(days=-6 * 365), unhumanize('6 years ago'))

  def test_future_time_intervals(self):
    self.assertEqual(timedelta(days=1), unhumanize('a day'))
    self.assertEqual(timedelta(hours=1), unhumanize('an hour'))
    self.assertEqual(timedelta(seconds=1), unhumanize('a moment'))
    self.assertEqual(timedelta(seconds=23), unhumanize('23 seconds'))

  def test_zero_time_intervals(self):
    self.assertEqual(timedelta(seconds=0), unhumanize('just now'))

  def test_strange_formatting_time_intervals(self):
    self.assertEqual(timedelta(days=-1), unhumanize('   a     day ago'))
    self.assertEqual(timedelta(hours=1), unhumanize('an   hour'))
    self.assertEqual(timedelta(seconds=1), unhumanize(' a moment'))
    self.assertEqual(None, unhumanize('2 3 seconds'))
    self.assertEqual(None, unhumanize(' foo bar baz'))


if __name__ == '__main__':
  unittest.main()
