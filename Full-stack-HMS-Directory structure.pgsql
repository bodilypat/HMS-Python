Fullstack-Hotel-Management-System/
├── backend/                              
│   │     
│   ├── app/                           
│  	│	├── __init__.py       
│  	│   │         
│   │   ├── config/   
│   │   │	├── __init__.py    
│   │   │	└── setting.py
│   │   │
│   │	├── models/                                        # SQLAlchemy models       
│   │	│   ├── __init__py        
│   │	│   ├── core/           
│   │   │   │   ├── base_model.py
│   │   │   │   ├── user.py
│   │   │   │   ├── guest.py
│   │   │   │   └── staff.py
│   │   │   ├── booking/
│   │   │   │   ├── booking.py
│   │   │   │   └── reservation.py
│   │   │   ├── finance/
│   │   │   │   ├── payment.py
│   │   │   │   └── room_service.py
│   │   │   ├── feedback/
│   │   │   │   └── feedback.py
│   │   │   ├── guest/
│   │   │   │   └── guest.py
│   │   │   ├── room/
│   │   │   │   └── room.py
│   │   │   │
│   │   ├── controllers/
│   │   │   ├── base_controller.py       
│   │   │   │   ├── api/
│   │  	│   │   │   └── v1  
│   │ 	│   │   │   	├── auth/
│   │   │   │   │      	│   ├── login_controller.py
│   │   │   │   │       │   ├── logout_controller.py
│   │   │   │   │       │   └── regisgter_controller.py
│   │   │   │   │       ├── user_controller.py
│   │   │   │   │       ├── guest_controller.py
│   │   │   │   │       ├── booking_controller.py
│   │   │   │   │       ├── room_controller.py
│   │   │   │   │       ├── reservation_controller.py
│   │   │   │   │       └── payment_controller.py
│   │   │   │   └── admin/
│   │   │   │       ├── dashboard_controller.py    
│   │   │   │       ├── staff_controller.py    
│   │   │   │       ├── billing_controller.py    
│   │   │   │       ├── feedback_controller.py      
│   │   │   │       └── room_service_controller.php  
│   │   │   │
│   │	├── services/                           
│   │	│   ├── __init__.py       
│   │	│   ├── auth_service.py                 
│   │	│   ├── booking_service.py       
│   │	│   ├── billing_service.py
│   │	│   └── payment_service.py      
│   │	│   
│   │	├── routes/                           
│   │	│   ├── __init__.py       
│   │	│   ├── api.py                 
│   │	│   └── web.py         
│   │	│ 
│   │	├── middleware/                                    
│   │	│   └── auth_required.py  
│   │	│   
│   │	├── templates/                           
│   │	│   ├── email/                      
│   │	│   └── admin/   
│   │	├── static/                                    
│   │	│  
│   │	├── uploads/                                    
│   │	│   └── receipts/ 
│   │	├── database.py                                    
│   │   └── utils.py                                                  
│   │
│   ├── tests/                            
│   │   ├── __init__.py 
│   │   ├── test_booking.py
│   │   ├── test_au.py  
│   │   └── test_user.py                   
│   │
│   ├── run.py 
│   ├── requirements.txt
│   │
├── frontend/                             # Client-side application
│   ├── pages/   
│   │   ├── index.html  
│   │   ├── booking.html
│   │   ├── roomd.html 
│   │   ├── feedback.html 
│   │   ├── login.html 
│   │   └── dashboard.html                       
│   ├── css/  
│   │   ├── main.css
│   │   ├── booking.css 
│   │   ├── dashboard.css   
│   │   └── responsive.css                 
│   ├── js/
│   │   ├── main.js 
│   │   ├── booking.js 
│   │   ├── feedback.js 
│   │   ├── auth.js    
│   │   └── dashboard.js                  
│   ├── components/
│   │   ├── header.html
│   │   ├── footer.html
│   │   └── room-card.html                    
│   ├── images/ 
│   │   ├── logo.png
│   │   ├── rooms/
│   │   └── icons/ 
│   │       ├── checkin.svg  
│   │       └── service.svg                     
│   ├── assets/ 
│   │   └── vendors/                  
│   │    
│   └── uploads/                           # Client-side uploads (optionsal)
├── .env                                   # Environment variables
├── .gitignore
│
└── README.md
