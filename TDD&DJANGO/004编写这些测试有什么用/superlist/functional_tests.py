# -*- coding:utf-8 -*-
"""
TDD同时采用单元和功能测试流程

1.先写功能测试，从用户的角度描述应用的新功能
2.功能测试失败后，想办法编写代码让它通过（或者说至少让当前失败的测试通过
此时，使用一个或多个单元测试定义希望代码实现的结果，保证为应用的每一行代码
至少编写一个单元测试
3.单元测试失败后，编写最少量的应用代码，刚好让单元测试通过，有时要和第二和第三
步之间多次往返，直到我们觉得功能测试有一点进展为止
4.然后再运行功能测试，看能否通过，或者有没有进展，这一步可能促使我们编写一些新的
单元测试和代码等
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
        inputbox.send_keys('Buy peacock feathers')

        inputbox.send_keys(Keys.ENTER)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: Buy peacoke feathers' for row in rows))

        self.fail('Finish the test')


if __name__ == '__main__':
    unittest.main()


"""
TDD流程中涉及的所有慨念
1.功能测试
2.单元测试
3.单元测试/编写代码 循环
4.重构
"""