import allure
import pytest


def test_with_no_seversity_label():
    pass

@allure.severity(allure.severity_level.TRIVIAL)
def test_with_trivial_severity():
    pass

@allure.severity(allure.severity_level.NORMAL)
def test_with_normal_severity():
    pass

@allure.severity(allure.severity_level.NORMAL)
class TestClassWithNormalSeversity(object):

    def test_inside_the_normal_seversity_test_case(self):
        pass

    @allure.severity(allure.severity_level.CRITICAL)
    def test_inside_the_normal_seversity_test_class_with_overriding_critical_secersity(self):
        pass

if __name__ == '__main__':
    pytest.main()

