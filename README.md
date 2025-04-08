# NutriBuddy Application

NutriBuddy is a health and wellness application designed to parse user disease history, recommend personalized diets, and provide exercise recommendations. This application leverages **FastAPI** for the backend, **React** for the frontend, and **PostgreSQL** as the database, all orchestrated using **Docker Compose** for seamless deployment.

---

## Features

### Core Functionality
1. **User Management**:
   - Sign up with details like height, weight, gender, dietary preferences, and medical history.
   - Login functionality with secure password hashing.
   - Update profile details (height, weight, disease history).
   - Change password securely.

2. **Disease Parsing & Diet Recommendations**:
   - Uses an LLM service to parse disease history and recommend personalized diets based on user input.

3. **Exercise Recommendations**:
   - Provides personalized exercise recommendations based on user BMI and preferences.
   - Adds variability by randomly selecting exercises from predefined lists for each category to enhance user engagement.

4. **Interactive Dashboard**:
   - View meal and exercise recommendations.
   - Interact with meals (like, dislike, buy) and refresh recommendations.

### Technical Features
- Fully containerized deployment using Docker Compose.
- Backend API with endpoints for user management, disease parsing, diet recommendations, and exercise recommendations.
- Frontend built with React for a seamless user experience.
- PostgreSQL database for storing user data and recommendation results.

---

## Directory Structure

```
nb_dev/
├── backend/                  # FastAPI backend
│   ├── app/
│   │   ├── api/              # API routes
│   │   ├── core/             # Core configurations
│   │   ├── models/           # Database models
│   │   ├── services/         # Business logic (LLM service, recommendation logic)
│   │   └── main.py           # Entry point for FastAPI
├── frontend/                 # React frontend
│   ├── src/
│   │   ├── components/       # React components (e.g., Login, Dashboard)
│   │   ├── pages/            # Application pages
│   │   └── App.tsx           # Main React app file
├── docker-compose.yml        # Docker Compose configuration
├── cleaned_meals.csv         # Dataset for meal recommendations
├── cleaned_exercise.csv      # Dataset for exercise recommendations
├── cleaned_recent_activity.csv # Dataset for user interactions
└── README.md                 # Documentation (this file)
```


---

## Setup Instructions

### Prerequisites

- Docker and Docker Compose installed on your system.
- Node.js (for local frontend development).
- Python 3.10+ (for local backend development).

### Steps to Run the Application

1. **Clone the Repository**:
    ```
    git clone https://github.com/VenkatSR-14/nb_dev.git
    cd nb_dev
    ```

2. **Set Up Environment Variables**:
    Create a `.env` file in the `backend` directory with the following variables:
    ```
    DATABASE_URL=postgresql://postgres:password@db:5432/nutribuddy_db
    SECRET_KEY=your_secret_key_here
    ```

3. **Run the Application with Docker Compose**:
    ```
    docker-compose up --build
    ```
    This will:
    - Start the PostgreSQL database container.
    - Start the FastAPI backend on `http://localhost:8000`.
    - Start the React frontend on `http://localhost:3000`.

4. **Access the Application**:
    - Frontend: [http://localhost:3000](http://localhost:3000)
    - Backend API docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Deliverables

1. **Proposal & Presentation**:
   - Available as PDF and PPT in the repository under `docs/`.

2. **Source Code**:
   - Appropriately commented source code is available in this repository.

3. **Sample Output**:
   - Screenshots of the application are available in the `screenshots/` directory.

4. **Single-Page GitHub Guide**:
   A single-page guide detailing how to set up and use this repository is included in this README under "Setup Instructions."

5. **Discussion of Alternatives**:
   The project could have been approached differently by using other technologies like Flask instead of FastAPI or MongoDB instead of PostgreSQL. These alternatives were not chosen due to performance considerations and compatibility with project requirements.

6. **Incomplete Areas (if any)**:
   Any incomplete areas of the project will be documented in the final proposal along with reasons for incompletion.

---

## PostgreSQL Database Setup

The application uses PostgreSQL as its database management system. The database is managed within a Docker container via Docker Compose.

### Key Points:
- The `docker-compose.yml` file defines a service named `db` for PostgreSQL.
- The database connection string is configured using environment variables (`DATABASE_URL`) in `.env`.
- All migrations or schema updates should be applied via SQLAlchemy models in the backend.

---

## How to Contribute

1. Fork this repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes with descriptive messages.
4. Push your branch to your forked repository.
5. Create a pull request to merge your changes into the main branch.

---

## License

This project is licensed under the MIT License.