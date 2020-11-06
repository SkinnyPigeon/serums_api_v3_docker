# Imports

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, BigInteger, String, DateTime, Time, Text, Numeric, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import ARRAY, JSON

import os
from dotenv import load_dotenv
from pathlib import Path

project_folder = os.path.expanduser('~/code/api/')
load_dotenv(os.path.join(project_folder, '.env'))
PASSWORD = os.environ.get('PGPASSWORD')

engine = create_engine('postgresql://postgres:{}@localhost:5432/source'.format(PASSWORD), echo='debug')


# Tables/Classes

class FCRB_Diagnostic(Base):
    __tablename__ = 'diagnostic'
    __table_args__ = {'schema': 'fcrb'}
    einri = Column(String)
    patnr = Column(Integer, primary_key=True)
    falnr = Column(String, primary_key=True)
    lfdnr = Column(Integer)
    dkey1 = Column(String)
    pernr = Column(String, primary_key=True)

class FCRB_Episode(Base):
    __tablename__ = 'episode'
    __table_args__ = {'schema': 'fcrb'}
    einri = Column(String)
    falnr = Column(String, primary_key=True)
    falar = Column(String)
    patnr = Column(Integer, primary_key=True)
    bekat = Column(String)
    einzg = Column(String)
    statu = Column(String)
    krzan = Column(String)
    enddt = Column(DateTime(timezone=False))
    erdat = Column(DateTime(timezone=False))
    pernr = Column(String, primary_key=True)
    storn = Column(String)
    begdt = Column(DateTime(timezone=False))
    casetx = Column(String)
    fatnx = Column(String)
    enddtx = Column(String)

class FCRB_Medical_Specialty(Base):
    __tablename__ = 'medical_specialty'
    __table_args__ = {'schema': 'fcrb'}
    orgid = Column(String, primary_key=True)
    orgna = Column(String)

class FCRB_Medication(Base):
    __tablename__ = 'medication'
    __table_args__ = {'schema': 'fcrb'}
    einri = Column(String)
    patnr = Column(Integer, primary_key=True)
    falnr = Column(String, primary_key=True)
    pernr = Column(String, primary_key=True)
    motx = Column(String)
    mostx = Column(String)
    motypid = Column(String)
    mpresnr = Column(String, primary_key=True)
    erdat = Column(DateTime(timezone=False))
    storn = Column(String)
    stusr = Column(String, primary_key=True)
    stdat = Column(DateTime(timezone=False))
    stoid = Column(String)

class FCRB_Monitoring_Parameters(Base):
    __tablename__ = 'monitoring_parameters'
    __table_args__ = {'schema': 'fcrb'}
    patnr = Column(Integer, primary_key=True)
    falnr = Column(String, primary_key=True)
    vppid = Column(String)
    pernr = Column(String, primary_key=True)
    vbem = Column(String)
    datyp = Column(DateTime(timezone=False))
    wertogr = Column(String)
    wertugr = Column(String)
    wertmax = Column(String)
    wertmin = Column(String)

class FCRB_Order_Entry(Base):
    __tablename__ = 'order_entry'
    __table_args__ = {'schema': 'fcrb'}
    einri = Column(String)
    falnr = Column(String, primary_key=True)
    idodr = Column(String, primary_key=True)
    patnr = Column(Integer, primary_key=True)
    pernr = Column(String, primary_key=True)
    erdat = Column(DateTime(timezone=False))
    orgid = Column(String, primary_key=True)

class FCRB_Patient(Base):
    __tablename__ = 'patient'
    __table_args__ = {'schema': 'fcrb'}
    patnr = Column(Integer, primary_key=True)
    gschl = Column(String)
    nname = Column(String)
    vname = Column(String)
    gbdat = Column(DateTime(timezone=False))
    gbnam = Column(String)
    namzu = Column(String)
    glrand = Column(String)
    famst = Column(String)
    telf1 = Column(String)
    rvnum = Column(String)
    decdat = Column(DateTime(timezone=False))

class FCRB_Patient_Address(Base):
    __tablename__ = 'patient_address'
    __table_args__ = {'schema': 'fcrb'}
    patnr = Column(Integer, primary_key=True)
    pstlz = Column(String)
    stras = Column(String)
    land = Column(String)
    ort = Column(String)
    floor = Column(String)
    adrnr = Column(String)

class FCRB_Professional(Base):
    __tablename__ = 'professional'
    __table_args__ = {'schema': 'fcrb'}
    pernr = Column(String, primary_key=True)
    erusr = Column(String)
    orgid = Column(String)
    gbdat = Column(DateTime(timezone=False))
    begdt = Column(DateTime(timezone=False))
    enddt = Column(DateTime(timezone=False))
    erdat = Column(DateTime(timezone=False))
    rank = Column(String)

class FCRB_Serums_IDs(Base):
    __tablename__ = 'serums_ids'
    __table_args__ = {'schema': 'fcrb'}
    serums_id = Column(Integer, primary_key=True)
    patnr = Column(Integer, primary_key=True)

class FCRB_Vital_Signs(Base):
    __tablename__ = 'vital_signs'
    __table_args__ = {'schema': 'fcrb'}
    patnr = Column(Integer, primary_key=True)
    falnr = Column(String, primary_key=True)
    idvs = Column(String, primary_key=True)
    vppid = Column(String)
    dttyp = Column(String)
    erdat = Column(DateTime(timezone=False))
    vptim = Column(Time(timezone=False))
    typevs =Column(String)
    vwert = Column(String)
    vbem = Column(String)

class FCRB_Patient_Rules(Base):
    __tablename__ = 'patient_rules'
    __table_args__ = {'schema': 'fcrb'}
    rule_id = Column(String, primary_key=True)
    tags = Column(ARRAY(String))
    filters = Column(JSON)
    serums_id = Column(Integer)
    
class FCRB_TAGS(Base):
    __tablename__ = 'hospital_tags'
    __table_args__ = {'schema': 'fcrb'}
    id = Column(Integer, primary_key=True)
    tags = Column(ARRAY(String))  

class FCRB_Doctors(Base):
    __tablename__ = 'hospital_doctors'
    __table_args__ = {'schema': 'fcrb'}
    id = Column(Integer, primary_key=True)
    name = Column(String)
    specialism = Column(Integer)

### USTAN

# Tables/Classes

class USTAN_Chemocare(Base):
    __tablename__ = 'chemocare'
    __table_args__ = {'schema': 'ustan'}
    chi = Column(BigInteger, primary_key=True)
    intention = Column(String)
    regime = Column(String)
    appointment_date = Column(DateTime(timezone=False), primary_key=True)
    drug_dose = Column(Integer)
    drug_type = Column(String)
    drug_status = Column(String)
    outcome = Column(String)

class USTAN_Demographics(Base):
    __tablename__ = 'demographics'
    __table_args__ = {'schema': 'ustan'}
    chi	= Column(BigInteger, primary_key=True)
    name = Column(String)
    initial	= Column(String)
    gp_name	= Column(String)
    postcode = Column(String)	
    age	= Column(Integer)
    dat_birth = Column(DateTime(timezone=False), primary_key=True)
    gender = Column(String)
    civil_status = Column(Integer)
    religion = Column(Integer)
    ref_hospital = Column(Integer)
    dat_death = Column(Integer)

class USTAN_Diagnosis(Base):
    __tablename__ = 'diagnosis'
    __table_args__ = {'schema': 'ustan'}
    chi	= Column(BigInteger, primary_key=True)
    first_seen_date	= Column(DateTime(timezone=False), primary_key=True)
    primary_field = Column(Integer)
    age	= Column(Integer)
    site = Column(String)
    side = Column(Integer)
    histology = Column(Integer)
    stage = Column(String)
    tnm_t = Column(String)
    tnm_n = Column(String)
    tnm_m = Column(String)
    perf_stat = Column(String)
    metastasis1 = Column(String)

class USTAN_Smr01(Base):
    __tablename__ = 'smr01'
    __table_args__ = {'schema': 'ustan'}
    chi	= Column(BigInteger, primary_key=True)
    incidence_date = Column(DateTime(timezone=False), primary_key=True)
    admission_date = Column(DateTime(timezone=True))
    length_of_stay = Column(Integer)
    main_condition = Column(String)	
    other_condition1 = Column(String)
    other_condition2 = Column(String)	
    other_condition3 = Column(String)	
    main_operation_a = Column(String)
    main_operation_b = Column(String)	
    discharge_date = Column(DateTime(timezone=False))	
    waiting_list_type = Column(Integer)	
    marital_status = Column(String)
    ethnic_group = Column(String)

    

class USTAN_Serums_IDs(Base):
    __tablename__ = 'serums_ids'
    __table_args__ = {'schema': 'ustan'}
    serums_id = Column(Integer, primary_key=True)
    chi = Column(BigInteger, primary_key=True)

class USTAN_Patient_Rules(Base):
    __tablename__ = 'patient_rules'
    __table_args__ = {'schema': 'ustan'}
    rule_id = Column(String, primary_key=True)
    tags = Column(ARRAY(String))
    filters = Column(JSON)
    serums_id = Column(Integer)

class USTAN_TAGS(Base):
    __tablename__ = 'hospital_tags'
    __table_args__ = {'schema': 'ustan'}
    id = Column(Integer, primary_key=True)
    tags = Column(ARRAY(String)) 

class USTAN_Doctors(Base):
    __tablename__ = 'hospital_doctors'
    __table_args__ = {'schema': 'ustan'}
    id = Column(Integer, primary_key=True)
    name = Column(String)
    specialism = Column(Integer)



### ZMC 

# Tables/Classes

class ZMC_Wearable(Base):
    __tablename__ = 'wearable'
    __table_args__ = {'schema': 'zmc'}
    patnr = Column(Integer, primary_key=True)
    day_nr = Column(Integer, primary_key=True)
    time_total = Column(Integer)
    time_passive = Column(Integer)
    time_active = Column(Integer)
    time_sit = Column(Integer)
    time_stand = Column(Integer)
    time_walk = Column(Integer)
    time_cycle = Column(Integer)
    time_hi = Column(Integer)
    nr_sst = Column(Integer)
    steps_total = Column(Integer)
    cadence = Column(Integer)
    cyc_rot = Column(Integer)
    cyc_rpm = Column(Integer)

class ZMC_Patient_Details(Base):
    __tablename__ = 'patient_details'
    __table_args__ = {'schema': 'zmc'}
    patnr = Column(Integer, primary_key=True)
    gschl = Column(String)
    nname = Column(String)
    nnams = Column(String)
    vname = Column(String)
    titel = Column(String)
    namzu = Column(String)
    gbdat = Column(DateTime(timezone=False))
    gbnam = Column(String)
    gbnas = Column(String)
    gland = Column(String)
    natio = Column(String)
    land = Column(String)
    pstlz = Column(String)
    ort = Column(String)
    stras = Column(String)
    telf1 = Column(String)

class ZMC_Patient_Measurements(Base):
    __tablename__ = 'patient_measurements'
    __table_args__ = {'schema': 'zmc'}
    patnr = Column(Integer, primary_key=True)
    height = Column(Integer)
    weight = Column(Integer)
    date = Column(DateTime(timezone=False))

class ZMC_Documents(Base):
    __tablename__ = 'patient_documents'
    __table_args__ = {'schema': 'zmc'}
    patnr = Column(Integer, primary_key=True)
    report_title = Column(String, primary_key=True)
    department = Column(String)
    date = Column(DateTime(timezone=False))
    content = Column(Text)

class ZMC_Serums_IDs(Base):
    __tablename__ = 'serums_ids'
    __table_args__ = {'schema': 'zmc'}
    serums_id = Column(Integer, primary_key=True)
    patnr = Column(Integer, primary_key=True)

class ZMC_Patient_Rules(Base):
    __tablename__ = 'patient_rules'
    __table_args__ = {'schema': 'zmc'}
    rule_id = Column(String, primary_key=True)
    tags = Column(ARRAY(String))
    filters = Column(JSON)
    serums_id = Column(Integer)

class ZMC_Appointments(Base):
    __tablename__ = 'patient_appointments'
    __table_args__ = {'schema': 'zmc'}
    patnr = Column(Integer, primary_key=True)
    type = Column(String, primary_key=True)
    date = Column(DateTime(timezone=False))
    notes = Column(Text)

class ZMC_Operations(Base):
    __tablename__ = 'patient_operations'
    __table_args__ = {'schema': 'zmc'}
    patnr = Column(Integer, primary_key=True)
    anatomical_location = Column(String)
    date = Column(DateTime(timezone=False))
    notes = Column(Text)

class ZMC_Warnings(Base):
    __tablename__ = 'patient_warnings'
    __table_args__ = {'schema': 'zmc'}
    patnr = Column(Integer, primary_key=True)
    alerts = Column(String)
    begin_date = Column(DateTime(timezone=False))
    type = Column(String)

class ZMC_Functional_State(Base):
    __tablename__ = 'patient_functional_state'
    __table_args__ = {'schema': 'zmc'}
    patnr = Column(Integer, primary_key=True)
    name = Column(String)
    value = Column(String)
    date = Column(DateTime(timezone=False))

class ZMC_Living_Situation(Base):
    __tablename__ = 'patient_living_situation'
    __table_args__ = {'schema': 'zmc'}
    patnr = Column(Integer, primary_key=True)
    house_type = Column(String)
    description = Column(String)

class ZMC_Drug_Use(Base):
    __tablename__ = 'patient_drug_use'
    __table_args__ = {'schema': 'zmc'}
    patnr = Column(Integer, primary_key=True)
    substance = Column(String)
    quantity = Column(String)
    description = Column(String)

class ZMC_Alcohol_Use(Base):
    __tablename__ = 'patient_alcohol_use'
    __table_args__ = {'schema': 'zmc'}
    patnr = Column(Integer, primary_key=True)
    usage_status = Column(String)
    quantity = Column(String)
    description = Column(String)

class ZMC_Tobacco_Use(Base):
    __tablename__ = 'patient_tobacco_use'
    __table_args__ = {'schema': 'zmc'}
    patnr = Column(Integer, primary_key=True)
    substance = Column(String)
    description = Column(String)

class ZMC_Allergies(Base):
    __tablename__ = 'patient_allergies_intolerance'
    __table_args__ = {'schema': 'zmc'}
    patnr = Column(Integer, primary_key=True)
    caustic_substance = Column(String)
    critical = Column(String)
    description = Column(String)

class ZMC_Diagnostic(Base):
    __tablename__ = 'patient_diagnostic'
    __table_args__ = {'schema': 'zmc'}
    patnr = Column(Integer, primary_key=True)
    type = Column(String)
    name = Column(String)
    anatomical_location = Column(String)
    laterality = Column(String)
    begin_date = Column(DateTime(timezone=False))
    end_date = Column(DateTime(timezone=False))

class ZMC_TAGS(Base):
    __tablename__ = 'hospital_tags'
    __table_args__ = {'schema': 'zmc'}
    id = Column(Integer, primary_key=True)
    tags = Column(ARRAY(String)) 

class ZMC_Doctors(Base):
    __tablename__ = 'hospital_doctors'
    __table_args__ = {'schema': 'zmc'}
    id = Column(Integer, primary_key=True)
    name = Column(String)
    specialism = Column(Integer)

Base.metadata.create_all(engine)