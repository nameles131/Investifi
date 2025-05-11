from src.model import RecurringOrder, User


class DbSetup:
    def run(self):
        self._create_recurring_order_table()
        self._create_user_table()

    def _create_recurring_order_table(self):
        try:
            RecurringOrder.create_table()
        except Exception:
            pass

    def _create_user_table(self):
        try:
            User.create_table()
        except Exception:
            pass


if __name__ == "__main__":
    db_setup = DbSetup()
    db_setup.run()
