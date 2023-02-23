SELECT users.bounded_mean(
  TO_JSON(
    ARRAY((SELECT TotalPurchases FROM users.purchases))
  )
)