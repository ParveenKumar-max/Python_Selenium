Feature: Order Transactions
  Test related to Order Transactions

  Scenario Outline: Verify the Order Success Message in details page
    Given Enter the <Username> and <Password>
    And Place the Order with same credentials
    When I logged with <Username> and <Password> in portal
    And Naviagte to the Order page
    Then Select the Order and placed the different Order
    And Order Success message is successfully displayed on page
    Examples:
      | Username                | Password |
      | parveendogra2@gmail.com | Qwerty12345@ |
      | pintudogra@gmail.com    | Pintudogra@123 |