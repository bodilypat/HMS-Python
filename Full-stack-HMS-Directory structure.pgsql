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
│   
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
│   │	├── pages(features)/                              # Page-level views grouped by domain
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
│   │   │     	     
│   │	├── shared/                                      # Global/Shared modules
│   │   │	├── components/
│   │   │   │	├── navbar.js
│   │   │   │	├── footer.js
│   │   │   │	└── sidebar.js 
│   │   │	├── hooks/
│   │   │   │	├── useForm.js
│   │   │   │	└── useDebounce.js
│   │   │	├── styles/
│   │   │   │	└── main.css
│   │   │	└── utils/     
│   │   │   	├── constants.js
│   │   │		└── validators.js               
│   │	├── services/                                    # API call abstraction
│   │   │	└── api.js                     
│  	│	├── context/                                     # Global state 
│   │   │	└── globalAppContext.js 
│   │	├── hooks/                                       # Custom Reusable hooks
│   │   │	├── useAuth.js
│   │   │	├── useForm.js
│   │   │	└── userBooking.js 
│   │	├── styles/                                      # Global and scoped CSS
│   │   │	├── main.css
│   │   │	├── dashboard.css
│   │   │	└── room.css
│   │	├── utils/                                       # Utility functions and constants
│   │   │	├── constants.js
│   │   │	└── validators.js
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
