import json
import logging

import allure
import pytest
import time
from utils.HttpSender import HttpSender
from utils.Toolbar import Toolbar


class TestHttp(HttpSender):
    case_data = HttpSender.getCaseData('TestHttpBin_get')

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.parametrize("case_name, url, method, params, data, headers, assert_type, assert_text, case_desc",
                             argvalues=case_data)
    def test_http(self, case_name, url, method, params, data, headers, assert_type, assert_text, case_desc):

        res = self.send_http_request(
            url=url, method=method, params=params, data=data, headers=headers)

        self.log.info(self.return_curl(res.request))
        self.log.info(res.json())
        self.log.info(res.status_code)


        if assert_type == 'status_code':
            self.assert_util.assert_code(assert_text, res.status_code)
        if assert_type == 'assert_in_body':
            self.assert_util.assert_in_body(res.json(), assert_text)




        # allure
        allure.dynamic.title(case_name)
        allure.dynamic.story(case_name)
        allure.dynamic.feature(__name__)
        with open('./utils/allrue_log_template.txt', 'r') as f:
            allure.dynamic.description(

                f.read().format(self.return_curl(res.request), json.dumps(res.json(), indent=4), str(res.status_code),
                                assert_type, assert_text))


if __name__ == "__main__":
    pytest.main(['-s', '--alluredir', '../report/result/','TestHttpBin.py'])
    time.sleep(1)

    Toolbar.exec_allure_script('../report/result', '../report/html')
    #       判断xx为真 assert xx
    #       判断xx不为真 assert not xx
    #       判断b包含a  assert a in b
    #       判断a等于b  assert  a == b
    #       判断a不等于b assert a != b


