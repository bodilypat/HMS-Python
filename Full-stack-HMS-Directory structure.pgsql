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
│   │   │   │	├── __init__.py        
│   │   │   │   ├── user.py
│   │   │   │   ├── guest.py
│   │   │   │   └── staff.py
│   │   │   ├── room/
│   │   │   │	├── __init__.py
│   │   │   │   ├── room.py
│   │   │   │   ├── category.py
│   │   │   │   ├── amenity.py
│   │   │   │   ├── pricing.py
│   │   │   │   └── availability.py
│   │   │   ├── booking/
│   │   │   │	├── __init__.py
│   │   │   │   ├── booking.py
│   │   │   │   ├── reservation.py
│   │   │   │   └── history.py
│   │   │   ├── finance/
│   │   │   │	├── __init__.py
│   │   │   │   ├── payment.py
│   │   │   │   ├── billing.py
│   │   │   │   ├── invoice.py
│   │   │   │   ├── transaction.py
│   │   │   │   └── discount.py
│   │   │   ├── ameneties/
│   │   │   │   ├── hotel.py
│   │   │   │   └── service_room.py
│   │   │   └── feedback/
│   │   │   	├── __init__.py
│   │   │       └── feedback.py
│   │   │  
│   │   ├── schemas/                                           # All Pydantic schemas 
│   │   │   ├── __init__.py       
│   │   │   ├── base_schema.py                 
│   │   │   ├── core/  
│   │   │   │	├── __init__.py
│   │   │   │   ├── user.py
│   │   │   │   ├── guest.py
│   │   │   │   └── staff.py   
│   │   │   ├── room/  
│   │   │   │	├── __init__.py
│   │   │   │   ├── room.py
│   │   │   │   ├── category.py
│   │   │   │   ├── amenity.py
│   │   │   │   ├── pricing.py
│   │   │   │   └── availability.py  
│   │   │   ├── booking/
│   │   │   │	├── __init__.py
│   │   │   │   ├── booking.py
│   │   │   │   ├── reservation.py
│   │   │   │   └── history.py
│   │   │   ├── finance/
│   │   │   │	├── __init__.py
│   │   │   │   ├── payment.py
│   │   │   │   ├── billing.py
│   │   │   │   ├── invoice.py
│   │   │   │   ├── transaction.py
│   │   │   │   └── discount.py
│   │   │   ├── amenities/ 
│   │   │   │	├── __init__.py
│   │   │   │   ├── hotel.py
│   │   │   │   └── service_room.py
│   │   │   └── feedback/
│   │   │   	├── __init__.py
│   │   │       └── feedback.py           
│   │   │
│   │	├── services/                                         # Bussiness logic between controllers and DB
│   │   │	├── __init__.py  
│   │   │   ├── core/  
│   │   │   │	├── __init__.py
│   │   │   │   ├── user.py
│   │   │   │   ├── guest.py
│   │   │   │   └── staff.py   
│   │   │   ├── room/  
│   │   │   │	├── __init__.py
│   │   │   │   ├── management.py
│   │   │   │   ├── category.py
│   │   │   │   ├── availability.py
│   │   │   │   ├── amenities.py
│   │   │   │	├── pricing.py
│   │   │   │   └── inventory.py   
│   │   │   ├── booking/
│   │   │   │	├── __init__.py
│   │   │   │   ├── booking.py
│   │   │   │   ├── reservation.py
│   │   │   │   ├── availability.py
│   │   │   │   └── history.py  
│   │   │   ├── finance/
│   │   │   │	├── __init__.py
│   │   │   │   ├── payment.py
│   │   │   │   ├── billing.py
│   │   │   │   ├── invoice.py
│   │   │   │   ├── transaction.py
│   │   │   │   └── discount.py
│   │   │   ├── amenities/ 
│   │   │   │	├── __init__.py
│   │   │   │   ├── hotel.py
│   │   │   │   └── service_room.py   
│   │   │   └── feedback/
│   │   │   	├── __init__.py
│   │   │       └── feedback.py   
│   │   ├── controllers/                                        # FastAPI routers (grouped by domain)
│   │   │   ├── __init__.py   
│   │   │   ├── core/  
│   │   │   │	├── __init__.py
│   │   │   │   ├── user.py
│   │   │   │   ├── guest.py
│   │   │   │   └── staff.py 
│   │   │   ├── room/  
│   │   │   │	├── __init__.py
│   │   │   │   ├── room.py
│   │   │   │   ├── category.py
│   │   │   │   ├── availabiity.py
│   │   │   │   ├── amenity.py
│   │   │   │   └── pricing.py   
│   │   │   ├── booking/
│   │   │   │	├── __init__.py
│   │   │   │   ├── booking.py
│   │   │   │   ├── reservation.py
│   │   │   │   └── history.py  
│   │   │   ├── finance/
│   │   │   │	├── __init__.py
│   │   │   │   ├── billing.py
│   │   │   │   ├── payment.py
│   │   │   │   ├── invoice.py
│   │   │   │   └── transaction.py  
│   │   │   ├── service/ 
│   │   │   │	├── __init__.py
│   │   │   │   ├── hotel.py
│   │   │   │   └── room_service.py
│   │   │   ├── amenities/ 
│   │   │   │	├── __init__.py
│   │   │   │   ├── hotel.py
│   │   │   │   └── service_room.py
│   │   │   └── feedback/
│   │   │   	├── __init__.py
│   │   │       └── feedback.py     
│   │   ├── utils/                                       	 # Reusable helpers
│   │   │	├── __init__.py       
│   │   │	├── helpers.py        
│   │	│	└── validators.py                 
│   │   │
│   │	├── db/                                              # DB config and migrations
│   │   │	├── __init__.py       
│   │   │	├── session.py       
│   │   │	├── base.py              
│   │	│	└── migrations/                                               
│   │   │
│   │	└── tests/                                           # Pytest or unittest structure
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
│   ├── run.py                                             # Entrypoint script 
│   ├── .env
│   └── requirements.txt                                   # Dependancies 
│    FastAPI(main.py) ->Controller -> Service (room/management.py) -> Model Layer -> DB session (db/session.py) -> Returns: Schema(from schema/room/)
├── frontend/                             
│   ├── public/   
│   │   ├── index.html  
│   │   ├── favicon.ico
│   │   └── assets/
│   │   	├── images/  
│   │   	└── icons/
│   ├── src/                                    
│   │   ├── index.js                                      # React entry point
│   │   ├── app.js                                        # Root App wrapper
│   │	├── routes/                                       # Routing logic
│   │	│   ├── appRoutes.js                              # AppRoutes defininition
│   │	│   ├── protecteRoute.js                
│   │   │   └── roleBaseRoute.js                 
│   │	├── features       /                              # Page-level views grouped by domain
│   │   │ 	├── auth/ 
│   │   │ 	│	├── pages/
│   │   │ 	│	│   ├── login.js
│   │   │ 	│	│   └── register.js
│   │   │ 	│	├── services/
│   │   │   │ 	│	└── authService.js
│   │   │ 	│	├── context/
│   │   │   │ 	│	└── authContext.js
│   │   │ 	│	└── hooks/
│	│	│	│		└── useAuth.js
│   │   │ 	├── Booking/  
│   │   │ 	│	├── pages/
│   │   │ 	│	│   ├── BookingList.js
│   │   │ 	│	│   ├── BookingForm.js
│   │   │ 	│	│   └── Bookingdetials.js
│   │   │ 	│	├── components/
│   │   │   │ 	│	└── bookingCard.js
│   │   │ 	│	├── services/
│   │   │   │ 	│	└── bookingService.js
│   │   │ 	│	└── hooks/
│	│	│	│		└── useBooking.js
│   │   │ 	├── room/
│   │   │ 	│	├── pages/
│   │   │ 	│	│   ├── roomList.js
│   │   │ 	│	│   ├── roomDetails.js
│   │   │ 	│	│   └── roomManagement.js
│   │   │ 	│	├── components/
│   │   │   │ 	│	└── roomCard.js
│   │   │ 	│	├── services/
│   │   │   │ 	│	└── roomService.js
│   │   │ 	│	└── styles/
│	│	│	│		└── room.css  
│   │   │ 	├── finance/
│   │   │ 	│	├── pages/
│   │   │ 	│	│   ├── billing.js
│   │   │ 	│	│   └── payment.js
│   │   │ 	│	└── services/
│	│	│	│		└── financeService.js
│   │   │ 	├── feedback/
│   │   │ 	│	├── pages/
│   │   │ 	│	│   └── feedbackForm.js
│   │   │ 	│	├── components/
│   │   │   │ 	│	└── ratingStars.js
│   │   │ 	│	└── services/
│	│	│	│		└── feedbackService.js 
│   │   │ 	├── services/
│   │   │ 	│	├── pages/
│   │   │ 	│	│   └── roomService.js
│   │   │ 	│	└── services/
│	│	│	│		└── serviceRequestService.js 
│   │   │ 	└── dashboard/  
│   │   │ 	│	├── pages/
│   │   │ 	│	│   ├── Dashboard.js
│   │   │ 	│	│   └── StatsWidget.js
│   │   │ 	│	└── styles/
│	│	│	│		└── dashboard.css        
│   │   │   │  	     
│   │	├── shared/                                      # Global/Shared modules
│   │   │	├── components/
│   │   │   │	├── navbar.js
│   │   │   │	├── footer.js
│   │   │   │	└── sidebar.js 
│   │   │	├── hooks/
│   │   │   │	├── useForm.js
│   │   │   │	└── useDebounce.js (optional)
│   │   │	├── styles/
│   │   │   │	└── main.css
│   │   │	└── utils/     
│   │   │   	├── constants.js
│   │   │		└── validators.js               
│   │	├── services/                                    # API call abstraction
│   │   │	└── api.js                     
│  	│	├── context/                                     # Global state 
│   │   │	└── globalAppContext.js 
│   │   │
│   └── tests/                                           # Client-side uploads (optionsal)
│       ├── features/  
│       │   ├── auth/  
│		│   │   └── login.test.js		
│       │   ├── booking/
│		│	│	└── bookingList.test.js
│       │   ├── feedback/		
│		│   │   └── feedbackForm.test.js	
│       │	└── room/
│		│       └── roomCard.test.js	
│    	└── app.test.js
├── .env                                                # Environment variables
├── .gitignore
├── package.json
└── README.md
