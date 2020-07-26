Feature: Login 


Scenario: Enter login page
    Given I am currently at home page
    When I click the sign in button
    Then I will be in the login page


Scenario: successful Login into user account
    Given I am currently at login page
    When I tipe a valid e-mail: "admin@test.com"
    And type the corresponding password "admin"
    And submit login form
    Then I will be in the account page


Scenario: unsuccessful Login into user account
    Given I am currently at login page
    When I tipe a valid e-mail: "admin@test.com"
    And type the wrong password "123"
    And submit login form
    Then the correct error message should be displayed

Scenario: unsuccessful Login into user account
    Given I am currently at login page
    when submit login form
    Then the correct error message should be displayed