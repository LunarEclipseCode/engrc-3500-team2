import os
import shutil

# Get the directory of the script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Directory containing the HTML files
html_directory = os.path.join(script_directory, '_build', 'html', 'content')

# HTML code block to be inserted
github_block = '''
    <div class="dropdown dropdown-source-buttons">
    <button class="btn dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false" aria-label="Source repositories">
      <i class="fab fa-github"></i>
    </button>
    <ul class="dropdown-menu">
        
        
        
        <li><a href="https://github.com/LunarEclipseCode/engrc-3500-team2" target="_blank"
     class="btn btn-sm btn-source-repository-button dropdown-item"
     title="Source repository"
     data-bs-placement="left" data-bs-toggle="tooltip"
  >
    
  
  <span class="btn__icon-container">
    <i class="fab fa-github"></i>
    </span>
  <span class="btn__text-container">Repository</span>
  </a>
  </li>
        
        
        
        
        <li><a href="https://github.com/LunarEclipseCode/engrc-3500-team2/issues" target="_blank"
     class="btn btn-sm btn-source-issues-button dropdown-item"
     title="Open an issue"
     data-bs-placement="left" data-bs-toggle="tooltip"
  >
    
  
  <span class="btn__icon-container">
    <i class="fas fa-lightbulb"></i>
    </span>
  <span class="btn__text-container">Open issue</span>
  </a>
  </li>
        
    </ul>
  </div>
'''

# code block to have link to homepage in the sidebar
homepage_block = '''

        <ul class="nav bd-sidenav bd-sidenav__home-link">
            <li class="toctree-l1">
                <a class="reference internal" href="../../intro.html">
                    Home Page
                </a>
            </li>
        </ul>
'''

google_form = ''''<iframe src="https://docs.google.com/forms/d/e/1FAIpQLSeSYc5M8ci_heB02N-iVcbPs-Px6n8hgmtrGe7qbP-k4nkrAw/viewform?embedded=true" width="700" height="610" frameborder="0" marginheight="0" marginwidth="0">Loading</iframe>'''

choose_language =''''
  <div class="dropdown dropdown-language-buttons">
    <button class="btn dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false" aria-label="Source repositories">
      <i class="fa-solid fa-language"></i>
    </button>
    <ul class="dropdown-menu">
      
        
        <li><a href="https://github.com/LunarEclipseCode/engrc-3500-team2" target="_blank"
     class="btn btn-sm btn-source-repository-button dropdown-item"
     title="English"
     data-bs-placement="left" data-bs-toggle="tooltip"
  >
    
  
  <span class="btn__icon-container">
    </span>
  <span class="btn__text-container">English</span>
  </a>
  </li>
        

        <li><a href="https://github.com/LunarEclipseCode/engrc-3500-team2/issues" target="_blank"
     class="btn btn-sm btn-source-issues-button dropdown-item"
     title="Mandarin"
     data-bs-placement="left" data-bs-toggle="tooltip"
  >
  
  <span class="btn__icon-container">
    </span>
  <span class="btn__text-container">Mandarin</span>
  </a>
  </li>
        
    </ul>
  </div>
  
  '''
  

def add_content(file_path, class_name, add_code):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        search_line = class_name
        
        # Find the index of the search line in the content
        index = content.find(search_line)
        while index != -1:
            # Insert the code block after the search line
            content = content[:index + len(search_line)] + add_code + content[index + len(search_line):]
            index = content.find(search_line, index + len(search_line))

        # Write the modified content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
            
def add_google_form(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        
        last_index = content.rfind('</section>')
        if last_index != -1:
            updated_html = content[:last_index]+ google_form + content[last_index + len('</section>'):]
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(updated_html)
            

# Source and destination directories
source_directory = os.path.join(script_directory,'content')  

# Function to copy images from source to destination directory
def copy_images(source, destination):
    for root, dirs, files in os.walk(source):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                source_path = os.path.join(root, file)
                relative_path = os.path.relpath(source_path, source)
                destination_path = os.path.join(destination, relative_path)

                # Create the directory structure in the destination folder
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)

                # Copy the image file to the destination folder
                shutil.copyfile(source_path, destination_path)


# Iterate through each HTML file in the directory
for root, dirs, files in os.walk(html_directory):
    for filename in files:
        if filename.endswith('.html'):
            file_path = os.path.join(root, filename)
            
            add_content(file_path, '<div class="article-header-buttons">', github_block)
            add_content(file_path, '<div class="bd-toc-item navbar-nav active">', homepage_block)
            
            
            if filename != 'intro.html':
                add_google_form(file_path)
            

# Add the images corresponding to html files in the proper folder
copy_images(source_directory, html_directory)

#fix the intro.html relative link
apple_dir = os.path.join(html_directory, 'iPhone')

for root, dirs, files in os.walk(apple_dir):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)

            # Read the contents of the file
            with open(file_path, 'r', encoding='utf-8') as f:
                file_contents = f.read()

            # Replace the old string with the new string
            new_contents = file_contents.replace("../../intro.html", "../intro.html")

            # Write the modified contents back to the file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_contents)

# copy over the logo into static              
dark_logo = os.path.join(script_directory, "help-dark.png")
light_logo = os.path.join(script_directory, "help-light.png")
move_logo = os.path.join(script_directory, '_build', 'html', '_static')

shutil.copy(dark_logo, move_logo)
shutil.copy(light_logo, move_logo)
     
# fix relative directory in intro.html   
intro_file = os.path.join(html_directory, 'intro.html')
        
with open(intro_file, 'r') as file:
    content = file.read()
    
content = content.replace("../../intro.html", "intro.html")

with open(intro_file, 'w') as file:
    file.write(content)



    

