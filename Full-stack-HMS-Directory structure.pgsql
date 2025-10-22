Fullstack-Hotel-Management-System/
├── backend/                              
│   │     
│   ├── app/                           
│   │   ├── __init__.py     									 # FastAPI app entry point
│   │   ├── run.py       
│   │   ├── models.py          
│   │   ├── auth.py              								 # Authentication logic 
│   │	├── routes/                               
│   │   │	└── protected.py                                     # Routes requiring logic 
│   │	├── core/                                            	 # Core infra: security, auth, etc.
│   │   │	├── __init__.py                             
│   │   │	├── auth.py                                      	 # JWT, OAuth, etc.
│   │   │	└── hashing.py                                   	 # Password hashing utilities
│   │   │
│   │   ├── api/                                      		 	 # FastAPI routers (grouped by domain)
│   │   │   ├── __init__.py   
│   │   │   ├── api_router.py                                	 # Aggregates end registers all router
│   │   │   ├── core/  
│   │   │   │	├── __init__.py
│   │   │   │   ├── user_router.py
│   │   │   │   ├── guest_router.py
│   │   │   │   └── staff_router.py 
│   │   │   ├── room/  
│   │   │   │	├── __init__.py
│   │   │   │   ├── room_router.py
│   │   │   │   ├── category_router.py
│   │   │   │   ├── availability_router.py
│   │   │   │   ├── amenity_router.py
│   │   │   │   └── room_price_router.py   
│   │   │   ├── booking/
│   │   │   │	├── __init__.py
│   │   │   │   ├── booking_router.py
│   │   │   │   ├── reservation_router.py
│   │   │   │   ├── availability_check_router.py
│   │   │   │   └── history_router.py  
│   │   │   ├── finance/
│   │   │   │	├── __init__.py
│   │   │   │   ├── billing_router.py
│   │   │   │   ├── payment_router.py
│   │   │   │   ├── invoice_router.py
│   │   │   │   ├── transaction_router.py
│   │   │   │   └── discount_router.py  
│   │   │   ├── amenities/ 
│   │   │   │	├── __init__.py
│   │   │   │   ├── hotel_amenity_router.py
│   │   │   │   └── room_amenity_router.py
│   │   │   └── feedback/
│   │   │   	├── __init__.py
│   │   │       └── feedback_router.py     
│   │   │   
│   │	├── services/                                         # Bussiness logic between controllers and DB
│   │   │	├── __init__.py  
│   │   │   ├── core/  
│   │   │   │	├── __init__.py
│   │   │   │   ├── user_service.py
│   │   │   │   ├── guest_servive.py
│   │   │   │   └── staff_service.py   
│   │   │   ├── room/  
│   │   │   │	├── __init__.py
│   │   │   │   ├── room_service.py
│   │   │   │   ├── category_service.py
│   │   │   │   ├── availability_service.py
│   │   │   │   ├── amenity_service.py
│   │   │   │   └── room_price_service.py   
│   │   │   ├── booking/
│   │   │   │	├── __init__.py
│   │   │   │   ├── booking_service.py
│   │   │   │   ├── reservation_service.py
│   │   │   │   ├── availability_check_service.py
│   │   │   │   └── history_service.py  
│   │   │   ├── finance/
│   │   │   │	├── __init__.py
│   │   │   │   ├── billing_service.py
│   │   │   │   ├── payment_service.py
│   │   │   │   ├── invoice_service.py
│   │   │   │   ├── transaction_service.py
│   │   │   │   └── discount_service.py
│   │   │   ├── amenities/ 
│   │   │   │	├── __init__.py
│   │   │   │   ├── hotel_amenity_service.py
│   │   │   │   └── room_amenity_service.py   
│   │   │   └── feedback/
│   │   │   	├── __init__.py
│   │   │       └── feedback.py         
│   │	├── models/                                          # SQLAlchemy ORM models       
│   │	│   ├── __init__.py            
│   │	│   ├── core/   
│   │   │   │	├── __init__.py        
│   │   │   │   ├── user.py
│   │   │   │   ├── guest.py
│   │   │   │   └── staff.py
│   │   │   ├── room/
│   │   │   │	├── __init__.py
│   │   │   │   ├── room.py
│   │   │   │   ├── category.py
│   │   │   │   ├── availability.py
│   │   │   │   ├── amenity.py
│   │   │   │   └── room_price.py
│   │   │   ├── booking/
│   │   │   │	├── __init__.py
│   │   │   │   ├── booking.py
│   │   │   │   ├── reservation.py
│   │   │   │   ├── availability.py
│   │   │   │   └── history.py
│   │   │   ├── finance/
│   │   │   │	├── __init__.py
│   │   │   │   ├── billing.py
│   │   │   │   ├── payment.py
│   │   │   │   ├── invoice.py
│   │   │   │   ├── transaction.py
│   │   │   │   └── discount.py
│   │   │   ├── amenities/
│   │   │   │	├── __init__.py
│   │   │   │   ├── hotel_amenity.py
│   │   │   │   └── room_amenity.py
│   │   │   └── feedback/
│   │   │   	├── __init__.py
│   │   │       └── feedback.py
│   │   │  
│   │   ├── schemas/                                           # All Pydantic schemas 
│   │   │   ├── __init__.py                     
│   │   │   ├── core/  
│   │   │   │	├── __init__.py
│   │   │   │   ├── user_schema.py
│   │   │   │   ├── guest_schema.py
│   │   │   │   └── staff_schema.py   
│   │   │   ├── room/  
│   │   │   │	├── __init__.py
│   │   │   │   ├── room_schema.py
│   │   │   │   ├── category_schema.py
│   │   │   │   ├── availability_schema.py
│   │   │   │   ├── amenity_schema.py
│   │   │   │   └── room_pricing_schema.py  
│   │   │   ├── booking/
│   │   │   │	├── __init__.py
│   │   │   │   ├── booking_schema.py
│   │   │   │   ├── reservation_schema.py
│   │   │   │   ├── availability_check_schema.py
│   │   │   │   └── history_schema.py
│   │   │   ├── finance/
│   │   │   │	├── __init__.py
│   │   │   │   ├── billing_schema.py
│   │   │   │   ├── payment_schema.py
│   │   │   │   ├── invoice_schema.py
│   │   │   │   ├── transaction_schema.py
│   │   │   │   └── discount_schema.py
│   │   │   ├── amenities/ 
│   │   │   │	├── __init__.py
│   │   │   │   ├── hotel_amenity_schema.py
│   │   │   │   └── room_amenity_schema.py
│   │   │   └── feedback/
│   │   │   	├── __init__.py
│   │   │       └── feedback_schema.py           
│   │   │
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
│   │   	├── reservation/ 
│   │   	│   └── test_servation.py
│   │   	├── room/ 
│   │   	│   └── test_room.py
│   │   	└── user/    
│   │           └── test_user.py                
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
