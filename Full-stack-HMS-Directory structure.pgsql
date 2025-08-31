Fullstack-Hotel-Management-System/
├── backend/                              
│   │     
│   ├── app/                           
│   │   ├── main.py     									 # FastAPI app entry point
│   │   ├── config.py                                        # App settings via Pydantic BaseSettings
│   │   ├── constants.py                                     # App-wide constants or enum
│   │	├── deps/                               
│   │   │	└── db.py  
│   │	├── core/                                            # Core infra: security, auth, etc.
│   │   │	├── __init__.py                             
│   │   │	├── auth.py                                      # JWT, OAuth, etc.
│   │   │	└── hashing.py                                   # Password hashing utilities
│   │   │         
│   │	├── models/                                          # SQLAlchemy ORM models       
│   │	│   ├── __init__.py       
│   │	│   ├── base_model.py      
│   │	│   ├── core/           
│   │   │   │   ├── user.py
│   │   │   │   ├── guest.py
│   │   │   │   └── staff.py
│   │   │   ├── room/
│   │   │   │   ├── room.py
│   │   │   │   ├── category.py
│   │   │   │   ├── amenity.py
│   │   │   │   ├── pricing.py
│   │   │   │   └── availability.py
│   │   │   ├── booking/
│   │   │   │   ├── booking.py
│   │   │   │   ├── reservation.py
│   │   │   │   └── history.py
│   │   │   ├── finance/
│   │   │   │   ├── payment.py
│   │   │   │   ├── billing.py
│   │   │   │   ├── invoice.py
│   │   │   │   ├── transaction.py
│   │   │   │   └── discount.py
│   │   │   ├── service/
│   │   │   │   ├── hotel.py
│   │   │   │   └── room.py
│   │   │   └── feedback/
│   │   │       ├── __init__.py
│   │   │       └── feedback.py
│   │   │  
│   │   ├── schemas/                                           # All Pydantic schemas 
│   │   │   ├── __init__.py       
│   │   │   ├── base_schema.py                 
│   │   │   ├── core/  
│   │   │   │   ├── user.py
│   │   │   │   ├── guest.py
│   │   │   │   └── staff.py   
│   │   │   ├── room/  
│   │   │   │   ├── room.py
│   │   │   │   ├── category.py
│   │   │   │   ├── amenity.py
│   │   │   │   ├── availability.py
│   │   │   │   └── princing.py  
│   │   │   ├── booking/
│   │   │   │   ├── booking.py
│   │   │   │   ├── reservation.py
│   │   │   │   └── history.py
│   │   │   ├── finance/
│   │   │   │   ├── payment.py
│   │   │   │   ├── billing.py
│   │   │   │   ├── transaction.py
│   │   │   │   ├── invoice.py
│   │   │   │   └── discount.py
│   │   │   ├── services/ 
│   │   │   │   ├── hotel.py
│   │   │   │   └── room.py
│   │   │   └── feedback/
│   │   │       └── feedback.py           
│   │   │
│   │	├── services/                                         # Bussiness logic between controllers and DB
│   │   │	├── __init__.py  
│   │   │   ├── core/  
│   │   │   │   ├── user.py
│   │   │   │   ├── guest.py
│   │   │   │   └── staff.py   
│   │   │   ├── room/  
│   │   │   │   ├── management.py
│   │   │   │   ├── category.py
│   │   │   │   ├── availability.py
│   │   │   │   ├── pricing.py
│   │   │   │   └── inventory.py   
│   │   │   ├── booking/
│   │   │   │   ├── booking.py
│   │   │   │   ├── reservation.py
│   │   │   │   ├── availbility.py
│   │   │   │   └── history.py  
│   │   │   ├── finance/
│   │   │   │   ├── payment.py
│   │   │   │   ├── billing.py
│   │   │   │   ├── invoice.py
│   │   │   │   ├── transaction.py
│   │   │   │   └── discount.py
│   │   │   ├── service/ 
│   │   │   │   ├── hotel.py
│   │   │   │   └── room_service.py   
│   │   │   └── feedback/
│   │   │       └── feedback.py   
│   │   ├── controllers/                                        # FastAPI routers (grouped by domain)
│   │   │   ├── __init__.py   
│   │   │   ├── core/  
│   │   │   │   ├── user.py
│   │   │   │   ├── guest.py
│   │   │   │   └── staff.py 
│   │   │   ├── room/  
│   │   │   │   ├── room.py
│   │   │   │   ├── category.py
│   │   │   │   └── availability.py   
│   │   │   ├── booking/
│   │   │   │   ├── booking.py
│   │   │   │   └── reservation.py  
│   │   │   ├── finance/
│   │   │   │   ├── billing.py
│   │   │   │   └── payment.py  
│   │   │   ├── service/ 
│   │   │   │   ├── hotel.py
│   │   │   │   └── room_service.py
│   │   │   └── feedback/
│   │   │       └── feedback.py     
│   │   ├── utils/                                       # Reusable helpers
│   │   │	├── __init__.py       
│   │   │	├── helpers.py        
│   │	│	└── validators.py                 
│   │   │
│   │	├── db/                                           # DB config and migrations
│   │   │	├── __init__.py       
│   │   │	├── session.py       
│   │   │	├── base.py              
│   │	│	└── migrations/                                               
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
