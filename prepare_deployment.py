import os
import shutil
import zipfile
from pathlib import Path

def create_directory_structure():
    """Create the necessary directory structure."""
    directories = [
        'static/images',
        'static/css',
        'static/js',
        'templates'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

def move_images():
    """Move all images to static/images directory."""
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.svg')
    
    # Move images from root and other directories
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.lower().endswith(image_extensions):
                src = os.path.join(root, file)
                dst = os.path.join('static/images', file)
                if src != dst:
                    shutil.move(src, dst)

def create_zip():
    """Create a deployment-ready ZIP file."""
    files_to_zip = [
        'app.py',
        'requirements.txt',
        'deploy.sh',
        'README.md',
        'static',
        'templates'
    ]
    
    with zipfile.ZipFile('vmarsbio_deployment.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in files_to_zip:
            if os.path.isfile(file):
                zipf.write(file)
            elif os.path.isdir(file):
                for root, dirs, files in os.walk(file):
                    for f in files:
                        file_path = os.path.join(root, f)
                        arcname = os.path.relpath(file_path, '.')
                        zipf.write(file_path, arcname)

def main():
    print("Preparing project for deployment...")
    
    # Create directory structure
    print("Creating directory structure...")
    create_directory_structure()
    
    # Move images
    print("Moving images to static/images...")
    move_images()
    
    # Create deployment ZIP
    print("Creating deployment ZIP file...")
    create_zip()
    
    print("\nDeployment preparation completed!")
    print("A new file 'vmarsbio_deployment.zip' has been created.")
    print("\nNext steps:")
    print("1. Upload vmarsbio_deployment.zip to your VPS")
    print("2. Follow the deployment instructions in README.md")

if __name__ == '__main__':
    main() 