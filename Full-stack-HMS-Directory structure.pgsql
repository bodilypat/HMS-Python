Fullstack-Hotel-Management-System/
├── backend/                              
│   │     
│   ├── app/                           
│  	│	├── __init__.py       
│  	│   │         
│   │   ├── config/   
│   │   │	├── __init__.py    
│   │   │	└── settings.py
│   │   │
│   │	├── models/                                          # SQLAlchemy models       
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
│   │  	│   │   │   └── v1/  
│   │ 	│   │   │   	├── auth/
│   │   │   │   │      	│   ├── login_controller.py
│   │   │   │   │       │   ├── logout_controller.py
│   │   │   │   │       │   └── register_controller.py
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
│   │   │   │       └── room_service_controller.py 
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
│   │   ├── test_auth.py  
│   │   └── test_user.py                   
│   │
│   ├── run.py 
│   └── requirements.txt
│   
├── frontend/                             
│   ├── public/   
│   │   ├── index.html  
│   │   ├── favicon.ico
│   │   └── assets/
│   │   	├── images/  
│   │   	└── icons/
│   ├── src/  
│   │   ├── App.js
│   │   ├── index.js 
│   │   └── routes/                                        # React Router Routes
│   │   	└── ProtectRoute.js                 
│   ├── pages/
│   │   ├── Home.js 
│   │   ├── Login.js 
│   │   ├── Register.js 
│   │   ├── Dashboard.js    
│   │   ├── Booking.js    
│   │   ├── Rooms.js    
│   │   ├── Feedback.js    
│   │   └── Profile.js                  
│   ├── components/
│   │   ├── Navbar.js
│   │   ├── Footer.js
│   │   ├── Sidebar.js
│   │   ├── RoomCard.js
│   │   └── BookingForm.js                    
│   ├── services/ 
│   │   ├── api.js                                         # Axios/fetch wrapper
│   │   ├── authService.js
│   │   └── bookingService.js                     
│   ├── context/ 
│   │   └── AuthContent.js 
│   ├── styles/ 
│   │   ├── main.css
│   │   └── dashboard.css 
│   ├── utils/ 
│   │   ├── validators.js
│   │   └── contants.js
│   │    
│   └── uploads/                           # Client-side uploads (optionsal)
├── .env                                   # Environment variables
├── .gitignore
├── package.json
│
└── README.md
