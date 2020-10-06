# -*- coding: utf-8 -*-
"""
Represents a margin object.
"""

class PlatformMargin:

    def __init__(self, category, funds, utilized, \
        available, pseudoAccount, tradingAccount, \
        stockBroker):

        self.category = category
        self.funds = funds
        self.utilized = utilized
        self.available = available
        self.pseudo_account = pseudoAccount
        self.trading_account = tradingAccount
        self.stock_broker = stockBroker

    def __str__(self):
        return ("Margin[Pseudo Acc: {0}, Trading Acc: {1}, Broker: {2}, "
            "Category: {3}, Funds: {4}, Utilized: {5}, Available: {6}]").format( \
            self.pseudo_account, self.trading_account, self.stock_broker, \
            self.category, self.funds, self.utilized, self.available)
