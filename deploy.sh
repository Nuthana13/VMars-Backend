#!/bin/bash

# Exit on error
set -e

# Update system
echo "Updating system..."
sudo apt-get update
sudo apt-get upgrade -y

# Install required packages
echo "Installing required packages..."
sudo apt-get install -y python3 python3-pip python3-venv nginx

# Create project directory
echo "Creating project directory..."
sudo mkdir -p /var/www/vmarsbio
sudo chown -R $USER:$USER /var/www/vmarsbio

# Create and activate virtual environment
echo "Setting up Python virtual environment..."
python3 -m venv /var/www/vmarsbio/venv
source /var/www/vmarsbio/venv/bin/activate

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Create Gunicorn service file
echo "Creating Gunicorn service..."
sudo tee /etc/systemd/system/vmarsbio.service << EOF
[Unit]
Description=Gunicorn instance to serve vmarsbio
After=network.target

[Service]
User=$USER
Group=www-data
WorkingDirectory=/var/www/vmarsbio
Environment="PATH=/var/www/vmarsbio/venv/bin"
ExecStart=/var/www/vmarsbio/venv/bin/gunicorn --workers 3 --bind unix:vmarsbio.sock -m 007 app:app

[Install]
WantedBy=multi-user.target
EOF

# Create Nginx configuration
echo "Creating Nginx configuration..."
sudo tee /etc/nginx/sites-available/vmarsbio << EOF
server {
    listen 80;
    server_name vmarsbio.com www.vmarsbio.com;

    location / {
        include proxy_params;
        proxy_pass http://unix:/var/www/vmarsbio/vmarsbio.sock;
    }

    location /static {
        alias /var/www/vmarsbio/static;
    }
}
EOF

# Enable Nginx site
echo "Enabling Nginx site..."
sudo ln -s /etc/nginx/sites-available/vmarsbio /etc/nginx/sites-enabled
sudo rm -f /etc/nginx/sites-enabled/default

# Set up SSL with Certbot
echo "Setting up SSL..."
sudo apt-get install -y certbot python3-certbot-nginx
sudo certbot --nginx -d vmarsbio.com -d www.vmarsbio.com

# Start and enable services
echo "Starting services..."
sudo systemctl start vmarsbio
sudo systemctl enable vmarsbio
sudo systemctl restart nginx

echo "Deployment completed successfully!"
echo "Your website should now be accessible at https://vmarsbio.com" 