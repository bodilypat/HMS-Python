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
│   │   └── logger.py 
│   ├── models/
│   │   ├── __init__.py                      # exports commonly used models & helper factories
│   │   ├── base.py                          # Base SQLModel / ORM base + Timestamp/ID mixins
│   │   ├── mixins.py                        # SoftDeleteMixin, AuditMixin, Versioning helper
│   │   ├── enums.py                         # shared Enums (RoomStatus, BookingStatus, PaymentStatus)
│   │   ├── indexes.py                       # centralised DB index/constraint definitions
│   │   ├── amenities.py                     # Amenity model & simple helpers
│   │   ├── room_types.py                    # RoomType (capacity, default_rate, relations)
│   │   ├── room_type_amenity.py             # association table: room_type <> amenity
│   │   ├── rooms.py                         # Room model (type_id, status, number, floor)
│   │   ├── room_price.py                    # Seasonal and override pricing rules
│   │   ├── users.py                         # User model (auth fields, roles, last_login)
│   │   ├── guests.py                        # Guest profile (contact, loyalty_id)
│   │   ├── staffs.py                        # Staff profile (roles, permissions metadata)
│   │   ├── reservations.py                  # Reservation/hold model (availability window)
│   │   ├── bookings.py                      # Booking model (checkin/checkout, status, invoice ref)
│   │   ├── room_service.py                  # On-room orders (items, status, assigned_staff)
│   │   ├── payments.py                      # Payment records (gateway metadata, status, retries)
│   │   ├── billings.py                      # Invoice, line items, adjustments, taxes
│   │   └── README.md                        # model design notes, relationships, migration tips
│   ├── schemas/                                    # Pydantic/Serializers (organized, versioned, reusable)
│   │   ├── __init__.py                             # exports and version aliases
│   │   ├── base.py                                 # BaseModel config (orm_mode, timestamps, id mixins)
│   │   ├── common.py                               # shared types, enums, helper validators
│   │   ├── pagination.py                           # paging request/response schemas
│   │   ├── response.py                             # standard API envelope / error models
│   │   ├── auth_schema.py                          # login, token, refresh, password flows
│   │   ├── amenity_schema.py                       # CreateAmenity / UpdateAmenity / AmenityOut
│   │   ├── room_type_schema.py                     # Create/Update/Out + amenity refs
│   │   ├── room_schema.py                          # Create/Update/Out + availability DTOs
│   │   ├── room_price_schema.py                    # seasonal/override pricing request/responses
│   │   ├── user_schema.py                          # profile, create/update, role claims
│   │   ├── guest_schema.py                         # guest profile, lookup, loyalty DTOs
│   │   ├── staff_schema.py                         # staff create/update + role assignment
│   │   ├── reservation_schema.py                   # hold, availability request/response
│   │   ├── booking_schema.py                       # booking create/modify/checkin/out schemas
│   │   ├── service_schema.py                       # hotel service create/update/out
│   │   ├── room_service_schema.py                  # on-room orders request/response
│   │   ├── payment_schema.py                       # payment request/response + gateway metadata
│   │   ├── billing_schema.py                       # invoice, adjustment, line-item schemas
│   │   └── examples/                               # small JSON examples for docs & tests
│   │       ├── amenity_example.json
│   │       ├── booking_example.json
│   │       └── invoice_example.json
│   ├── routes/                                  # API endpoints (Controllers) - organized, versioned and extensible
│   │   ├── __init__.py                          # aggregate and mount routers (e.g. include api_v1 routers)
│   │   ├── base.py                              # shared router helpers / dependencies / response models
│   │   ├── health.py                            # /health, readiness, liveness endpoints
│   │   ├── docs.py                              # custom docs endpoints / swagger redirects
│   │   ├── metrics.py                           # metrics / prometheus exporter endpoint
│   │   ├── webhooks.py                          # external webhook receivers
│   │   │
│   │   ├── api_v1/                              # versioned API (v1) - keeps future upgrades simple
│   │   │   ├── __init__.py                      # register v1 routers and tags
│   │   │   ├── auth_routes.py                   # /api/v1/auth (login, refresh, logout, password flows)
│   │   │   ├── user_routes.py                   # /api/v1/users (profile, CRUD, roles/permissions)
│   │   │   ├── guest_routes.py                  # /api/v1/guests
│   │   │   ├── staff_routes.py                  # /api/v1/staffs (admin-only)
│   │   │   ├── amenities_routes.py              # /api/v1/amenities
│   │   │   ├── room_type_routes.py              # /api/v1/room-types
│   │   │   ├── room_type_amenities_routes.py    # /api/v1/room-types/{id}/amenities (associations)
│   │   │   ├── room_routes.py                   # /api/v1/rooms
│   │   │   ├── room_price_routes.py             # /api/v1/room-prices (seasonal / override pricing)
│   │   │   ├── reservation_routes.py            # /api/v1/reservations (availability checks)
│   │   │   ├── booking_routes.py                # /api/v1/bookings (check-in/out, calendar)
│   │   │   ├── service_routes.py                # /api/v1/services (hotel services)
│   │   │   ├── room_service_routes.py           # /api/v1/room-services (on-room orders)
│   │   │   ├── payment_routes.py                # /api/v1/payments (gateway integrations)
│   │   │   ├── billing_routes.py                # /api/v1/billings (invoices, adjustments)
│   │   │   └── report_routes.py                 # /api/v1/reports (occupancy, revenue, custom)
│   │   │
│   │   └── admin/                               # admin-only grouped routers (optional)
│   │       ├── __init__.py
│   │       ├── admin_staff_routes.py
│   │       ├── admin_user_routes.py
│   │       └── admin_audit_routes.py
│   │
│   ├── services/                             # Business logic separated by domain + helpers
│   │   ├── __init__.py
│   │   ├── README.md                         # how to use services, DI notes, async vs sync
│   │   ├── base_service.py                   # common helpers / base class for services
│   │   ├── interfaces.py                     # service interfaces / protocols for typing & testing
│   │   ├── exceptions.py                     # domain-specific exceptions
│   │   ├── validators.py                     # shared validation utilities
│   │   ├── factory.py                        # service factory / DI bootstrap helpers
│   │   │
│   │   ├── auth/                             # auth-related business logic
│   │   │   ├── __init__.py
│   │   │   ├── auth_service.py               # login, refresh, logout, token ops (async-friendly)
│   │   │   └── password.py                   # hashing, policy, reset helpers
│   │   │
│   │   ├── rooms/                            # room domain logic
│   │   │   ├── __init__.py
│   │   │   ├── room_service.py               # room CRUD, status transitions
│   │   │   └── availability.py               # availability checks, occupancy helpers
│   │   │
│   │   ├── bookings/                         # booking flows & business rules
│   │   │   ├── __init__.py
│   │   │   ├── booking_service.py            # create/cancel/modify bookings, check-in/out
│   │   │   └── checkin_checkout.py           # check-in/out specific logic & validations
│   │   │
│   │   ├── reservations/                     # reservation / hold logic (pre-booking)
│   │   │   ├── __init__.py
│   │   │   ├── reservation_service.py        # availability holds, confirmations, expiries
│   │   │   └── availability_strategy.py      # pluggable strategies for availability rules
│   │   │
│   │   ├── payments/                         # payment processing & gateway adapters
│   │   │   ├── __init__.py
│   │   │   ├── payment_service.py            # payment orchestration, retries, refunds
│   │   │   └── gateways.py                   # adapters for Stripe, Braintree, test gateway
│   │   │
│   │   ├── billing/                          # invoicing & post-stay billing
│   │   │   ├── __init__.py
│   │   │   ├── billing_service.py            # invoice generation, adjustments, credits
│   │   │   └── invoices.py                   # invoice templates, tax & rounding logic
│   │   │
│   │   ├── staff/                            # staff management & RBAC business rules
│   │   │   ├── __init__.py
│   │   │   ├── staff_service.py              # staff CRUD, assignments, permissions
│   │   │   └── roles.py                      # role/permission utilities & checks
│   │   │
│   │   └── guests/                           # guest profiles & loyalty logic
│   │       ├── __init__.py
│   │       ├── guest_service.py              # guest CRUD, lookup, merge duplicates
│   │       └── loyalty.py                    # loyalty points, tiers, redemption rules
│   ├── utils/                         
│   │   ├── auth.py
│   │   ├── validator.py
│   │   ├── response.py
│   │   ├── pagination.py
│   │   ├── date_utils.py
│   │   └── file_upload.py
│   ├── data/
│   │   ├── guests.js
│   │   ├── staffs.js
│   │   ├── room_types.js
│   │   ├── rooms.js
│   │   ├── room_type_amenities.js
│   │   ├── amenities.js
│   │   ├── booking.js
│   │   └── payments.js
│   ├── middleware/                         
│   │   ├── auth_middleware.py
│   │   └── rate_limit.py
│   ├── tasks/                         
│   │   ├── email_docs.py
│   │   └── report_tasks.py
│   ├── docs/                         
│   │   ├── api_docs.md
│   │   └── endpoint_collection.json
│   ├── main.py                                        # App entrypoint (FastAPI/Flask/Django)
│   └── requirements.txt                 
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
│   │   │   ├── Badge.jsx
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
│   │   │   │   ├── TableHead.jsx
│   │   │   │   ├── TableBody.jsx
│   │   │   │   ├── TableRow.jsx
│   │   │   │   ├── TableCell.jsx
│   │   │   │   └── TableEmpty.jsx   
│   │   │   ├── Pagination/
│   │   │   │   └── PaginationTable.jsx   
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