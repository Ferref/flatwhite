import os

def create_project_structure(project_type='php'):
    if project_type == 'php':
        # Define the folder structure for a PHP project
        folders = [
            "project-root/assets/css",
            "project-root/assets/images",
            "project-root/assets/js",
            "project-root/includes",
            "project-root/sql",
            "project-root/templates"
        ]
        
        # Define the files to be created for a PHP project
        files = {
            "project-root/assets/css/styles.css": "",
            "project-root/assets/images/logo.png": "",
            "project-root/assets/js/scripts.js": "",
            "project-root/includes/header.php": "",
            "project-root/includes/footer.php": "",
            "project-root/includes/config.php": "",
            "project-root/sql/database.sql": "",
            "project-root/templates/index.php": "",
            "project-root/templates/about.php": "",
            "project-root/templates/contact.php": "",
            "project-root/.gitignore": "",
            "project-root/README.md": "",
            "project-root/index.php": "",
            "project-root/.htaccess": ""
        }
        
        # Create the folders
        for folder in folders:
            os.makedirs(folder, exist_ok=True)
        
        # Create the files
        for file_path, content in files.items():
            with open(file_path, 'w') as file:
                file.write(content)
        
        print(f"{project_type.capitalize()} project folder structure created successfully.")
    else:
        print(f"Project type '{project_type}' is not supported.")

# Example usage
create_project_structure('php')
