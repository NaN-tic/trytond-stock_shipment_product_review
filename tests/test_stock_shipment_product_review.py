# This file is part of the stock_shipment_product_review module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class StockShipmentProductReviewTestCase(ModuleTestCase):
    'Test Stock Shipment Product Review module'
    module = 'stock_shipment_product_review'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        StockShipmentProductReviewTestCase))
    return suite