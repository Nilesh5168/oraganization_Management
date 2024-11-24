# oraganization_Management


A Django web application that allows multiple organizations to manage their own users and roles. The system supports role-based access control, where organization admins can oversee their respective users and assign roles.

## Features

1. **Multi-Organizational Support**:
   - A Main Organization ("Admin Organization") can manage sub-organizations.
   - Each sub-organization has its own users and roles.

2. **Role-Based Access Control**:
   - Roles include Admin, Editor, and Viewer.
   - Only organization admins can assign roles to their users.

3. **User Management**:
   - Organization admins can create, view, update, and delete users within their organization.
   - Users are restricted to seeing and managing data for their organization only.

4. **CRUD for Organizations**:
   - Main Organization's admin can create, update, and delete sub-organizations.

## Installation

### Prerequisites
- Python 3.8+
- Django 4.x
- PostgreSQL (optional, SQLite is used by default)

### Steps to Set Up

1. **Clone the Repository**:

   git clone https://github.com/Nilesh5168/oraganization_Management
   cd multi-org-management

2. **Apply Migrations**:

python manage.py makemigrations
python manage.py migrate

3.**Run the Server**:
python manage.py runserver
