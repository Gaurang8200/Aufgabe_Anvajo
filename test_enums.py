from src.section_enums import Label, Sample


def test_sample():
    """
    SPECIFICATION: the sample provides the volume in m³ and liters

    ASSUMPTION: implementation is correct
    TASK: patch the test
    """
    sample = Sample("New", 123.4)
    assert sample.volume__m3 == 123.4
    #assert sample.volume__l == 123.4*2e3
    assert sample.volume__l == 123.4*1e3 
    # Explain: Correct conversion factor (1e3)
    


def test_labels():
    """
    ASSUMPTION: implementation is correct
    TASK: patch the test
    """
    #sample = Sample("New", 123.4, Label.FULL) 
    sample = Sample("New", 123.4, Label.FULL.value)
    assert sample.label == Label.FULL.value

'''
Explain: 'sample.label' doesn't Provide the value but it provide an enum member (Label.FULL).
So i can change assert and compare the Memeber instead of integer or i can change the sample.
I decide to change the sample() and then compare the value instead of 'Lebel.Full' Enum member.

'''