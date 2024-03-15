# Terraform new Typst projects

Simple and easy script to startup new Typst projects (we are not using the real Terraform though)

## Usage

As now, we can specify the name of the project and the name of the user. The script will create a new directory with the name of the project inside `Outputs`

```bash
% python3 terraform.py
Who are you? Miche-lino
What is the title of your new Typst project? Quantum Simulation
Project created successfully
```

As now we have only one template, in the future we need to a add new templates, such as "Reports" with different configs
