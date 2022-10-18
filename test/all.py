import os

import pytest

if __name__ == '__main__':
    pytest.main(['-sv'])

    #os.system('allure generate ./temp -o ./reports  --clean')