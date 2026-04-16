-- Last updated: 4/16/2026, 12:55:25 AM
# Write your MySQL query statement below
SELECT Person.firstName, Person.lastName, Address.city, Address.state
FROM Person
LEFT JOIN Address ON Person.personId = Address.personId;