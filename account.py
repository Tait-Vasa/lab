class Account:
    def __init__(self, name : str) -> None :
        '''
        This is init function
        :param name of the account
        '''
        self.__name = name
        self.__account_balance = 0

    def deposit(self, amount : float) -> bool:
        '''
        This is the deposit function add money to an account
        :param amount: this is amount selected to be put in
        :return: returns if the function deposited or not
        '''

        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False


    def withdraw(self, amount: float) -> bool:
        '''
        This is the deposit function add money to an account
        :param amount: this is amount selected to be taken out
        :return: returns if the function withdrew or not
        '''
        if self.__account_balance > amount and amount > 0:
            self.__account_balance -= amount
            return True

        else:
            return False


    def get_balance(self) -> float:
        '''
        This displays the account balance.
        :return: returns the amount in the account
        '''
        return self.__account_balance

    def get_name(self) -> str:
        '''
        This function displays the name of the account.
        :return: returns the account name
        '''
        return self.__name