data={
"user_001": {
    "transactions": [
      {
        "details": {
          "transaction_id": "TXN00001",
          "amount": 123.45,
          "currency": "USD"
        },
        "meta": {
          "timestamp": "2024-04-10T14:22:01",
          "status": "completed",
          "category": "groceries"
        },
        "bank_noise": {
          "bank_code": "BANK_US_001",
          "terminal_id": "TRM1023",
          "merchant_name": "WholeMart City Center"
        }
      },
      {
        "details": {
          "transaction_id": "TXN00002",
          "amount": 89.99,
          "currency": "USD"
        },
        "meta": {
          "timestamp": "2024-06-25T09:11:45",
          "status": "pending",
          "category": "services"
        },
        "bank_noise": {
          "bank_code": "BANK_US_002",
          "terminal_id": "TRM1147",
          "merchant_name": "QuickFix Repairs"
        }
      },
      {
        "details": {
          "transaction_id": "TXN00003",
          "amount": 345.0,
          "currency": "USD"
        },
        "meta": {
          "timestamp": "2024-08-17T18:05:33",
          "status": "completed",
          "category": "electronics"
        },
        "bank_noise": {
          "bank_code": "BANK_EU_008",
          "terminal_id": "TRM2011",
          "merchant_name": "TechStore EU"
        }
      },
      {
        "details": {
          "transaction_id": "TXN00004",
          "amount": 59.1,
          "currency": "USD"
        },
        "meta": {
          "timestamp": "2024-11-03T20:14:27",
          "status": "failed",
          "category": "entertainment"
        },
        "bank_noise": {
          "bank_code": "BANK_US_004",
          "terminal_id": "TRM1455",
          "merchant_name": "MovieZone Downtown"
        }
      },
      {
        "details": {
          "transaction_id": "TXN00005",
          "amount": 210.75,
          "currency": "USD"
        },
        "meta": {
          "timestamp": "2024-12-19T08:47:52",
          "status": "completed",
          "category": "clothing"
        },
        "bank_noise": {
          "bank_code": "BANK_CA_005",
          "terminal_id": "TRM3320",
          "merchant_name": "FashionLoop Toronto"
        }
      }
    ]
  }
}
res = {}
trans = data["user_001"]["transactions"]
for i in trans:
  amount = i["details"]["amount"]
  st = i["meta"]["status"]
  if st not in res:
    res[st] = amount
  else:
    res[st] = res[st] + amount
print(res)
