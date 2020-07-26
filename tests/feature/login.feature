Feature: Login 


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
    Then the correct error message Invalid password. should be displayed

Scenario: unsuccessful Login into user account
    Given I am currently at login page
    when submit login form
    Then the correct error message An email address required. should be displayed    