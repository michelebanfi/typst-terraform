import fileinput
import shutil, errno

def copyanything(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno in (errno.ENOTDIR, errno.EINVAL):
            shutil.copy(src, dst)
        else: raise

author = input("Who are you? ")
projectName = input("What is the title of your new Typst project? ")

authorNamePlaceholder = '{{AUTHOR}}'
projectNamePlaceholder = '{{PROJECT_NAME}}'

outputDir = 'Outputs/{}'.format(projectName)

copyanything('Templates', outputDir)

filePath = '{}/main.typ'.format(outputDir)

with open(filePath, 'r') as file:
  filedata = file.read()

filedata = filedata.replace(authorNamePlaceholder, author)
filedata = filedata.replace(projectNamePlaceholder, projectName)

with open(filePath, 'w') as file:
  file.write(filedata)

print('Project created successfully')

# {{PROJECT_NAME}}
# {{AUTHOR}}