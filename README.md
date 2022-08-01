# Team Member Management
A simple team-member management application implemented using Django

## Building the project
- Clone this repo
- Navigate to this repo's parent directory
- Install Python from https://www.python.org/
- Install PIP from https://pypi.org/project/pip/
- Install Django using the command `python -m pip install Django`
- Install django-bootstrap v5 using the command `python -m pip install django-bootstrap-v5`
- Insatll django-bootstrap-icons using the command `python -m pip install django-bootstrap-icons`
- Install Python Decouple using the command `python -m pip install python-decouple`
- Run the command `python manage.py runserver`

## Testing the project
- Go to http://127.0.0.1:8000/
- View all team members and the number of team members on the list page
- Click the plus at the top of the list page to go to the add page
- Click a team member on the list page to go to the edit page
- To add a team member:
  - Go to the add page
  - Enter the team member's first name in the first input field
  - Enter the team member's last name in the second input field
  - Enter the team member's email in the third input field
  - Enter the team member's phone number in the fourth input field
  - Choose the team member's role using the radio buttons
  - Click save to add the team member and return to the list page
- To edit a team member:
  - Go to the team member's edit page
  - Edit the team member's first name in the first input field
  - Edit the team member's last name in the second input field
  - Edit the team member's email in the third input field
  - Edit the team member's phone number in the fourth input field
  - Change the team member's role using the radio buttons
  - Click save to edit the team member and return to the list page
- To delete a team member:
  - Go to the team member's edit page
  - Click delete to delete the team member and return to the list page
