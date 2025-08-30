Fullstack-Hotel-Management-System/
├── backend/                              
│   │     
│   ├── app/                           
│   │   ├── __init__.py  
│   │   ├── main.py     									 # FastAPI app entry point
│   │   ├── config.py                                        # App settings via Pydantic BaseSettings
│   │   ├── deps.py                                          # Shared FastAPI dependancies 
│   │   ├── constants.py                                     # App-wide constants or enum
│   │   │         
│   │	├── models/                                          # SQLAlchemy ORM models       
│   │	│   ├── __init__.py       
│   │	│   ├── base_model.py      
│   │	│   ├── core/           
│   │   │   │   ├── __init__.py
│   │   │   │   ├── user_model.py
│   │   │   │   ├── guest_model.py
│   │   │   │   └── staff_model.py
│   │   │   ├── room/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── room_model.py
│   │   │   │   └── room_type_model.py
│   │   │   ├── booking/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── booking_model.py
│   │   │   │   └── reservation_model.py
│   │   │   ├── finance/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── payment_model.py
│   │   │   │   └── billing_model.py
│   │   │   ├── service/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── hotel_service_model.py
│   │   │   │   └── room_service_model.py
│   │   │   └── feedback/
│   │   │       ├── __init__.py
│   │   │       └── feedback_model.py
│   │   │  
│   │   ├── schemas/                                           # All Pydantic schemas 
│   │   │   ├── __init__.py       
│   │   │   ├── base_schema.py                 
│   │   │   ├── core/  
│   │   │   │   ├── __init__.py
│   │   │   │   ├── user_schema.py
│   │   │   │   ├── guest_schema.py
│   │   │   │   └── staff_schema.py   
│   │   │   ├── room/  
│   │   │   │   ├── __init__.py
│   │   │   │   ├── room_schema.py
│   │   │   │   └── room_type_schema.py  
│   │   │   ├── booking/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── booking_schema.py
│   │   │   │   └── reservation_schema.py
│   │   │   ├── finance/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── payment_schema.py
│   │   │   │   └── billing_schema.py
│   │   │   ├── services/ 
│   │   │   │   ├── __init__.py
│   │   │   │   ├── hotel_service_schema.py
│   │   │   │   └── room_service_schema.py
│   │   │   └── feedback/
│   │   │       ├── __init__.py
│   │   │       └── feedback_schema.py           
│   │   │       
│   │   ├── controllers/                                        # FastAPI routers (grouped by domain)
│   │   │   ├── __init__.py   
│   │   │   ├── core/  
│   │   │   │   ├── __init__.py
│   │   │   │   ├── user_controller.py
│   │   │   │   ├── guest_controller.py
│   │   │   │   └── staff_controller.py 
│   │   │   ├── room/  
│   │   │   │   ├── __init__.py
│   │   │   │   └── room_controller.py   
│   │   │   ├── booking/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── booking_controller.py
│   │   │   │   └── reservation_controller.py   
│   │   │   ├── finance/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── payment_controller.py
│   │   │   │   └── billing_controller.py  
│   │   │   ├── service/ 
│   │   │   │   ├── __init__.py
│   │   │   │   ├── hotel_service_controller.py
│   │   │   │   └── room_service_controller.py
│   │   │   └── feedback/
│   │   │       ├── __init__.py
│   │   │       └── feedback_controller.py           
│   │   │
│   │	├── services/                                         # Bussiness logic between controllers and DB
│   │   │	├── __init__.py  
│   │   │   ├── core/  
│   │   │   │   ├── __init__.py
│   │   │   │   ├── user_service.py
│   │   │   │   ├── guest_service.py
│   │   │   │   └── staff_service.py   
│   │   │   ├── room/  
│   │   │   │   ├── __init__.py
│   │   │   │   ├── room_service.py
│   │   │   │   └── room_service.py   
│   │   │   ├── booking/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── booking_service.py
│   │   │   │   └── reservation_service.py  
│   │   │   ├── finance/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── payment_service.py
│   │   │   │   └── billing_service.py  
│   │   │   ├── service/ 
│   │   │   │   ├── __init__.py
│   │   │   │   ├── hotel_service.py
│   │   │   │   └── room_service.py   
│   │   │   └── feedback/
│   │   │       ├── __init__.py
│   │   │       └── feedback_service.py         
│   │   │
│   │	├── db/                                           # DB config and migrations
│   │   │	├── __init__.py       
│   │   │	├── session.py       
│   │   │	├── base.py              
│   │	│	└── migrations/      
│   │	│ 
│   │	├── middleware/  
│   │   │	├── __init__.py                                         
│   │   │	└── auth_required.py  
│   │   │
│   │	├── auth/                                        # JWT-based auth, roles, permissions
│   │   │	├── __init__.py                             
│   │   │	├── security.py                   
│   │   │	└── dependencies.py
│   │   │
│   │   ├── utils/                                       # Reusable helpers
│   │   │	├── __init__.py       
│   │   │	├── helpers.py        
│   │	│	└── validators.py                                                
│   │   │
│   │	└── tests/                                      # Pytest or unittest structure
│   │   	├── __init__.py 
│   │   	├── conftest.py 
│   │   	├── auth/
│   │   	│   └── test_auth.py
│   │   	├── booking/ 
│   │   	│   └── test_booking.py 
│   │   	├── user/ 
│   │   	│   └── test_user.py
│   │   	├── reservation/ 
│   │   	│   └── test_reservation.py
│   │   	└── room/    
│   │           └── test_room.py                
│   │
│   ├── run.py                                  # Entrypoint script 
│   ├── .env
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
│   │	├── routes/                             # React Router configuration
│   │	│   ├── index.js                        # Central route definitions
│   │	│   ├── ProtecteRoute.js                # Auth guard wrapper
│   │   │   └── RoleBaseRoute.js                # (Optional) RBAC support
│   │   │ 
│   ├── pages/                                  # Page-level components (screen views)
│   │   ├── Home.js 
│   │   ├── Login.js 
│   │   ├── Register.js 
│   │   ├── Dashboard/
│   │	│   ├── index.js  
│   │   │   └── StatsWidget.js   
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
│   │   ├── bookingService.js
│   │   └── roomService.js                     
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
│   ├── uploads/    
│   └── __tests__/                                # Client-side uploads (optionsal)
│       ├── App.test.js                 
│    	└── components/
│           └── Navbar.test.js
├── .env                                        # Environment variables
├── .gitignore
├── package.json
│
└── README.md
