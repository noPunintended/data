def conditions(words):
        if words[1]=="1A":
            words.insert(2, "Spinal Disorders (non-traumatic)")
        elif words[1]=="1B":
            words.insert(2, "Cerebral Palsy")
        elif words[1]=="1C":
            words.insert(2, "Neoplasm")
        elif words[1]=="1D":
            words.insert(2, "Degenerative Disorders")
        elif words[1]=="1E":
            words.insert(2, "Multiple Sclerosis and Cerebellar Ataxia")
        elif words[1]=="1F":
            words.insert(2, "Specific Cerebrovascular Disorders Except TIA")
        elif words[1]=="1G":
            words.insert(2, "Transient Ischemic Attack and Precerebral Occlusions")
        elif words[1]=="1H":
            words.insert(2, "Nonspecific Cerebrovascular Diseases")
        elif words[1]=="1I":
            words.insert(2, "Cranial and Peripheral Nerve Disorders")
        elif words[1]=="1J":
            words.insert(2, "Cranial and Peripheral Nerve Disorders")
        elif words[1]=="1K":
            words.insert(2, "Infections Except Viral Meningitis")
        elif words[1]=="1L":
            words.insert(2, "Viral Meningitis")
        elif words[1]=="1M":
            words.insert(2, "Nontraumatic Stupor and Coma")
        elif words[1]=="1N":
            words.insert(2, "Febrile Convulsions")
        elif words[1]=="1P":
            words.insert(2, "Seizure Disorders")
        elif words[1]=="1Q":
            words.insert(2, "Headaches")
        elif words[1]=="1R":
            words.insert(2, "Intracranial Injury")
        elif words[1]=="1S":
            words.insert(2, "Skull Fractures")
        elif words[1]=="1T":
            words.insert(2, "Other Head Injury")
        elif words[1]=="1U":
            words.insert(2, "Other Disorders of Nervous System")
        elif words[1]=="1V":
            words.insert(2, "Guillain-Barre Syndrome")
        elif words[1]=="1W":
            words.insert(2, "Spinal Injuries")
        elif words[1]=="1PK":
            words.insert(2, "Multiple Craniotomy ")
        elif words[1]=="1PL":
            words.insert(2, "Plasmapheresis")
        elif words[1]=="1PH":
            words.insert(2, "Intracranial Vasc Procedures")
        elif words[1]=="1PJ":
            words.insert(2, "Endovasc Procedures")
        elif words[1]=="1PB":
            words.insert(2, "Craniotomy")
        elif words[1]=="1PC":
            words.insert(2, "Spinal Procedures")
        elif words[1]=="1PD":
            words.insert(2, "Extracranial Vascular Procedures")
        elif words[1]=="1PE":
            words.insert(2, "Carpal Tunnel Release")   
        elif words[1]=="1PF" or words[1]=="1PG":
                words.insert(2, "Peripheral & Cranial Nerve & Other Nervous System Procedures")      
        elif words[1]=="2PK":
            words.insert(2, "Multiple Major Lens")
        elif words[1]=="2PL":
            words.insert(2, "Multiple Other Lens")
        elif words[1]=="2PE":
            words.insert(2, "Major Lens")
        elif words[1]=="2PM":
            words.insert(2, "Major Procedures for Lacrimal System")
        elif words[1]=="2PD":
            words.insert(2, "Intraoc Procedures Except lens & Retina")
        elif words[1]=="2PF":
            words.insert(2, "Other Lens")
        elif words[1]=="2PG":
            words.insert(2, "Other Eye Procedures")
        elif words[1]=="2C":
            words.insert(2, "Hyphema and Trauma")
        elif words[1]=="2A":
            words.insert(2, "Acute Major Infections")
        elif words[1]=="2E":
            words.insert(2, "Malignancy")
        elif words[1]=="2B":
            words.insert(2, "Neurological & Vasc Disorders")
        elif words[1]=="2D":
            words.insert(2, "Other Disorders of the Eye")
        elif words[1]=="3PA":
            words.insert(2, "Major Head and Neck Procedures")
        elif words[1]=="3PP":
            words.insert(2, "Minor Head and Neck Procedures")
        elif words[1]=="3PL":
            words.insert(2, "Ear and Other Head and Neck Procedures")
        elif words[1]=="3A":
            words.insert(2, "Malignancy")
        elif words[1]=="3B":
            words.insert(2, "Ear Diseases and Balance")
        elif words[1]=="3C":
            words.insert(2, "Nose, Mouth, Throat and Larynx Diseases")
        elif words[1]=="3H":
            words.insert(2, "Dental Oral and Jaw Disorders")
        elif words[1]=="4PA":
            words.insert(2, "Major Chest")
        elif words[1]=="4PF":
            words.insert(2, "Major Thoracoscopic Procedure")
        elif words[1]=="4PG":
            words.insert(2, "DiagnosticThoracoscopic Procedure")
        elif words[1]=="4PB":
            words.insert(2, "Other Respiratory System Procedures")
        elif words[1]=="4PD":
            words.insert(2, "Ventilator Support")
        elif words[1]=="4PE":
            words.insert(2, "Noninvasive Ventilation")
        elif words[1]=="4PC":
            words.insert(2, "Other Minor Respiratory System Procedures")
        elif words[1]=="4B":
            words.insert(2, "Pulmonary Embolism")
        elif words[1]=="4C":
            words.insert(2, "Respiratory Infection/Inflammation")
        elif words[1]=="4D":
            words.insert(2, "Sleep Apnea")
        elif words[1]=="4E":
            words.insert(2, "Pulmonary Edema and Respiratory Failure")
        elif words[1]=="4F":
            words.insert(2, "COPD")
        elif words[1]=="4G":
            words.insert(2, "Major Chest Trauma")
        elif words[1]=="4H":
            words.insert(2, "Respiratory Signs and Symptoms")
        elif words[1]=="4J":
            words.insert(2, "Pneumothorax")
        elif words[1]=="4K":
            words.insert(2, "Bronchitis and Asthma and Whooping Cough")
        elif words[1]=="4M":
            words.insert(2, "Respiratory Neoplasms")
        elif words[1]=="4R":
            words.insert(2, "Pyothorax")
        elif words[1]=="4N":
            words.insert(2, "Pleural Effusion and Other Pleura Conditions")
        elif words[1]=="4P":
            words.insert(2, "Interstitial Lung Diseases")
        elif words[1]=="4Q":
            words.insert(2, "Other Respiratory System Diagnosis")
        elif words[1]=="5PE":
            words.insert(2, "Thoracoabdominal Procedures Combination")
        elif words[1]=="5PC":
            words.insert(2, "Coronary Bypass")
        elif words[1]=="5PX":
            words.insert(2, "Complex Cardiothoracic Procedures")
        elif words[1]=="5PV":
            words.insert(2, "Multiple Valve Procedures")
        elif words[1]=="5PA":
            words.insert(2, "Valve Replacement and Open Valvuloplasty")
        elif words[1]=="5PD":
            words.insert(2, "Other Cardiothoracic Procedures")
        elif words[1]=="5PF":
            words.insert(2, "Major Cardiovascular Procedures")
        elif words[1]=="5PU":
            words.insert(2, "Simple Cardiothoracic Procedures")
        elif words[1]=="5PG":
            words.insert(2, "Percutaneous Cardiovascular Procedures")
        elif words[1]=="5PW":
            words.insert(2, "Multiple Wound Debridement")
        elif words[1]=="5PH":
            words.insert(2, "Cardiac Electrophysiologic Procedures")
        elif words[1]=="5PM":
            words.insert(2, "Automatic Cardioverter Procedures")
        elif words[1]=="5PJ":
            words.insert(2, "Major Amputation ")
        elif words[1]=="5PS":
            words.insert(2, "Other Vascular Procedures")
        elif words[1]=="5PK":
            words.insert(2, "Permanent Pacemaker ")
        elif words[1]=="5PN":
            words.insert(2, "Pacemaker Revision and Replacement")
        elif words[1]=="5PR":
            words.insert(2, "Other Circulatory System OR Procedures")
        elif words[1]=="5PT":
            words.insert(2, "Cardiac Cath")
        elif words[1]=="5PL":
            words.insert(2, "Minor Amputation")
        elif words[1]=="5PQ":
            words.insert(2, "Vein Ligation and Stripping")
        elif words[1]=="5B":
            words.insert(2, "Infective Endocarditis")
        elif words[1]=="5C":
            words.insert(2, "Heart Failure and Shock")
        elif words[1]=="5D":
            words.insert(2, "Venous Thrombosis")
        elif words[1]=="5E":
            words.insert(2, "Skin Ulcer for Circulatory Disorders")
        elif words[1]=="5F":
            words.insert(2, "Peripheral Vascular")
        elif words[1]=="5G":
            words.insert(2, "Coronary Atherosclerosis and Unstable Angina")
        elif words[1]=="5H":
            words.insert(2, "Hypertension")
        elif words[1]=="5J":
            words.insert(2, "Congenital Heart Disease")
        elif words[1]=="5K":
            words.insert(2, "Valvular Disorders")
        elif words[1]=="5L":
            words.insert(2, "Major Arrhythmia and Cardiac Arrest")
        elif words[1]=="5M":
            words.insert(2, "Non-major Arrhythmia and Conduction Disorders")
        elif words[1]=="5P":
            words.insert(2, "Chest Pain, Syncope and Collapse")
        elif words[1]=="5R":
            words.insert(2, "Other Circulatory System Diagnoses")
        elif words[1]=="6QB":
            words.insert(2, "Esophageal Resection")
        elif words[1]=="6PV":
            words.insert(2, "Stomach,Duodenum Resection")
        elif words[1]=="6PS":
            words.insert(2, "Lap Stomach, Duodenum , Diaphragm")
        elif words[1]=="6PW":
            words.insert(2, "Lap Rectal Resection")
        elif words[1]=="6PB":
            words.insert(2, "Major Small and Large Bowel")
        elif words[1]=="6PX":
            words.insert(2, "Lap Major Small and Large Bowel")
        elif words[1]=="6PA":
            words.insert(2, "Rectal Resection")
        elif words[1]=="6QC":
            words.insert(2, "Other Esophageal Procedures")
        elif words[1]=="6PT":
            words.insert(2, "Lap Peritoneal Adhesiolysis ")
        elif words[1]=="6PE":
            words.insert(2, "Other Stomach , Duodenum")
        elif words[1]=="6PY":
            words.insert(2, "Lap Abdominal Hernia Proc")
        elif words[1]=="6PC":
            words.insert(2, "Peritoneal Adhesiolysis")
        elif words[1]=="6PK":
            words.insert(2, "Other Digestive System OR Procedures")
        elif words[1]=="6PM":
            words.insert(2, "Complex TherapeuticGastroscopy")
        elif words[1]=="6PZ":
            words.insert(2, "Lap Inguinal Hernia Proc")
        elif words[1]=="6PD":
            words.insert(2, "Minor Small and Large Bowel")
        elif words[1]=="6PU":
            words.insert(2, "Lap Appendectomy")
        elif words[1]=="6PL":
            words.insert(2, "Pyloromyotomy procedures")
        elif words[1]=="6PJ":
            words.insert(2, "Appendectomy")
        elif words[1]=="6PN":
            words.insert(2, "Other Gastroscopy")
        elif words[1]=="6PP":
            words.insert(2, "Complex Therpeutic Colonoscopy")
        elif words[1]=="6PQ":
            words.insert(2, "Other Colonoscopy")
        elif words[1]=="6PR":
            words.insert(2, "Dilatation of Intestine")
        elif words[1]=="6PG" or words[1] == "6PH":
            words.insert(2, "Hernia Proc")
        elif words[1]=="6PF":
            words.insert(2, "Anal and Stomal Procedures")
        elif words[1]=="6A":
            words.insert(2, "GI Malignancy")
        elif words[1]=="6C":
            words.insert(2, "Anal and Stomal Procedures")
        elif words[1]=="6D":
            words.insert(2, "Uncomplicated Peptic Ulcer")
        elif words[1]=="6E":
            words.insert(2, "Inflammatory Bowel Diseases")
        elif words[1]=="6F":
            words.insert(2, "GI Obstruction")
        elif words[1]=="6N":
            words.insert(2, "Non-infectious Gastroenteritis")
        elif words[1]=="6G":
            words.insert(2, "Infectious Gastroenteritis")
        elif words[1]=="6H":
            words.insert(2, "Misc Digestive Disorder")
        elif words[1]=="6J":
            words.insert(2, "Other Digestive System Diagnoses")
        elif words[1]=="6K":
            words.insert(2, "Abdominal Pain or Mesenteric Adenitis")
        elif words[1]=="6L":
            words.insert(2, "Intestinal Helminthiases")
        elif words[1]=="6M":
            words.insert(2, "Esophagitis, Gastritis & Dyspepsia")
        elif words[1]=="7PL":
            words.insert(2, "Shunt Procedures")
        elif words[1]=="7PA":
            words.insert(2, "Pancreas Resection ")
        elif words[1]=="7PK":
            words.insert(2, "Liver Resection")
        elif words[1]=="7PB":
            words.insert(2, "Biliary Tract Procedures")
        elif words[1]=="7PG":
            words.insert(2, "Pancreas and Liver Procedure Except Resection")
        elif words[1]=="7PE":
            words.insert(2, "Other Hepatobiliary and Pancreas Procedures")
        elif words[1]=="7PD":
            words.insert(2, "Hepatobiliary Diagnostic Procedures")
        elif words[1]=="7PJ":
            words.insert(2, "Lap Hepatic Procedures")
        elif words[1]=="7PC":
            words.insert(2, "Cholecystectomy")
        elif words[1]=="7PF":
            words.insert(2, "Laparoscopic Cholecystectomy")
        elif words[1]=="7PH":
            words.insert(2, "ERCP with Therapeutic Procedures")
        elif words[1]=="7A":
            words.insert(2, "Cirrhosis and Alcoholic Hepatitis")
        elif words[1]=="7B":
            words.insert(2, "Malignancy of Hepatobiliary or Pancreas")
        elif words[1]=="7C":
            words.insert(2, "Disorder of Pancreas, Except Malignancy")
        elif words[1]=="7D":
            words.insert(2, "Disorder of Liver, Except Malignancy, Cirrhosis, Alcoholic Hepatitis")
        elif words[1]=="7E":
            words.insert(2, "Disorder of Biliary Trac")
        elif words[1]=="8QE":
            words.insert(2, "Plasmapheresis")
        elif words[1]=="8QF":
            words.insert(2, "Multiple (>4) Wound Debridement")
        elif words[1]=="8QD" or words[1]=="8PCX+8PDX" or words[1]=="8PCX+8PEX" or words[1]=="8PDX+8PEX":
            words.insert(2, "Bilateral or Multiple Major Joint of Lower Extremity")
        elif words[1]=="8PW":
            words.insert(2, "Hip Revision")
        elif words[1]=="8QB":
            words.insert(2, "Multiple (2-4) Wound Debridement")
        elif words[1]=="8PX + 8PY":
            words.insert(2, "Knee Revision")
        elif words[1]=="8PF":
            words.insert(2, "Amputation for Musculoskeletal & Connective Tissue Disorders")
        elif words[1]=="8PD":
            words.insert(2, "Spinal Fusion")
        elif words[1]=="8PA":
            words.insert(2, "Hip Replacement")
        elif words[1]=="8PE":
            words.insert(2, "Back & Neck Procedure Except Spinal Fusion")
        elif words[1]=="8PV":
            words.insert(2, "Partial Hip Replacement")
        elif words[1]=="8PC":
            words.insert(2, "Other Major Joint Replacement & Limb Reattach of Lower/Upper Extremities ")
        elif words[1]=="8PB":
            words.insert(2, "Knee Replacement")
        elif words[1]=="8PK":
            words.insert(2, "Knee Procedures Except Replacement")
        elif words[1]=="8PJ":
            words.insert(2, "Hip and Femur Procedures Except Replacement")
        elif words[1]=="8PH":
            words.insert(2, "Skin Graft Except Hand for MS&CT")
        elif words[1]=="8PG":
            words.insert(2, "Biopsies of Musculoskeletal & Connective Tissue Disorders")
        elif words[1]=="8PT":
            words.insert(2, "Arthroscopy")
        elif words[1]=="8PU":
            words.insert(2, "Other Musculoskeletal System and Connective Tissue OR Procedures")
        elif words[1]=="8PM":
            words.insert(2, "Humerus, Tibia, Fibula & Ankle Procedures Except Replacement")
        elif words[1]=="8QA":
            words.insert(2, "Wound Debridement for MS&CT")
        elif words[1]=="8PL":
            words.insert(2, "Shoulder, Elbow & Forearm Procedures Except Replacement")
        elif words[1]=="8PS":
            words.insert(2, "Soft Tissue Procedures")
        elif words[1]=="8PQ":
            words.insert(2, "Local Excision & Removal of Internal Fixation Devices of Hip & Femur")
        elif words[1]=="8PP" or words[1]=="8PR":
            words.insert(2, "Foot Procedures and Local Excision & Removal of Internal Fixation Devices Exc Hip & Femur")
        elif words[1]=="8PN":
            words.insert(2, "Wrist & Hand Procedures Except Replacement")
        elif words[1]=="8A":
            words.insert(2, "Fracture of Femur")
        elif words[1]=="8B":
            words.insert(2, "Fracture of Hip and Pelvis")
        elif words[1]=="8C":
            words.insert(2, "Sprain, Strain and Dislocation of Hip, Pelvis and Thigh")
        elif words[1]=="8D":
            words.insert(2, "Osteomyelitis")
        elif words[1]=="8E":
            words.insert(2, "Pathological Fracture and Malignancy")
        elif words[1]=="8F":
            words.insert(2, "Connective Tissue")
        elif words[1]=="8G":
            words.insert(2, "Septic Arthritis")
        elif words[1]=="8H":
            words.insert(2, "Medical Back Problems")
        elif words[1]=="8J":
            words.insert(2, "Bone Disease and Arthropathies")
        elif words[1]=="8L":
            words.insert(2, "Signs and Symptoms")
        elif words[1]=="8M":
            words.insert(2, "Tendonitis, Myositis and Bursitis")
        elif words[1]=="8N":
            words.insert(2, "Aftercare")
        elif words[1]=="8P":
            words.insert(2, "Fracture, Sprain, Strain and Dislocation of Forearm, Hand and Foot")
        elif words[1]=="8Q":
            words.insert(2, "Fracture, Sprain, Strain and Dislocation of Upper Arm and Lower Leg")
        elif words[1]=="8R":
            words.insert(2, "Other Musculoskeletal System and Connective Tissue Diagnoses")
        elif words[1]=="8S":
            words.insert(2, "Major Connective Tissue Dx")
        elif words[1]=="9PJ":
            words.insert(2, "Pedicle Graft Plastic Procedures")
        elif words[1]=="9PD":
            words.insert(2, "Skin Graft and Debridement")
        elif words[1]=="9PA":
            words.insert(2, "Total Mastectomy")
        elif words[1]=="9PF":
            words.insert(2, "Skin, Subcut Tiss and Breast Plastic Proc")
        elif words[1]=="9PB" and words[1]=="9PC":
            words.insert(2, "Subtotal Mastextomy, Biopsy and Local Excision of Breast")
        elif words[1]=="9PG" and words[1]=="9PH":
            words.insert(2, "Other Skin, Subcutaneous Tissue and Breast Procedures")
        elif words[1]=="9PE":
            words.insert(2, "Perianal and Pilonidal")
        elif words[1]=="9A":
            words.insert(2, "Skin Ulcer")
        elif words[1]=="9B":
            words.insert(2, "Severe Skin Disorders")
        elif words[1]=="9C":
            words.insert(2, "Moderate Skin Disorders")
        elif words[1]=="9D":
            words.insert(2, "Minor Skin Disorders")
        elif words[1]=="9E":
            words.insert(2, "Malignant Breast Disorders")
        elif words[1]=="9F":
            words.insert(2, "Non-Malignant Breast Disorders")
        elif words[1]=="9G":
            words.insert(2, "Cellulites")
        elif words[1]=="9H":
            words.insert(2, "Trauma")
        elif words[1]=="9J":
            words.insert(2, "Skin Malignanc")
        elif words[1]=="10PB":
            words.insert(2, "Pituitary")
        elif words[1]=="10PC":
            words.insert(2, "Amputation of Lower Limb")
        elif words[1]=="10PK":
            words.insert(2, "Lap Proc for Obesity")
        elif words[1]=="10PE":
            words.insert(2, "Procedure for Obesity")
        elif words[1]=="10PA":
            words.insert(2, "Adrenal")
        elif words[1]=="10PF":
            words.insert(2, "Parathyroid")
        elif words[1]=="10PG":
            words.insert(2, "Thyroid")
        elif words[1]=="10PJ":
            words.insert(2, "Other Endocrine, Nutritional & Metabolic OR Procedures")
        elif words[1]=="10PH":
            words.insert(2, "Thyroglossal")
        elif words[1]=="10A" or words[1]=="10E":
            words.insert(2, "Endocrine Disorders Except Diabetes without Complicated PDx")
        elif words[1]=="10B":
            words.insert(2, "Severe Metabolic Disorders")
        elif words[1]=="10C":
            words.insert(2, "Nutritional and Misc. Metabolic Disorders")
        elif words[1]=="10D":
            words.insert(2, "Inborn Errors of Metabolism")
        elif words[1]=="10F":
            words.insert(2, "Diabetes without Complicated PDx")
        elif words[1]=="10G":
            words.insert(2, "EndocrineMalignancy")
        elif words[1]=="11PA":
            words.insert(2, "Kidney Transplant")
        elif words[1]=="11PL":
            words.insert(2, "Plasmapheresis")
        elif words[1]=="11PC":
            words.insert(2, "Kidney, Ureter and Major Bladder Procedures")
        elif words[1]=="11PM":
            words.insert(2, "Lap Adhesiolysis & Renal Tiss Ablation")
        elif words[1]=="11PB":
            words.insert(2, "Operative Insertion of Peritoneal Catheter for Dialysis")
        elif words[1]=="11PD":
            words.insert(2, "Transurethral Prostatectomy")
        elif words[1]=="11PH":
            words.insert(2, "Other Kidney and Urinary Tract OR Procedures")
        elif words[1]=="11PF":
            words.insert(2, "Transurethral Procedures, Except Prostatectomy")
        elif words[1]=="11PJ":
            words.insert(2, "Ureteroscopy")
        elif words[1]=="11PK":
            words.insert(2, "Cystourethroscopy")
        elif words[1]=="11PG":
            words.insert(2, "Urethral Procedures")
        elif words[1]=="11PE":
            words.insert(2, "Minor Bladder Procedures")
        elif words[1]=="11A":
            words.insert(2, "Chronic Renal Failure")
        elif words[1]=="11J":
            words.insert(2, "Acute Renal Failure")
        elif words[1]=="11B":
            words.insert(2, "Admit for Renal Dialysis")
        elif words[1]=="11C":
            words.insert(2, "Kidney and Urinary Tract Neoplasm")
        elif words[1]=="11D":
            words.insert(2, "Kidney and Urinary Tract Infection")
        elif words[1]=="11E":
            words.insert(2, "Urinary Stone")
        elif words[1]=="11F":
            words.insert(2, "Kidney & Urinary Tract Signs & Symptoms")
        elif words[1]=="11G":
            words.insert(2, "Urethral Stricture")
        elif words[1]=="11H":
            words.insert(2, "Other Kidney and Urinary Tract Diagnoses")
        elif words[1]=="11K":
            words.insert(2, "Major Kidney Dx")

        elif words[1]=="12PA":
            words.insert(2, "Major Male Pelvic Procedures")
        elif words[1]=="12PB":
            words.insert(2, "Transurethral Prostatectomy")
        elif words[1]=="12PF":
            words.insert(2, "Other Male Reproductive System OR Procedures")
        elif words[1]=="12PD":
            words.insert(2, "Penis Procedures")
        elif words[1]=="12PC":
            words.insert(2, "Testis Procedures")
        elif words[1]=="12PG":
            words.insert(2, "Cystourethroscopy")
        elif words[1]=="12PE":
            words.insert(2, "Circumcision")
        elif words[1]=="12A":
            words.insert(2, "Malignancy, Male Reproductive System")
        elif words[1]=="12B":
            words.insert(2, "Benign Prostatic Hypertrophy")
        elif words[1]=="12C":
            words.insert(2, "Inflammation of Male Reproductive System")
        elif words[1]=="12E":
            words.insert(2, "Other Male Reproductive System Diagnoses")
        elif words[1]=="13PJ":
            words.insert(2, "Pelvic Evisceration")
        elif words[1]=="13PL":
            words.insert(2, "Lap Radical Hysterectomy")
        elif words[1]=="13PA":
            words.insert(2, "Rad Hysterectomy and Rad Vulvectomy")
        elif words[1]=="13PK":
            words.insert(2, "Lap Uterine and Adnexal")
        elif words[1]=="13PB":
            words.insert(2, "Uterine and Adnexal")
        elif words[1]=="13PM":
            words.insert(2, "Lap adhesiolysis")
        elif words[1]=="13PH":
            words.insert(2, "Other Female Reproductive System OR Procedures")
        elif words[1]=="13PC":
            words.insert(2, "Female Reproductive System Reconstructive Procedures")
        elif words[1]=="13PF":
            words.insert(2, "Endoscopic Tubal Interruption")
        elif words[1]=="13PE":
            words.insert(2, "Incisional Tubal Interruption")
        elif words[1]=="13PD":
            words.insert(2, "Vagina, Cervix and Vulva Procedures")
        elif words[1]=="13PG":
            words.insert(2, "D&C")
        elif words[1]=="13B":
            words.insert(2, "Non Ovarian/Adnexal CA in Situ")
        elif words[1]=="13C":
            words.insert(2, "Ovarian/Adnexal Malignancy")
        elif words[1]=="13D":
            words.insert(2, "Lower Genitourinary Tract Infection")
        elif words[1]=="13E":
            words.insert(2, "Female Pelvic Infection")
        elif words[1]=="13F":
            words.insert(2, "Menstrual and Other Female Reproductive System Disorders")
        elif words[1]=="14A":
            words.insert(2, "Labour and Delivery")
        elif words[1]=="14B":
            words.insert(2, "Pregnancy ")
        elif words[1]=="14C":
            words.insert(2, "PP/Post Abort/Deli ")
        elif words[1]=="14D":
            words.insert(2, "PP/Post Abortion ")
        elif words[1]=="14E":
            words.insert(2, "Antenatal")
        elif words[1]=="14F":
            words.insert(2, "Ectopic Pregnancy")
        elif words[1]=="14G":
            words.insert(2, "Threatened Abortion")
        elif words[1]=="14H" or words[1]=="14K" or words[1]=="14L":
            words.insert(2, "Abortion")
        elif words[1]=="14J":
            words.insert(2, "False Labor")
        elif words[1]=="16A":
            words.insert(2, "Red Blood Cell Disorders")
        elif words[1]=="16B":
            words.insert(2, "Coagulation Disorders")
        elif words[1]=="16C":
            words.insert(2, "Reticuloendothelial and Immunity Disorders")
        elif words[1]=="17PA":
            words.insert(2, "Major OR Proc")
        elif words[1]=="17A":
            words.insert(2, "Acute Leukemia")
        elif words[1]=="17B":
            words.insert(2, "Lymphoma &Non-acute Leukemia")
        elif words[1]=="17C":
            words.insert(2, "Other Neoplastic Disorders")
        elif words[1]=="18A":
            words.insert(2, "Septicemia")
        elif words[1]=="18B":
            words.insert(2, "Postop & Posttraumatic Infections")
        elif words[1]=="18C":
            words.insert(2, "Malaria")
        elif words[1]=="18D":
            words.insert(2, "Dengue")
        elif words[1]=="18E":
            words.insert(2, "Fever of Unknown Origin")
        elif words[1]=="18F":
            words.insert(2, "Viral Illness Except Dengue")
        elif words[1]=="18G":
            words.insert(2, "Fungal Diseases")
        elif words[1]=="18H":
            words.insert(2, "Other Infectious & Parasitic Diseases")
        elif words[1]=="18J":
            words.insert(2, "Melioidosis")
        elif words[1]=="18K":
            words.insert(2, "Leptospirosis")
        elif words[1]=="19A":
            words.insert(2, "Acute Psychotic Disorders")
        elif words[1]=="19B":
            words.insert(2, "Chronic Psychotic Disorders")
        elif words[1]=="19C":
            words.insert(2, "Major Affective Disorders")
        elif words[1]=="19D":
            words.insert(2, "Other Affect and Somatoform Disorders")
        elif words[1]=="19E":
            words.insert(2, "Acute Reaction and Psychosocial Dysfunction")
        elif words[1]=="19F":
            words.insert(2, "Anxiety Disorders")
        elif words[1]=="19G":
            words.insert(2, "Eating and Obsessive Compulsive Disorders ")
        elif words[1]=="19H":
            words.insert(2, "Personality,Impulse Control Disorders, and Sexual Dysfunction")
        elif words[1]=="19J":
            words.insert(2, "Childhood Mental Disorders")
        elif words[1]=="19K":
            words.insert(2, "Organic Disturbance ")
        elif words[1]=="19L":
            words.insert(2, "Other Mental Disorders")
        elif words[1]=="19N":
            words.insert(2, "Mental Retardation ")
        elif words[1]=="20A":
            words.insert(2, "Alcohol Intoxication and Withdrawal")
        elif words[1]=="20B":
            words.insert(2, "Drug Use Disorders and Withdrawal")
        elif words[1]=="20C":
            words.insert(2, "Alcohol Use Disorders and Dependence")
        elif words[1]=="120D":
            words.insert(2, "Opioid Use Disorders and Dependence")
        elif words[1]=="20E" or words[1]=="20F":
            words.insert(2, "Other Drug Use Disorders and Dependence and Intoxication")
        elif words[1]=="21PF":
            words.insert(2, "Multiple Wound Debridement")
        elif words[1]=="21PB":
            words.insert(2, "Skin Graft")
        elif words[1]=="21PD" or words[1]=="21PE":
            words.insert(2, "Other OR Procedures for Injuries")
        elif words[1]=="21PC":
            words.insert(2, "Hand Procedures")
        elif words[1]=="21PA":
            words.insert(2, "Wound Debridement")
        elif words[1]=="21A":
            words.insert(2, "Traumatic Injury")
        elif words[1]=="21B":
            words.insert(2, "Allergic Reaction")
        elif words[1]=="21C":
            words.insert(2, "Drugs")
        elif words[1]=="21D":
            words.insert(2, "Complications of Treatment")
        elif words[1]=="21E":
            words.insert(2, "Other Injury, Poisoning and Toxic Effects Diagnoses")
        elif words[1]=="22A":
            words.insert(2, "PDx/SDx Extensive Burn")
        elif words[1]=="22B":
            words.insert(2, "PDx/SDx Full Thickness Burn")
        elif words[1]=="22C":
            words.insert(2, "PDx/SDx Full Thickness Burn No Debridement")
        elif words[1]=="23A":
            words.insert(2, "Rehabilitation")
        elif words[1]=="23B":
            words.insert(2, "Signs, Symptoms and Other Abnormal Findings")
        elif words[1]=="23C":
            words.insert(2, "Aftercare")
        elif words[1]=="23D":
            words.insert(2, "Other Factors Influencing Health Status")
        elif words[1]=="1":
            words.insert(2, "Significant Head Trauma")
        elif words[1]=="2":
            words.insert(2, "Significant Chest Trauma")
        elif words[1]=="3":
            words.insert(2, "Significant Abdominal Trauma")
        elif words[1]=="4":
            words.insert(2, "Significant Kidney Trauma")
        elif words[1]=="5":
            words.insert(2, "Significant Trauma of the Urinary System")
        elif words[1]=="6":
            words.insert(2, "Significant Trauma of the Pelvis or Spine")
        elif words[1]=="7":
            words.insert(2, "Significant Trauma of the Upper Limb")
        elif words[1]=="8":
            words.insert(2, "Significant Trauma of the Lower Limb")
        elif words[1]=="0":
            words.insert(2, "Not Significant Trauma")
        else:
            words.insert(1, "-")
            words.insert(2, "-")
