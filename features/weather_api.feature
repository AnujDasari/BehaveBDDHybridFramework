Feature: Weather API Automation

  @api
  Scenario: Verify GET call for current weather api
    When User sends "GET" call to endpoint "current.json" with city as "Bengaluru"
    Then User verifies the status code is "200"
    And User verifies GET response contains following information
      | name      | region    | country |
      | Bengaluru | Karnataka | India   |