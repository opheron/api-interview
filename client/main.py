import pprint as pp

from client import LoanStreetClient

if __name__ == "__main__":

  client = LoanStreetClient()

  params = {
    'amount': 5203.01,
    'interest_rate': 1.01,
    'loan_length_months': 30,
    'monthly_payment_amount': 5.43
  }

  update_params = {
    'id': 1,
    'amount': 2.01,
    'interest_rate': 1.01,
    'loan_length_months': 30,
    'monthly_payment_amount': 5.43
  }


  # result = pp.pprint(client.get_all_loans())

  # result = client.create_loan(params)
  # result = client.update_loan(update_params)
  # result = client.get_all_loans()
  result = client.get_loan(1)

  pp.pprint(result)