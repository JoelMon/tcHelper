"""
Tests for the *scr/tchelper* module

"""

from unittest import mock
import pytest
import scr.tchelper


@pytest.mark.parametrize('value, expected_value', [
        (True, True),
        (False, False)
])
@mock.patch('scr.tchelper.yam.set_value')
def test_set_first_run(mock_set_value, value, expected_value):
    """Test for set_first_run function"""

    scr.tchelper.set_first_run(value)
    assert mock_set_value.called
    mock_set_value.assert_called_with('first_run', expected_value)


@pytest.mark.parametrize('value, expected', [(True, True),
                                             (False, False)
                                             ])
@mock.patch('scr.tchelper.yam.get_value')
def test_check_first_run(mock_get_value, value, expected):
    """Tests the check_first_run function"""

    mock_get_value.return_value = value
    result = scr.tchelper.check_first_run()
    mock_get_value.assert_called_with('first_run')
    assert result == expected
