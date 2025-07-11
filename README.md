**Powerplant Production Plan API**

This project is a submission for the technical challenge: [https://github.com/gems-st-ib/powerplant-coding-challenge](https://github.com/gems-st-ib/powerplant-coding-challenge)It implements a REST API in Python that calculates the optimal distribution of load among different power plants (gas, wind turbines, jets...) based on production cost and resource availability.

**Technologies**

*   Python 3.8+
    
*   FastAPI
    
*   Pydantic
    
*   Docker + Docker Compose
    

**Architecture and Structure**

The project follows a small organization based on **Domain-Driven Design (DDD)** and **Hexagonal Architecture** principles.

**Running with Docker**

1.  Clone the repository:
    
`   git clone   cd powerplant_solved   `

1.  Build the container:
    

`   docker-compose build   `

1.  Run the server:
    
`   docker-compose up   `

The API will be available at:[http://localhost:8888](http://localhost:8888/)

You can test it using tools like **Postman** or directly in your browser at:[http://localhost:8888/docs](http://localhost:8888/docs)