<!-- PRINTING PORTAL -->
# Forex Microservices 

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#installation">Running The App</a></li>
        <li><a href="#installation">Running Unit Tests</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap / Kanban Board</a></li>
    <li><a href="#roadmap">Database Design</a></li>
    <li><a href="#roadmap">Test Coverage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project was created as a proof of concept for Microservices system architecture 
and to demonstrate a simple CI/CD pipeline for automatic testing and building and deployment of a Docker Swarm network.

The project utilises Jenkins for CI/CD and a nginx VM to assure load balancing/ providing a reverse proxy to the Manager/Workers 
Docker Swarm Network.

The application simulations a Forex (currency exchange rate) data-stream, pulling archived EUR/USD from a database and 
applying statistical math processes before finally rendering the data into a plot figure for the user. 

### Built With

* Flask
* SQLAlchemy, MySQL
* Pandas, MatPlotLib, MPLFinance




<!-- ROADMAP -->
## Roadmap / Kanban Board

This app was developed with an agile approach, the roadmap and kanban board can be found in the 
[projects section](https://github.com/users/OrigamiCranes/projects/1) on the github repo.

<!-- MICROSERVICES -->
## MicroServices

The application split into four services; Front-end, Back-end, Stream & Mathy. 

* Front-end renders the webpage and 
figure plot and is the interaction-end for user. 

* Back-end is called by Front-end to grab a data-block from Stream and process it through Mathy.

* Stream grabs the defined data-block size randomly from the database and returns all the values via JSON to Back-end.

* Mathy recieves the Stream data-block via Back-end and calculates the moving average (variable), then returns only the moving average via JSON to Back-end.

* Back-end merges the data-block and math-block into one single JSON item and returns the value to the front-end.


<!-- DATABASE DESIGN -->
## Database Design

The Database uses data gathered via MetaTrader5 for EURUSD trading data from the Dec 2020 period.
<!-- TEST COVERAGE -->
## Test Coverage
The unit testing assures that all routes are accessible, all database CRUD functions are working correctly and that any error values do not corrupt the database. 

Mock tests were utilised to test the requests/api calls where JSON data was required.



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Jack McKeon - coding@jackmckeon.co.uk

Project Link: [https://github.com/OrigamiCranes/microservices](https://github.com/OrigamiCranes/microservices)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* QA Academy DevOps Fundamental Project

