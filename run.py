import pytest,time
from utils.Toolbar import Toolbar




if __name__ == "__main__":
    pytest.main(['-s', '--alluredir', './report/result/'])
    time.sleep(1)

    Toolbar.exec_allure_script('./report/result', './report/html')