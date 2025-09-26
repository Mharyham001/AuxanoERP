# ERP 

ERP is a modular Enterprise Resource Planning (ERP) system built with Django and PostgreSQL.  
It is designed to unify organizational operations across multiple modules while maintaining flexibility, synchronization, and scalability.  

## 🚀 Features
- **Purchases Module**
  - Staff can create purchase requests.
  - Vendors can submit quotations.
  - Automatic creation of Purchase Orders from approved quotations.
  - Approve/Decline workflow with edit/delete functionality.

- **Inventory Module**
  - Manage products, categories, and stock levels.
  - Track staff and their assigned roles.
  - Create and monitor orders.
  - Role-based access control for staff and orders.
  - Sidebar navigation with modular templates.

- **Multi-Tenant Support**
  - Each organization runs in isolated tenant schemas.
  - Load sample data per tenant for testing.

- **Developer Friendly**
  - Dockerized setup for consistency.
  - Fixtures provided for sample data.
  - Organized module structure for scalability.

---

## 🛠️ Tech Stack
- **Backend:** Django (Python 3.12+)
- **Database:** PostgreSQL
- **Containerization:** Docker + Docker Compose
- **Frontend:** Django Templates + Bootstrap
- **Version Control:** GitHub

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/HeteroGenius01/erp_1_0/tree/Ayomide
cd erp_1_0


-------------------------------------------------------------------------------
🧪 Running Locally (without Docker)

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

-----------------------------------------------------------
📂 Project Structure


erp_1_0/
│── erp_1_0/            # Core Django project
│── purchases/          # Purchases module
│── inventory/          # Inventory module
│── templates/          # HTML templates
│── fixtures/           # Sample/test data
│── docker-compose.yml  # Docker setup
│── requirements.txt    # Dependencies
│── .env.example        # Environment variables template


-----------------------------------------------------
🤝 Contributing

Fork the repo

Create your feature branch: git checkout -b feature/your-feature

Commit changes: git commit -m 'Add your feature'

Push to branch: git push origin feature/your-feature

Open a Pull Request

------------------------------------------------------------------
📜 License

This project is licensed under the MIT License.
You are free to use, modify, and distribute it under the terms of the license.

--------------------------------------------------------------------------

✅ Summary of Techniques Used

Backend Framework: Django (ORM, Forms, CBVs, RBAC)

Database: MySQL (initial), migrated to PostgreSQL

Containerization: Docker + Docker Compose

Version Control: GitHub with .gitignore rules

Frontend: Django templates + Bootstrap + Modal forms

Data Management: JSON fixtures for test/sample data

Access Control: Django permissions & role restrictions

Multi-tenancy: Schema-based tenant support

----------------------------------------------------------------------
👨🏽‍💻 Author
Ogunyemi Ayomide Samuel (Anuoluwa)

----------------------------------------------------------------------

This `README.md` is **production-ready**:  
- It explains **what ERP is**  
- Guides on **setup & usage**  
- Includes **tech stack & structure**  
- Has a **contribution guide & license**  


for further questions or observations, feel free to reach out to me via mail ayomidesamuel365@gmail.com