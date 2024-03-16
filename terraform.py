import fileinput
import shutil, errno

def copyanything(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno in (errno.ENOTDIR, errno.EINVAL):
            shutil.copy(src, dst)
        else: raise

kind = input("What kind of project are you creating? (1) Notes, (2) Report ")
print(kind)
if kind == "1":
  author = input("Who are you? ")
  projectName = input("What is the title of your new Typst project? ")

  authorNamePlaceholder = '{{AUTHOR}}'
  projectNamePlaceholder = '{{PROJECT_NAME}}'

  outputDir = 'Outputs/{}'.format(projectName)

  copyanything('Templates/Notes', outputDir)

  filePath = '{}/main.typ'.format(outputDir)

  with open(filePath, 'r') as file:
    filedata = file.read()

  filedata = filedata.replace(authorNamePlaceholder, author)
  filedata = filedata.replace(projectNamePlaceholder, projectName)

  with open(filePath, 'w') as file:
    file.write(filedata)

  print('Project created successfully')
  
elif kind == "2":
  projectTitle = input("What is the title of your new Typst project? ")

  titleNamePlaceholder = '{{TITLE}}'
  outputDir = 'Outputs/{}'.format(projectTitle)

  copyanything('Templates/Report', outputDir)

  filePath = '{}/main.typ'.format(outputDir)

  with open(filePath, 'r') as file:
    filedata = file.read()

  filedata = filedata.replace(titleNamePlaceholder, projectTitle)

  with open(filePath, 'w') as file:
    file.write(filedata)

  print('Project created successfully')