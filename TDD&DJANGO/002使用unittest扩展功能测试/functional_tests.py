"""
有用的TDD概念
1.用户故事
    从用户的角度描述应用应该如何运行，用来组织功能测试
2.预期失败
    意料中的失败
"""
from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://127.0.0.1:8000/')
        self.assertIn('To-Do', self.browser.title)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
