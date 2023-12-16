# 0x0F. Python - Object-relational mapping

0. 0-select_states.py: A script that lists all states from the database hbtn_0e_0_usa
1. 1-filter_states.py: A script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa
2. 2-my_filter_states.py: A script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument
3. 3-my_safe_filter_states.py: Test "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '" as an input
4. 4-cities_by_state.py: A script that lists all cities from the database hbtn_0e_4_usa
5. 5-filter_cities.py: A script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
6. model_state.py: A python file that contains the class definition of a State and an instance Base = declarative_base()
7. 7-model_state_fetch_all.py: A script that lists all State objects from the database hbtn_0e_6_usa
8. 8-model_state_fetch_first.py: A script that prints the first State object from the database hbtn_0e_6_usa
9. 9-model_state_filter_a.py: A script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa
10. 10-model_state_my_get.py: A script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa
11. 11-model_state_insert.py: A script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
12. 12-model_state_update_id_2.py: A script that changes the name of a State object from the database hbtn_0e_6_usa
13. 13-model_state_delete_a.py: A script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa
14. model_city.py, 14-model_city_fetch_by_state.py: A Python file similar to model_state.py named model_city.py that contains the class definition of a City
15. relationship_city.py, relationship_state.py, 100-relationship_states_cities.py: A script that creates the State “California” with the City “San Francisco” from the database
16. 101-relationship_states_cities_list.py: A script that lists all State objects, and corresponding City objects, contained in the database
17. 102-relationship_cities_states_list.py: A script that lists all City objects from the database

## Usage:

    ./script.py <mysql_username> <mysql_password> <database_name>  

Note: No argument validation is performed in the script.