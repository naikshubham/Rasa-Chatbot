from rasa_sdk import Action

class ActionSharePrice(Action):
    """custom action to return share price from alphavantage""""
    def name(self) -> Text:
        return "action_shareprice"

    def fetchprice(self):
        