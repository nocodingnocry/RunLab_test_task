import pytest

@pytest.fixture()
def set_up():
    #Cюда можно поместить инициализацию браузера
    print("Start test")
    yield
    print('Finish test')

@pytest.fixture()
def set_group():
    #Cюда можно поместить инициализацию браузера
    print("Start system")
    yield
    print('Finish system')