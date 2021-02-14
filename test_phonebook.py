import pytest
from phonebook import PhoneBook


@pytest.fixture
def phonebook(tmpdir):
    "Provides and empty Phonebook"
    return PhoneBook(tmpdir)

# @pytest.fixture
# def phonebook(): return PhoneBook()


#@pytest.mark.skipif(sys.version_info < (3,6),reason="requires python3.6 or higher")
def test_lookup_by_name(phonebook):
    phonebook.add("Bob", "1234")
    assert "1234" == phonebook.lookup("Bob")

@pytest.mark.skip("WIP")
def test_phonebook_contains_all_names(phonebook):
    phonebook.add("Bob", "1234")
    assert "Bob" in phonebook.names()
    #assert phonebook.names() == {"Bob"}

def test_missing_name_raises_error(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("Bob")