CREATE OR REPLACE FUNCTION `users.bounded_mean`(purchase_totals JSON) RETURNS FLOAT64
REMOTE WITH CONNECTION `us.bounded-mean`
OPTIONS (
  endpoint = ''
)