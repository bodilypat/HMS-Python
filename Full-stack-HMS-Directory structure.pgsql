Fullstack-Hotel-Management-System/
├── backend/                              
│   │     
│   ├── app/                           
│  	│	├── __init__.py  
│  	│	├── main.py     									 # FastAPI app entry point
│  	│   │         
│   │   ├── config/                                          # Configuration & environment
│   │   │	├── __init__.py   
│   │   │	├── setting.py                                   # Pydantic settings
│   │   │	└── database.py                                  # SQLAlchemy engine/session config
│   │   │
│   │	├── models/                                          # SQLAlchemy ORM models       
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
│   │   │   │   └── billing.py
│   │   │   ├── room/
│   │   │   │   ├── room.py
│   │   │   │   └── roomtype.py
│   │   │   ├── service/
│   │   │   │   ├── service.py
│   │   │   │   └── room_service.py
│   │   │   └── feedback.py
│   │   │       └── feedback.py
│   │   │  
│   ├── schemas/                                           # Pydantic models(DTOS)
│   │   ├── __init__.py       
│   │   ├── user.py                 
│   │   ├── guest.py       
│   │   ├── booking.py
│   │   ├── reservation.py                 
│   │   ├── payment.py       
│   │   ├── room.py
│   │   ├── service.py                 
│   │   └── feedback.py      
│   ├── controllers/                                        # API logic (view layer)
│   │   ├── __init__.py       
│   │   ├── base.py                                         # Base controller logic
│   │   ├── v1/        
│   │   │  	├── auth/
│   │   │  	│   ├── login.py
│   │   │   │   ├── logout.py
│   │   │   │   └── register.py
│   │   │   ├── user.py
│   │   │   ├── guest.py
│   │   │   ├── booking.py
│   │   │   ├── room.py
│   │   │   ├── reservation.py
│   │   │   ├── payment.py
│   │   │   └── feedback.py
│   │   └── admin/
│   │       ├── dashboard.py    
│   │       ├── staff.py    
│   │       ├── billing.py    
│   │       └── room_service.py 
│   │   
│   ├── services/                                         # Bussiness logic layer
│   │   ├── __init__.py       
│   │   ├── auth.py                 
│   │   ├── booking.py       
│   │   ├── billing.py
│   │   ├── payment.py
│   │   └── room_service.py      
│   │   
│   ├── routes/                           
│   │   ├── __init__.py       
│   │   ├── api.py                 
│   │	└── web.py         
│   │	 
│   ├── middleware/                                    
│   │   └── auth_required.py  
│   │   
│   ├── templates/                           
│   │   ├── email/                      
│   │   └── admin/   
│   ├── static/                                    
│   │  
│   ├── uploads/                                    
│   │   └── receipts/
│   │
│   ├── utils/                           
│   │   ├── __init__.py       
│   │   ├── hash.py
│   │   ├── jwt.py                 
│   │	└── common.py                                                
│   │
│   ├── tests/                                   # Pytest or unittest structure
│   │   ├── __init__.py 
│   │   ├── auth/
│   │   │   └── test_auth.py
│   │   ├── booking/ 
│   │   │   └── test_booking.py 
│   │   ├── user/ 
│   │   │   └── test_user.py
│   │   ├── reservation/ 
│   │   │   └── test_reservation.py
│   │   └── room/    
│   │       └── test_room.py                
│   │
│   ├── run.py                                  # Entrypoint script 
│   └── requirements.txt                        # Dependancies 
│   
├── frontend/                             
│   ├── public/   
│   │   ├── index.html  
│   │   ├── favicon.ico
│   │   └── assets/
│   │   	├── images/  
│   │   	└── icons/
│   ├── src/                                    # Main source code
│   │   ├── index.js                            # Entry point
│   │   ├── App.js                              # Root component
│   │   ├── routes/
│   │   │   ├── index.js
│   │   │   └── ProtectedRoute.js   
│   ├── pages/                                  # Page-level components (screen views)
│   │   ├── Home.js 
│   │   ├── Login.js 
│   │   ├── Register.js 
│   │   ├── Dashboard.js    
│   │   ├── Booking.js    
│   │   ├── Rooms.js    
│   │   ├── Feedback.js    
│   │   └── Profile.js                  
│   ├── components/
│   │   ├── common/
│   │   │   ├── Navbar.js
│   │   │   ├── Footer.js
│   │   │   └── Sidebar.js 
│   │   ├── booking/
│   │   │   └── bookingForm.js
│   │   └── rooms/     
│   │   	└── RoomCard.js               
│   ├── services/                               # API service layer (Axios, Fetch)
│   │   ├── api.js                                         
│   │   ├── authService.js
│   │   └── bookingService.js                     
│   ├── context/                                # Global state 
│   │   └── AuthContent.js 
│   ├── hooks/                                  # Custom React hooks
│   │   └── userAuth.js 
│   ├── styles/                                 # Global and module-based styles
│   │   ├── main.css
│   │   └── dashboard.css 
│   ├── utils/                                  # Utility functions and constants
│   │   ├── validators.js
│   │   └── contants.js
│   │    
│   └── uploads/                                # Client-side uploads (optionsal)
├── .env                                        # Environment variables
├── .gitignore
├── package.json
│
└── README.md
