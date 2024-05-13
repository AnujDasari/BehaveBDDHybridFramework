Feature: Employee Management Functionality

  Background:
    Given User navigated to Login page
    When User enters valid username as "Admin" and password as "7Ac4C@IwIr" into the fields
    And User clicks on Login button
    Then User should get logged in


  @employment_management
  Scenario: Search for an existing employee
    When User clicks on Employee List link
    And User enters valid employee name as "Aaron Hamilton" in the Employee Name search field
    And User clicks on Search icon
    Then Employee details with employee id "1007" should be displayed

  @employment_management
  Scenario: Search for a non-existing employee
    When User clicks on Employee List link
    And User enters non existing employee name as "Abc zyx" in the Employee Name search field
    And User clicks on Search icon
    Then Toast message "No Records Found" should be displayed

  @employment_management
  Scenario Outline: Cancel a Resignation Request
    When User clicks on Request Desk option from the left menu
    And User selects Resignation Request from the Request type dropdown
    And User clicks on Next button
    When User enters resignation reason as "<resignation_reason>"
    And User enters resolution date as "<resolution_date>"
    And User enters resignation date as "<resignation_date>"
    When User clicks on Cancel button
    Then Requests page should be displayed with title as "My Requests"

    Examples:
      | resignation_reason                       | resolution_date | resignation_date |
      | Not satisfied with the salary            | 2024-06-13      | 2024-06-05       |
      | Not satisfied with the work-life balance | 2024-06-15      | 2024-06-15       |