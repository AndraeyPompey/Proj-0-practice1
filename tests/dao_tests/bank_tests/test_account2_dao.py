from custom_exceptions.no_acc_found import NoAccountFound
from data_access_layer.bank_dao.account2_dao_imp import Account2DaoImp
from entities.account_class2 import Account2

account2_dao = Account2DaoImp()

def test_create_account_success():
    account = Account2(0, -2, 500.00)
    result = account2_dao.create_account(account)
    assert result.account2_id != 0

def test_create_account_string_id():
    account = Account2("dog", -2, 500.00)
    result = account2_dao.create_account(account)
    assert result.account2_id != 0

def test_get_account_by_id_success():
    result = account2_dao.get_account_by_account_id(-3)
    assert result.account2_id == -3

def test_get_account_by_nonexistent_id():
    try:
        account2_dao.get_account_by_account_id(0)
        assert False
    except NoAccountFound as e:
        assert str(e) == "No account matches the Id given. try again"

def test_get_account_using_string():
    try:
        account2_dao.get_account_by_account_id("fish")
        assert False
    except NoAccountFound as e:
        assert str(e) == "No account matches the Id given. try again"

def test_get_all_accounts_by_customer_id_success():
    accounts = account2_dao.get_all_accounts_by_customer_id(-2)
    assert len(accounts) >= 2

def test_get_all_accounts_by_nonexistent_customer_id():
    try:
        account2_dao.get_all_accounts_by_customer_id(-1000)
        assert False
    except NoAccountFound as e:
        assert str(e) == "No account matches the Id given. try again"

def test_get_all_accounts_using_string():
    try:
        account2_dao.get_all_accounts_by_customer_id("CornCob")
        assert False
    except NoAccountFound as e:
        assert str(e) == "No account matches the Id given. try again"

def test_update_account_by_account_id_success():
    new_info = Account2(-100,-10,200.00)
    result = account2_dao.update_account_by_account_id(new_info)
    assert result.balance2 == 200.00

    # new_account = Account2(-7,-2, 200.00)
    # return account2_dao.update_account_by_account_id(new_account)

def test_update_account_with_invalid_id():
    try:
        new_info = Account2(-10009990, -10, 200.00)
        account2_dao.update_account_by_account_id(new_info)
        assert False
    except NoAccountFound as e:
        assert str(e) == "No account matches the Id given. try again"

def test_transfer_money_success():
    result = account2_dao.transfer(-101,-102,100.00)
    assert result

def test_transfer_money_nonexistent_sender_id():
    try:
        account2_dao.transfer(-100098,102, 100.00)
        assert False
    except NoAccountFound as e:
        assert str(e) == "No account matches the Id given. try again"

def test_transfer_money_nonexistent_receiver_id():
    try:
        account2_dao.transfer(-101,-10210, 100.00)
        assert False
    except NoAccountFound as e:
        assert str(e) == "No account matches the Id given. try again"

def test_delete_account_by_account_id_success():
    result = account2_dao.delete_account_by_id(-115)
    assert result

def test_delete_account_nonexistent_id():
    try:
        account2_dao.delete_account_by_id(-987976865)
        assert False
    except NoAccountFound as e:
        assert str(e) == "No account matches the Id given. try again"


