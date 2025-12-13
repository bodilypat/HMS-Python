Fullstack-Hotel-Management-System/
│
backend/   
├── manage.py                           
├── requirements.txt            
├── app/      
│   ├── core/                          
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── security.py
│   │   ├── loggers.py
│   │   └── exceptions.py          
│   ├── api/                                                # REST endpoints      
│   │   ├── v1/
│   │   │   ├── auth.py
│   │   │   │   ├── router.py
│   │   │   │   └── deoendencies.py
│   │   │   ├── rooms/
│   │   │   │   ├── router.py
│   │   │   │   ├── rooms.py
│   │   │   │   ├── room_types.py
│   │   │   │   ├── amenities.py
│   │   │   │   └── availability.py
│   │   │   ├── bookings.py     
│   │   │   │   ├── router.py
│   │   │   │   ├── bookings.py
│   │   │   │   ├── representation.py
│   │   │   │   └── payments.py
│   │   │   ├── guests.py  
│   │   │   │   ├── router.py
│   │   │   │   └── guests.py     
│   │   │   ├── staff.py 
│   │   │   │   ├── router.py
│   │   │   │   └── staff.py 
│   │   │   ├── services/
│   │   │   │   ├── router.py
│   │   │   │   └── services.py        
│   │   │   ├── billings/
│   │   │   │   ├── router.py
│   │   │   │   └── billings.py
│   │   │   ├── reports/
│   │   │   │   ├── router.py
│   │   │   │   └── reports.py    
│   │   │   └── __init__.py   
│   │   │                                                        
│   │   └── api_router.py      
│   │  
│   ├── models/                                        # SQLAlchemy  models (tables)
│   │   ├── base.py                          
│   │   ├── auth.py                       
│   │   ├── rooms.py                          
│   │   ├── bookings.py              
│   │   ├── guests.py          
│   │   ├── staff.py
│   │   ├── hotel_services.py
│   │   ├── billings.py                                  
│   │   └── reports.py    
│   │                   
│   ├── schemas/                                      # Pydantic models(validation & serialization)
│   │   ├── common.py                          
│   │   ├── auth.py                                
│   │   ├── rooms.py                           
│   │   ├── bookings.py                      
│   │   ├── guests.py                  
│   │   ├── staff.py
│   │   ├── services
│   │   ├── billings                            
│   │   └── reports   
│   │  
│   ├── crud/                                           # Database Logic 
│   │   ├── base.py                          
│   │   ├── auth.py                       
│   │   ├── rooms.py                          
│   │   ├── bookings.py              
│   │   ├── guests.py          
│   │   ├── staff.py
│   │   ├── hotel_services.py
│   │   ├── billings.py                                  
│   │   └── reports.py   
│   │                                  
│   ├── services/                                    # Business Logic
│   │   ├── __init__.py                          
│   │   ├── auth/
│   │   │   ├── auth_service.py
│   │   │   └── token_service.py                                            
│   │   ├── rooms/  
│   │   │   ├── room_service.py
│   │   │   ├── room_type_service.py
│   │   │   ├── amenity_service.py
│   │   │   └── availability_service.py                                   
│   │   ├── bookings/ 
│   │   │   ├── booking_service.py
│   │   │   ├── reservation_service.py
│   │   │   └── payment_service.py                             
│   │   ├── guests/  
│   │   │   └── guest_service.py                             
│   │   ├── staff/
│   │   │   └── staff_service.py
│   │   ├── hotel_services/
│   │   │   ├── additional_service.py
│   │   │   └── room_service_log.py
│   │   ├── billings/ 
│   │   │   └── billing_service.py                                    
│   │   └── reports/
│   │       └── report_service.py  
│   │                              
│   ├── utils/                         
│   │   ├── pagination.py
│   │   ├── datetime.py
│   │   └── helpers.py
│   │
│   ├── events/                         
│   │   ├── auth_middleware.py
│   │   └── rate_limit.py
│   ├── main.py                                        # App entrypoint (FastAPI/Flask/Django)
│   └── __init__.py               
└── .env
│            
/frontend/
├── public/
│   └── index.html
├── src/
│   ├── api/                          # For raw HTTP endpoints
│   │   ├── axiosConfig.js            # axios instance + interceptors (auth token, error handling)
│   │   ├── index.js                  # central re-exports for all API modules
│   │   ├── authApi.js                # auth: login, refresh, logout, password flows
│   │   ├── guestApi.js               # guest CRUD & lookup endpoints
│   │   ├── roomApi.js                # room endpoints (availability, status, details)
│   │   ├── bookingApi.js             # booking flows (create, modify, checkin/checkout)
│   │   ├── paymentApi.js             # payment orchestration, refunds, gateway adapters
│   │   ├── staffApi.js               # Staff CRUD, roles. permissions
│   │   └── settingApi.js             # auth: login, refresh, logout, password flows
│   ├── services/                     # Business Logic
│   │   ├── index.js                  # re-export service layer
│   │   ├── authService.js            # higher-level auth flows (token refresh, session management)
│   │   ├── guestService.js           # guest helper functions (dedupe, format)
│   │   ├── bookingService.js         # business logic: validation, mapping, orchestration with APIs
│   │   ├── roomService.js            # availability checks, pricing composition
│   │   ├── paymentService.js         # payment orchestration & retry logic
│   │   └── staffService.js           # staff-related business rules & permission helpers
│   ├── assets/
│   │   ├── icons/
│   │   ├── images/
│   │   └── fonts/
│   ├── components/
│   │   ├── ui/
│   │   │   ├── Avatar.jsx                     
│   │   │   ├── Badge.jsx
│   │   │   ├── Button.jsx       
│   │   │   ├── Card.jsx
│   │   │   ├── Chip.jsx
│   │   │   ├── Divider.jsx
│   │   │   ├── IconButton.jsx
│   │   │   ├── Spinner.jsx
│   │   │   ├── Alert.jsx
│   │   │   ├── Tooltip.jsx
│   │   │   └── index.js
│   │   ├── common/
│   │   │   ├── SearchBar.jsx
│   │   │   ├── FilterPanel.jsx
│   │   │   ├── Breadcrumb.jsx
│   │   │   ├── EmptyState.jsx
│   │   │   ├── ConfirmationDialog.jsx
│   │   │   ├── Notification.jsx
│   │   │   └── index.js
│   │   ├── layout/
│   │   │   ├── Layout.jsx                      # main layout wrapper (Header / Sidebar / Footer)
│   │   │   ├── Sidebar.jsx
│   │   │   ├── Navbar.jsx
│   │   │   ├── Header.jsx
│   │   │   ├── Footer.jsx
│   │   │   └── index.js
│   │   ├── forms/                               
│   │   │   ├── Input.js
│   │   │   ├── Select.jsx
│   │   │   ├── TextArea.jsx
│   │   │   ├── CheckBox.jsx
│   │   │   ├── RadioGroup.jsx
│   │   │   ├── DateInput.jsx
│   │   │   ├── FormGroup.jsx 
│   │   │   ├── FormSelect.jsx     
│   │   │   ├── ErrorMessage.jsx  
│   │   │   ├── utils/   
│   │   │   │   └── validators.js              
│   │   │   └── index.js                   
│   │   ├── tables/
│   │   │   ├── Table/
│   │   │   │   ├── Table.jsx
│   │   │   │   ├── TableHeader.jsx
│   │   │   │   ├── TableBody.jsx
│   │   │   │   ├── TableRow.jsx
│   │   │   │   ├── TableCell.jsx
│   │   │   │   ├── TableEmpty.jsx
│   │   │   │   ├── TableLoading.jsx
│   │   │   │   ├── TableFooter.jsx
│   │   │   │   └── index.jsx   
│   │   │   ├── Pagination/
│   │   │   │   ├── PaginationTable.jsx
│   │   │   │   └── PaginationControls.jsx   
│   │   │   ├── Filters/
│   │   │   │   └── FilterTable.jsx   
│   │   │   ├── Sort/
│   │   │   │   └── SortTable.jsx   
│   │   │   └── index.js
│   │   └── index.js
│   ├── pages/
│   │   ├── Auth/
│   │   │   ├── Login.jsx
│   │   │   ├── Register.jsx
│   │   │   ├── ForgotPassword.jsx
│   │   │   └── ResetPassword.jsx
│   │   ├── Dashboard/
│   │   │   ├── Dashboard.jsx
│   │   │   ├── OverviewWidget.jsx
│   │   │   ├── StatsCards.jsx
│   │   │   └── Dashboard.module.css
│   │   ├── Guests/
│   │   │   ├── GuestsList.jsx
│   │   │   ├── GuestDetail.jsx
│   │   │   ├── GuestCreate.jsx
│   │   │   └── GuestEdit.jsx
│   │   ├── Bookings/
│   │   │   ├── BookingList.jsx
│   │   │   ├── BookingDetail.jsx
│   │   │   ├── BookingForm.jsx
│   │   │   ├── CheckIn.jsx
│   │   │   ├── CheckOut.jsx
│   │   │   └── BookingCalendar.jsx
│   │   ├── Rooms/
│   │   │   ├── RoomsList.jsx
│   │   │   ├── RoomDetail.jsx
│   │   │   ├── RoomForm.jsx
│   │   │   ├── RoomTypeList.jsx
│   │   │   ├── RoomTypeForm.jsx
│   │   │   └── RoomAmenities.jsx
│   │   ├── Staffs/
│   │   │   ├── StaffList.jsx
│   │   │   ├── StaffForm.jsx
│   │   │   └── StaffDetail.jsx
│   │   ├── payments/
│   │   │   ├── Payments.jsx
│   │   │   ├── PaymentDetail.jsx
│   │   │   └── PaymentForm.jsx
│   │   └── Settings/
│   │       ├── HotelInfo.jsx
│   │       ├── Integrations.jsx
│   │       ├── RolesAndPermissions.jsx
│   │       ├── UserManagement.jsx
│   │       └── Settings.module.css
│   ├── styles/
│   │   ├── index.css
│   │   ├── variables.css
│   │   ├── layout.css
│   │   ├── table.css
│   │   ├── modal.css
│   │   └── forms.css
│   ├── utils/
│   │   ├── index.js                                # re-export utilities
│   │   ├── formatDate.js
│   │   ├── calculatePrice.js
│   │   ├── generateInvoiceNumber.js
│   │   └── validators.js
│   ├── hooks/                                     # consolidate hooks used across components
│   │   ├── index.js
│   │   ├── useFetch.js
│   │   ├── useAuth.js
│   │   ├── useForm.js
│   │   ├── useToggle.js
│   │   └── useDebounce.js
│   ├── router/
│   │   ├── AppRoutes.jsx
│   │   └── ProtectedRoute.jsx
│   ├── __tests__/                                 # component-level integration tests
│   │   ├── components.test.jsx
│   │   └── layout.test.jsx
│   ├── stories/                                   # component-level integration tests
│   │   ├── ui.stories.jsx
│   │   ├── layout.stories.jsx
│   │   └── tables.stories.jsx
│   ├── App.js
│   └── index.jsx / main.jsx
├── tests/
│   ├── pages/
│   └── components/
├── .env.example
├── package.json
└── README.md