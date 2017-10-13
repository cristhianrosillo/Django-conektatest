from __future__ import unicode_literals

from django.db import models
from django.conf import settings
import conekta
import json

class Sale(models.Model):
    def __init__(self, *args, **kwargs):
        super(Sale, self).__init__(*args, **kwargs)

        conekta.api_key = settings.CONEKTA_PRIVATE_KEY
        conekta.api_version = "2.0.0"

    def crear_custumer(self, token_id):
        try:

          customer = conekta.Customer.create({
            'name': 'Cristhian Rosillo',
            'email': 'cristhian@conekta.com',
            'phone': '52181818181',
            'payment_sources': [{
              'type': 'card',
              'token_id': token_id,
            }]
          })

          return (self.genera_order(customer.id))
        except conekta.ConektaError as e:
          print (e.message)

    def genera_order (self, customer_var):
        try:
          orden = conekta.Order.create({
                "line_items": [{
                  "name": "Burro",
                  "unit_price": 200000,
                  "quantity": 1,
                }],

              "currency":"MXN",
              "customer_info": {
                "customer_id": customer_var,
                },

                "shipping_contact": {
                  "receiver": "Sancho Panza",
                  "phone": "1234567890",
                  "address": {
                    "street1": "Street",
                    "city":"Algun lugar de la Mancha",
                    "state":"Toledo",
                    "postal_code":"ZIP 123",
                    "country":"Espana",
                  }
                },
                "shipping_lines": [{
                    "carrier":"McFly",
                    "method":"Time Tavel Service",
                    "amount": 100000,
                    "tracking_number":"sdrhb2343",
                  }],

              "charges": [{
                  "payment_method": {
                    "type": "default"
                  }
              }]
            })

          return (orden.payment_status + "  $" + str(orden.amount/100) + orden.currency + "<br> <br> Numero de Orden: " + orden.id + "  <br> ID usuario creado: " + customer_var)
        except conekta.ConektaError as e:
          print e.error_json['message']
