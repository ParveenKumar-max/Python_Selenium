Feature: Order Transactions
  Test related to Order Transactions

  Scenario Outline: Verify the Order Success Message in details page
    Given Enter the <Username> and <Password> and place the order
    When I logged with <Username> and <Password> in portal
    And Navigate to the Order page
    Then Select the Order and fill all the required details
    And Order Success message is successfully displayed on page

    Examples:
      | Username                 | Password       |
      | parveendogra2@gmail.com  | Qwerty12345@   |
      | pintudogra@gmail.com     | Pintudogra@123 |