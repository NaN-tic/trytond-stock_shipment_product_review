# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool, PoolMeta
from trytond.transaction import Transaction

__all__ = ['ShipmentIn']


class ShipmentIn:
    __metaclass__ = PoolMeta
    __name__ = 'stock.shipment.in'

    @classmethod
    def receive(cls, shipments):
        pool = Pool()
        Date = pool.get('ir.date')
        ProductReview = pool.get('product.review')

        today = Date.today()
        reviews = ProductReview.search([
            ('state', '!=', 'done')
            ])
        reviews = {
            r.product: {
                t.review_type.id for t in reviews if r.product == t.product
                } for r in reviews
            }

        vlist = []
        for shipment in shipments:
            for move in shipment.moves:
                product = move.product
                template = product.template
                if template.review:
                    for review in template.review_types:
                        if product not in reviews:
                            reviews[product] = set([review.id])
                        elif review.id not in reviews[product]:
                            reviews[product].add(review.id)
                        else:
                            continue
                        values = {
                            'product': product.id,
                            'review_type': review.id,
                            'date': today,
                            }
                        vlist.append(values)
        if vlist:
            with Transaction().set_user(0, set_context=True):
                ProductReview.create(vlist)
        super(ShipmentIn, cls).receive(shipments)
