Feature: Login Functionality

  @login
  Scenario: Login with valid credentials
    Given User navigated to Login page
    When User enters valid username as "Admin" and password as "7Ac4C@IwIr" into the fields
    And User clicks on Login button
    Then User should get logged in


  @login
  Scenario: Login without entering any credentials
    Given User navigated to Login page
    When User does not enter anything into username and password fields
    And User clicks on Login button
    Then User should see proper warning message under username and password fields
      | username_error_message   | password_error_message   |
      | Username cannot be empty | Password cannot be empty |

  @login-1
  Scenario: Login with invalid credentials
    Given User navigated to Login page
    When User enters invalid username and invalid password into the fields
      | username | password |
      | Admin    | pwd01    |
    And User clicks on Login button
    Then User should get a proper warning message as "Invalid Credentials"


