from pathlib import Path

from src.section_data import DataStructureDemo, format_string

def test_add_item():
    """
    SPECIFICATION: add_item shall create a backup of 'items', which is then
    available under 'items_backup'

    ASSUMPTION: implementation is wrong and the backup is not created correctly
    TASK: patch the implementation
    HINT: special behavior of python dict/list
    """
    demo = DataStructureDemo()
    demo.add_item(1)
    assert len(demo.items) > len(demo.items_backup)


def test_set_item():
    """
    SPECIFICATION: 'set_item' shall set the given key-value-pair to 'data'.

    ASSUMPTION: test is correct
    TASK: patch the implementation
    """
    demo = DataStructureDemo()
    demo.set_item("example", 22)
    assert demo.data["example"] == 22


def test_transform_items():
    """
    SPECIFICATION: 'transform_items' shall return a subsection of
    the upper characters of 'items'

    ASSUMPTION: test is wrong
    TASK: patch the test


    Second TODO:
    Parametrize this test to not just run with "a"-"d", but also with other combinations
    Use the pytest-parametrize feature.
    """
    demo = DataStructureDemo(items=["a", "b", "c", "d"])
    result = demo.transform_items(start_index=2)
    assert result == ["C", "D"]  
    ''' Explain: assert result == ["b", "c"] was orginally, but i think it is 
    Wrong comparision according to the Index and result after Format of method.
    i can't change the transform_item() due to Task of patching the test only and
    thats why can'change the start_index and so i have to change the assert.
    '''



def test_string_formatting():
    """
    SPECIFICATION: 'format_string' returns an identical string,
    once formatted using %-formatting, once using f-string-formatting

    ASSUMPTION: assume the test is correct
    TASK: patch the implementation
    """
    old_style, new_style = format_string("John", 30)
    assert old_style == "Name: John, Age: 30"
    assert new_style == "Name: John, Age: 30"


def test_get_evaluation():
    """
    SPECIFICATION: 'get_evaluation' shall return
    - 'Large' for values > 100
    - 'Negative' for values <= 0
    - 'Normal' for values inbetween

    ASSUMPTION: assume the test is correct
    TASK: patch the implementation
    """
    demo = DataStructureDemo()
    assert demo.get_evaluation(150) == "Large"
    assert demo.get_evaluation(0) == "Negative"
    assert demo.get_evaluation(50) == "Normal"


def test_get_evaluation_2():
    """
    ASSUMPTION:
    - implementation is correct
    - test is poorly defined

    TASK: explain why the test is failing
    HINT: special behavior of python class attributes
    """
    demo_1 = DataStructureDemo() #object 1
    demo_2 = DataStructureDemo() #object 2

    assert demo_1.get_evaluation(102) == "Large"
    assert demo_2.get_evaluation(102) == "Large"

    demo_1.BOUNDARY_HIGH = 103
    assert demo_1.get_evaluation(102) == "Normal"
    assert demo_2.get_evaluation(102) == "Large"

    DataStructureDemo.BOUNDARY_HIGH = 103 #EXPLAIN: This modifies the class attribute BOUNDARY_HIGH = 103, That's why it's Shows Normal instead Large.
    assert demo_1.get_evaluation(102) == "Large"
    assert demo_2.get_evaluation(102) == "Large"

    '''Explain: The test fails due to Python’s class and instance attribute behavior. 
    Class attributes are shared across instances unless overridden.
    Instance attributes do not affect the class attribute, which is DataStructureDemo().
    If an instance variable is created with the same name as a class attribute, it shadows the class attribute for that instance only.'''

def test_file_operations(tmp_path: Path):
    """
    SPECIFICATION: 'write_data' and 'read_data' shall lead
    to unmodified data

    ASSUMPTION: assume the test is correct
    TASK:  patch the implementation
    """
    demo = DataStructureDemo()
    filepath = tmp_path / "test.json"
    testdata = {"testkey": "testvalue"}
    demo.data.update(testdata)
    demo.write_data(filepath)
    demo.read_data(filepath)
    assert demo.data == testdata


def test_file_operation_local():
    """
    SPECIFICATION: 'write_data' and 'read_data' shall lead
    to unmodified data

    ASSUMPTION: assume the test and the implementation is correct
    TASK: Use a pytest fixture to specify the filepath.
    Use it in this test, and cleanup after the test has finished.
    The test will fail if the file already exists upon start.
    Therefore the file should (at least) be removed before the test is started.
    Use a pytest fixture for this.
    """
    demo = DataStructureDemo()
    filepath = Path("test.json")
    testdata = {"testkey": "testvalue"}
    demo.data.update(testdata)

    assert not filepath.exists()
    demo.write_data(filepath)

    assert filepath.exists()
