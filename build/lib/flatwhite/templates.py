import os

def create_project_structure(project_type='web', includes=None, templates='create'):
    if includes is None:
        includes = ['html', 'js', 'css', 'php', 'sql']
    
    if project_type == 'web':
        # Define the folder structure based on includes
        folders = []
        files = {}
        
        if 'css' in includes:
            folders.append("assets/css")
            files["assets/css/styles.css"] = "" if templates == 'create' else "/* CSS Boilerplate */\nbody { font-family: Arial, sans-serif; }\n"
        
        if 'images' in includes:
            folders.append("assets/images")
            files["assets/images/logo.png"] = ""
        
        if 'js' in includes:
            folders.append("assets/js")
            files["assets/js/scripts.js"] = "" if templates == 'create' else "// JavaScript Boilerplate\nconsole.log('Hello, World!');\n"
        
        if 'php' in includes:
            folders.append("includes")
            files["includes/header.php"] = "" if templates == 'create' else "<?php\n// Header Boilerplate\n?><header>\n    <h1>Header</h1>\n</header>\n"
            files["includes/footer.php"] = "" if templates == 'create' else "<?php\n// Footer Boilerplate\n?><footer>\n    <p>Footer</p>\n</footer>\n"
            files["includes/config.php"] = "" if templates == 'create' else "<?php\n// Config Boilerplate\n?>"
            files["index.php"] = "" if templates == 'create' else "<?php\n// Index PHP Boilerplate\ninclude 'includes/header.php';\n?>\n<h1>Welcome to My Web Project</h1>\n<?php\ninclude 'includes/footer.php';\n?>"
        
        if 'sql' in includes:
            folders.append("sql")
            files["sql/database.sql"] = "" if templates == 'create' else "-- SQL Boilerplate\nCREATE DATABASE my_database;\nUSE my_database;\n"
        
        folders.append("templates")
        files["templates/index.php"] = "" if templates == 'create' else "<!-- Index Template Boilerplate -->\n<h1>Index Page</h1>\n"
        files["templates/about.php"] = "" if templates == 'create' else "<!-- About Template Boilerplate -->\n<h1>About Page</h1>\n"
        files["templates/contact.php"] = "" if templates == 'create' else "<!-- Contact Template Boilerplate -->\n<h1>Contact Page</h1>\n"
        
        files[".gitignore"] = ""
        files["README.md"] = ""
        
        if 'html' in includes:
            files["index.html"] = "" if templates == 'create' else """<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="assets/css/styles.css">
    <script src="assets/js/scripts.js"></script>
</head>
<body>
    <?php include 'includes/header.php'; ?>
    <h1>Welcome to My Web Project</h1>
    <?php include 'includes/footer.php'; ?>
</body>
</html>"""
        
        files[".htaccess"] = """RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteRule ^ index.html [QSA,L]"""
        
        # Create the folders if they don't exist
        for folder in folders:
            os.makedirs(folder, exist_ok=True)
        
        # Create the files if they don't exist
        for file_path, content in files.items():
            if not os.path.exists(file_path):
                with open(file_path, 'w') as file:
                    file.write(content)
        
        print("Web project folder structure created successfully.")
    else:
        print(f"Project type '{project_type}' is not supported.")

# Example usage
create_project_structure('web', includes=['html', 'js', 'css', 'php', 'sql'], templates='boilerplate')
