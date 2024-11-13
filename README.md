# Inventory Management Application

This Django-based inventory management application allows users to efficiently manage inventory items, categorize them, and receive alerts for low inventory levels. It features a responsive, user-friendly interface and is deployed on Heroku.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Database Setup](#database-setup)
  - [Environment Variables](#environment-variables)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Documentation](#api-documentation)
- [Deployment on Heroku](#deployment-on-heroku)
- [Testing](#testing)
- [License](#license)

---

## Features

- User registration, login, and logout functionality.
- Inventory management with quantity tracking and category organization.
- Low inventory alerts on the dashboard.
- Full CRUD (Create, Read, Update, Delete) operations on inventory items.
- Responsive UI built with Bootstrap and enhanced with Django Crispy Forms for optimized form rendering.

## Technologies Used

- **Backend**: Python, Django
- **Frontend**: HTML, CSS (Bootstrap 5), Django Crispy Forms
- **Database**: SQLite (development), PostgreSQL (production on Heroku)
- **Deployment**: Heroku
- **APIs**:
  - **Django Crispy Forms**: Simplifies form layout and Bootstrap integration.
  - **Bootstrap 5**: Provides a modern, responsive design.

## Getting Started

### Prerequisites

- Python 3.x
- Git
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) (for deployment)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd inventory_management
## Database Setup
- By default, this application uses SQLite for local development. For production, it is configured to use PostgreSQL on Heroku.

## Environment Variables
1. Create a .env file in the root directory and include the following configurations:
- SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=postgres://<user>:<password>@<hostname>:<port>/<database>  # For Heroku PostgreSQL
LOW_QUANTITY=5  # Customize the threshold for low inventory alerts

