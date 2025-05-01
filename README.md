# VmarsBio Pharma Website

This is the official website for VmarsBio Pharma, featuring a modern design and contact form functionality.

## Setup Instructions

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure email settings:
   - Update the `EMAIL_USER` and `EMAIL_PASS` variables in `app.py` with your Gmail credentials
   - Make sure to use an App Password if you have 2-factor authentication enabled

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to `http://localhost:5000`

## Features

- Modern, responsive design using Bootstrap 5
- Contact form with email functionality
- Smooth scrolling navigation
- Mobile-friendly layout

## Technologies Used

- Flask (Python web framework)
- Bootstrap 5 (Frontend framework)
- SMTP (Email functionality)
- HTML5/CSS3/JavaScript 