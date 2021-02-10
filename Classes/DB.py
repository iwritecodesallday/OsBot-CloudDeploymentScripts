import psycopg2
import random


class DB(object):
    def __init__(self, config):
        self.conn = psycopg2.connect(
            host=config['DB']['host'],
            port=config['DB']['port'],
            database=config['DB']['database'],
            user=config['DB']['user'],
            password=config['DB']['password']
        )
        self.cur = self.conn.cursor()

    def check_for_available_accounts(self):
        """

        @param: self
        """
        print("Locating all available accounts")
        self.cur.execute(
            # Code to check the Accounts table for available accounts (column: Available[Boolean])
            " \
                SELECT * FROM dbo.\"osrs\" \
                WHERE \"available\" = true \
            "
        )

        results = self.cur.fetchall()

        account_id, email, password, available, proxy, character = results[random.randint(0, len(results) - 1)]

        return account_id, email, password, proxy
        # Todo: Check Account Activity

    def set_account_availability(self, account_id, available):
        self.cur.execute(
            "\
                UPDATE dbo.\"Accounts\" \
                SET \"available\" = {}\
                WHERE \"id\" = '{}'\
            ".format(available, account_id)
        )
        self.conn.commit()

    def log_activity(self, acc_id, activity, target):
        self.cur.execute("\
                         INSERT INTO dbo.\"Activity\"(account_id, action, target) \
                             VALUES ('{}', '{}', '{}') \
                         ".format(acc_id, activity, target))
        self.conn.commit()


def convert(tup, di):
    for a, b, c in tup:
        di.setdefault(b, [c])
    return di
