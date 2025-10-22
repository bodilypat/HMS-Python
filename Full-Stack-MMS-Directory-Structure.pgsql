Full-Stack-Medical-Management-System-Directory-Structure
├── backend-Python
│   ├── app/  
│   │   ├── main.py                           			# FastAPI app startup
│   │   ├── api_router.py
│   │   ├── api/                              			# Route handler (controllers)
│   │   │   └── endpoints/
│   │   │       ├── __init__.py
│   │   │       ├── patient_router.py
│   │   │       ├── department_router.py
│   │   │       ├── doctor_router.py
│   │   │       ├── appointment_router.py
│   │   │       ├── prescription_router.py
│   │   │       ├── medical_record_router.py
│   │   │       ├── billing_router.py
│   │   │       ├── inventory_router.py
│   │   │       └── lab_api.py
│   │   ├── models/                           			# SQLAlchemy models
│   │   │   ├── __init__.py
│   │   │   ├── patient.py
│   │   │   ├── department.py
│   │   │   ├── doctor.py
│   │   │   ├── appointment.py
│   │   │   ├── prescription.py
│   │   │   ├── medical_record.py
│   │   │   ├── inventory.py
│   │   │   └── billing.py
│   │   ├── schemas/                                    # Pydantic data validation
│   │   │   ├── __init__.py
│   │   │   ├── patient.py
│   │   │   ├── department.py
│   │   │   ├── doctor.py
│   │   │   ├── appointment.py
│   │   │   ├── prescription.py
│   │   │   ├── medical_record.py
│   │   │   ├── inventory.py
│   │   │   └── billing.py
│   │   ├── services/                                   # Business Logic
│   │   │   ├── __init__.py
│   │   │   ├── patient_service.py
│   │   │   ├── department_service.py
│   │   │   ├── doctor_service.py
│   │   │   ├── appointment_service.py
│   │   │   ├── prescription_service.py
│   │   │   ├── medical_record_service.py
│   │   │   ├── inventory_service.py
│   │   │   └── billing_service.py
│   │   ├── db/                                         # Database engine / session/ init
│   │   │   ├── base.py
│   │   │   ├── session.py
│   │   │   └── init_db.py
│   │   ├── middleware/                                 
│   │   │   └── auth_middleware.py
│   │   ├── auth/                                       
│   │   │   ├── auth_handler.py
│   │   │   └── auth_bearer.py
│   │   ├── utils/                                      # Utility functions
│   │   │   └── auth_utils.py
│   │   ├── core/                                       # Configs, security, exceptions
│   │   │   ├── config.py
│   │   │   ├── security.py
│   │   │   └── exceptions.py
│   │   └── main.py                                                                                                                 
│   ├── tests/                                          # Unit & integration test
│   │   ├── api/
│   │   │   ├── test_auth.py
│   │   │   ├── test_patients.py
│   │   │   ├── test_doctors.py
│   │   │   └── test_appointments.py    
│   │   └── services/     
│   │       ├── test_doctors.py
│   │       └── test_appointments.py                             
├── .env                                      
├── README.md                                
├── requirements.txt
├── run.py                              
│
├── frontend-react/                      
│   ├── public                        # Static entry point for deployment  
│   │   └── index.html                # Entry login/landing page 
│   │     
│   ├── src/                              
│   │   ├── assets/
│   │   │   ├── images/ 
│   │   │   │   └── logo.png
│   │   │   └── styles/                     # Module-specific styles 
│   │   │       ├── main.css
│   │   │       └── layout.css
│   │   │
│   ├── components/							
│   │   ├── Navbar.jsx
│   │   ├── Sidebar.jsx
│   │   ├── Footer.jsx     
│   │   └── ModalDelete.jsx
│   ├── pages/	
│   │ 	├── Auth/
│   │   │   ├── login.jsx                    
│   │  	│   ├── register.jsx                     
│   │   │   ├── login.schema.js                 
│   │   │   └── register.schema.js
│   │ 	├── patients/
│   │   │   ├── patientList.jsx                    
│   │  	│   ├── patientFrom.jsx
│   │   │   ├── patient.api.js           
│   │   │   └── patient.schema.js
│   │   ├── doctors/
│   │   │   ├── doctorList.jsx                    
│   │  	│   ├── doctorFrom.jsx                        
│   │   │   └── doctor.api.js
│   │   ├── appointments/   
│   │   │   ├── appointmentList.jsx                    
│   │  	│   ├── appointmentFrom.jsx                            
│   │   │   └── appointment.api.js                 
│   │   ├── billings/
│   │   │   ├── billingList.jsx                    
│   │  	│   ├── billingReceipt.jsx                               
│   │   │   └── billing.api.js                   
│   │   └── reports/ 
│   │      	├── summary.jsx            
│   │      	└── charts.jsx           
│   │ 
│   ├── services/							
│   │   ├── apiClient.js                     # Business logic / utilities
│   │   ├── authService.js                   # Axios or fetch wrapper
│   │   └── session.js
│   ├── utils/                               # Utility scripts/helpers
│   │   ├── formValidation.js
│   │   └── dateUtils.js 
│   ├── routes/                              # Route definitions 
│   │   └── AppRoutes.jsx 
│   │ 
│   ├── App.jsx
│   ├── index.js
│   └── readme.md                 
│
├── .env 
├── package.json
├── tailwind.config.js / postcss.config.js(optional)
└── vite.config.js / webpack.config.js
