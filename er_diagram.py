import graphviz

# Define the ER diagram using Graphviz DOT Language 
er = graphviz.Digraph(format='png')
er.attr(rankdir='LR', size='8')

# Patients table 
er.node('Patients', '''{
        patient_id(PK)
        first_name
        last_name
        date_of_birth
        gender
        phone
        email
        address
        date_registered
    }''', shape='record')

# Departments table 
er.node('Departments', '''{
        department_id (PK)
        name
        description
    }''',shape='record')

# Doctors table
er.node('Doctors', '''{
        doctor_id (PK)
        first_name 
        last_name 
        specialization
        phone
        email
        department_id (FK)
    }''',shape='record')
# Appointments table
er.node('Appointments', '''{
        appointment_id (PK)
        patient_id (FK)
        doctor_id (FK)
        appointement_date
        reason 
        status
    }''', shape='record')
# Medical_records table
er.node('MedicalRecords', '''{
        record_id (PK)
        patient_id (FK)
        doctor_id (FK)
        visit_date
        diagnosis 
        notes 
    }''', shape='record')
# Prescriptions table
er.node('Prescriptions', '''{
        prescription_id (PK)
        record_id (FK)
        medication_name
        dosage 
        duration
    }''', shape='record')
# Billing table
er.node('Billing', '''{
        billing_id (PK)
        patient_id (FK)
        appointment_id (FK)
        amount 
        status 
        date_issued 
    }''', shape='record')

# Relationship
er.edge('Doctors', 'Departments', label='belongs to')
er.edge('Appointments', 'Patients', label='for')
er.edge('Appointments', 'Doctors', label='with')
er.edge('MedicalRecords', 'Patient', label='belong_to')
er.edge('MedicationRecords', 'Doctors', label="written_by")
er.edge('Prescriptions', 'MedicalRecords', label='prescribed in')
er.edge('Billing', 'Patients', label='for')
er.edge('Billing', 'Appointment', label='linked to')

# Render the diagram
er.edge('medical_management_er_diagram', view=True)