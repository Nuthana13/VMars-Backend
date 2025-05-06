# VmarsBio Pharma Website

This is the official website for VmarsBio Pharma, built with Flask and Bootstrap.

## Deployment Instructions

### Prerequisites
- Ubuntu-based VPS (e.g., IONOS Cloud Server)
- Domain name (e.g., vmarsbio.com)
- SSH access to your VPS

### Step 1: Prepare Your VPS
1. Connect to your VPS via SSH:
   ```bash
   ssh your_username@your_vps_ip
   ```

2. Update your domain's DNS settings in IONOS:
   - Add an A record pointing to your VPS IP address
   - Add a CNAME record for www subdomain

### Step 2: Deploy the Website
1. Upload the project files to your VPS:
   ```bash
   scp -r website_fb_corrected.zip your_username@your_vps_ip:~/
   ```

2. SSH into your VPS and extract the files:
   ```bash
   ssh your_username@your_vps_ip
   unzip website_fb_corrected.zip -d /var/www/vmarsbio
   ```

3. Make the deployment script executable and run it:
   ```bash
   chmod +x deploy.sh
   ./deploy.sh
   ```

### Step 3: Verify Deployment
1. Visit your domain (https://vmarsbio.com)
2. Test the contact form
3. Check SSL certificate status

### Troubleshooting
If you encounter any issues:

1. Check Gunicorn logs:
   ```bash
   sudo journalctl -u vmarsbio
   ```

2. Check Nginx logs:
   ```bash
   sudo tail -f /var/log/nginx/error.log
   ```

3. Restart services:
   ```bash
   sudo systemctl restart vmarsbio
   sudo systemctl restart nginx
   ```

## Development

### Local Setup
1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the development server:
   ```bash
   python app.py
   ```

### Project Structure
```
vmarsbio/
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── deploy.sh          # Deployment script
├── static/            # Static files
│   ├── css/
│   ├── js/
│   └── images/
└── templates/         # HTML templates
    └── index.html
```

## Contact
For support or questions, contact info@vmarsbio.com

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