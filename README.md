# Self-Assessment Questionnaire Application

A comprehensive Flask-based web application for managing and conducting student self-assessment questionnaires. This tool helps students evaluate their academic skills across multiple areas and provides personalized feedback for improvement.

![Application Screenshot](docs/screenshots/dashboard.png) *(Screenshot to be added)*

## Overview

This application provides a structured way for students to assess their academic capabilities through a 60-question survey. The system automatically analyzes responses and generates detailed feedback across ten key academic areas, helping students identify their strengths and areas for improvement.

### Assessment Areas

The questionnaire evaluates students across 10 key areas:

1. **Motivation** - Evaluates drive and commitment to academic goals
2. **Academic Resource Usage** - Measures how effectively students use available resources
3. **Information Processing** - Assesses ability to understand and retain information
4. **Time Management** - Evaluates planning and organizational skills
5. **Test Strategies** - Assesses approach to exams and evaluations
6. **Concentration** - Measures focus and attention during study
7. **Main Concept Selection** - Evaluates ability to identify key information
8. **Attitude** - Assesses general approach to academic work
9. **Self-Monitoring** - Measures self-awareness in learning process
10. **Anxiety Management** - Evaluates stress handling in academic situations

## Features

- User authentication system
- Interactive questionnaire with 60 questions
- Automatic score calculation for 10 different assessment areas
- Administrative dashboard
- PDF report generation
- Excel export functionality
- Feedback system based on score clusters

## Requirements

- Python 3.8 or higher
- SQLite3
- Modern web browser

## Installation

### Using Python venv

1. Clone the repository and navigate to the project directory:
```bash
git clone <repository-url>
cd Questionario-LF
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
# or
venv\Scripts\activate  # On Windows
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

### Using Conda

1. Clone the repository and navigate to the project directory:
```bash
git clone <repository-url>
cd Questionario-LF
```

2. Create and activate a Conda environment:
```bash
conda create -n questionario python=3.8
conda activate questionario
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Configuration

The application uses SQLite as its database. By default, it will create a `valutazioni.db` file in the project root directory.

### Initial Setup

1. After installation, change the default SECRET_KEY in `questionario_app.py`:
```python
app.config['SECRET_KEY'] = 'your_secure_secret_key_here'
```

2. Default admin credentials (change immediately after first login):
- Username: admin
- Password: admin123

### Changing Admin Password

1. Log in with the default credentials
2. Go to the admin dashboard
3. Navigate to the user settings section
4. Update your password

## Running the Application

1. Make sure your virtual environment is activated

2. Run the Flask application:
```bash
python questionario_app.py
```

3. Access the application in your web browser at:
```
http://localhost:5005
```

## Application Structure

- `questionario_app.py`: Main application file
- `models.py`: Database models
- `requirements.txt`: Python package dependencies
- `templates/`: HTML templates
  - `admin/`: Administrative interface templates
  - Other template files for user interface

## Administrator Guide

### Dashboard Features

- View all questionnaire submissions
- Generate individual and aggregate reports
- Export data to Excel
- Manage feedback clusters
- Configure question settings

### Managing Feedback Clusters

1. Access the admin dashboard
2. Navigate to "Gestione Clusters"
3. Add/Edit/Delete feedback clusters for each assessment area
4. Set score ranges and corresponding feedback text

### Data Export

1. From the admin dashboard, select "Export Data"
2. Choose between:
   - Full data export (Excel)
   - Individual reports (PDF)
   - Aggregate statistics

## User Guide

### Taking the Assessment

1. Access the application through your web browser
2. No login required for taking the assessment
3. Answer all 60 questions honestly
4. Submit the form to receive immediate feedback
5. Download or print your personalized report

### Understanding Your Results

- Scores are calculated for each of the 10 assessment areas
- Each area receives a score from 1.0 to 5.0
- Detailed feedback is provided based on score ranges
- Specific improvement suggestions are included for each area

## Database Management

The application uses Flask-Migrate for database migrations. After making any changes to the database models:

1. Initialize migrations (first time only):
```bash
flask db init
```

2. Create a new migration:
```bash
flask db migrate -m "Migration description"
```

3. Apply the migration:
```bash
flask db upgrade
```

## Troubleshooting

### Database Issues

1. If you encounter database errors:
   ```bash
   rm valutazioni.db
   rm -rf migrations/
   flask db init
   flask db migrate -m "fresh start"
   flask db upgrade
   ```

2. Restart the application:
   ```bash
   python questionario_app.py
   ```

### Common Issues

1. **Migration Errors**
   - Ensure all models are properly imported
   - Delete `migrations` folder and reinitialize if needed
   - Check database connection string

2. **Login Issues**
   - Clear browser cache and cookies
   - Reset admin password using SQLite command line
   - Check database permissions

3. **Report Generation Errors**
   - Verify all required Python packages are installed
   - Check write permissions in the application directory
   - Ensure proper encoding settings

## Security Notes

1. In Production:
   - Change the default admin password immediately
   - Update the SECRET_KEY in the application configuration
   - Enable HTTPS
   - Set up proper firewall rules
   - Configure secure headers
   - Enable logging
   - Regular security updates

2. Recommended Security Measures:
   - Use strong passwords
   - Regular database backups
   - Monitor access logs
   - Implement rate limiting
   - Configure CORS properly

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please ensure your PR:
- Follows the existing code style
- Includes appropriate tests
- Updates documentation as needed
- Describes the changes made

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Flask framework and its contributors
- SQLAlchemy team
- All contributors to this project

For additional support, please check the application logs or open an issue on GitHub.