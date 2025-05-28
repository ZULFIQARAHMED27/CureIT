import streamlit as st

# Updated code to handle multiple ailments

# Further expanded ailment database with additional common ailments
ailment_database = {
    "cough": {
        "symptoms": ["cough"],
        "natural_remedy": "Drink warm water with honey and ginger. Stay hydrated and avoid cold beverages.",
        "medicinal_suggestion": "Cough syrup containing Dextromethorphan or Guaifenesin may help. Check dosage instructions."
    },
    "cold": {
        "symptoms": ["cold", "runny nose", "congestion"],
        "natural_remedy": "Drink warm fluids like ginger tea, and eat foods rich in Vitamin C like oranges.",
        "medicinal_suggestion": "Consider taking Cetrizine for relief from runny nose and sneezing. Consult dosage guidelines."
    },
    "fever": {
        "symptoms": ["fever", "high temperature"],
        "natural_remedy": "Stay hydrated, rest, and place a cool, damp cloth on the forehead.",
        "medicinal_suggestion": "Paracetamol or Ibuprofen can reduce fever. Follow dosage instructions or consult a physician."
    },
    "headache": {
        "symptoms": ["headache", "migraine"],
        "natural_remedy": "Rest in a dark room, stay hydrated, and try massaging temples with peppermint oil.",
        "medicinal_suggestion": "Over-the-counter pain relievers like Ibuprofen or Acetaminophen may help. Use as directed."
    },
    "stomach ache": {
        "symptoms": ["stomach ache", "abdominal pain", "stomach pain"],
        "natural_remedy": "Ginger tea or peppermint tea can soothe the stomach. Avoid heavy meals and stick to bland foods.",
        "medicinal_suggestion": "Antacids or medications like Omeprazole may help with stomach pain related to acid. Consult a pharmacist."
    },
    "sore throat": {
        "symptoms": ["sore throat", "throat pain", "scratchy throat"],
        "natural_remedy": "Gargle with warm salt water, and drink ginger or chamomile tea for relief.",
        "medicinal_suggestion": "Throat lozenges or anti-inflammatory medication like Ibuprofen can provide relief."
    },
    "allergy": {
        "symptoms": ["allergy", "sneezing", "itchy eyes", "rash"],
        "natural_remedy": "Try drinking nettle tea or using a saline nasal rinse for nasal relief.",
        "medicinal_suggestion": "Antihistamines like Loratadine or Cetrizine can help relieve allergy symptoms. Check with a pharmacist for dosage."
    },
    "indigestion": {
        "symptoms": ["indigestion", "bloating", "acid", "heartburn"],
        "natural_remedy": "Drink a glass of warm water with a few drops of lemon juice. Avoid spicy and oily foods.",
        "medicinal_suggestion": "Antacids or medications like Ranitidine can provide quick relief from acid reflux or indigestion."
    },
    "back pain": {
        "symptoms": ["back pain", "lower back", "stiffness"],
        "natural_remedy": "Try gentle stretching and apply a warm compress. Rest and avoid lifting heavy objects.",
        "medicinal_suggestion": "Pain relievers like Ibuprofen or muscle relaxants can help manage pain. Consult with a pharmacist for proper usage."
    },
    "fatigue": {
        "symptoms": ["fatigue", "tired", "exhausted", "low energy"],
        "natural_remedy": "Make sure to get adequate sleep, and eat iron-rich foods like spinach and beans.",
        "medicinal_suggestion": "A multivitamin or B-complex supplement can help if the fatigue is due to nutritional deficiencies."
    },
    "nausea": {
        "symptoms": ["nausea", "queasy", "upset stomach"],
        "natural_remedy": "Sip ginger tea or chamomile tea. Avoid strong smells and eat light meals.",
        "medicinal_suggestion": "Over-the-counter anti-nausea medication like Pepto-Bismol may help. Check with a pharmacist."
    },
    "insomnia": {
        "symptoms": ["insomnia", "can't sleep", "restlessness"],
        "natural_remedy": "Try warm milk before bed, a calming bedtime routine, and avoid screens at night.",
        "medicinal_suggestion": "Melatonin supplements may help improve sleep. Check with a healthcare provider for appropriate dosage."
    },
    "constipation": {
        "symptoms": ["constipation", "difficulty passing stools"],
        "natural_remedy": "Increase fiber intake with fruits and vegetables, and drink plenty of water.",
        "medicinal_suggestion": "A gentle laxative like Senna may help if natural remedies don't work. Consult a pharmacist."
    },
    "diarrhea": {
        "symptoms": ["diarrhea", "loose stools", "stomach cramps"],
        "natural_remedy": "Stay hydrated, drink ORS, and avoid dairy and high-fiber foods.",
        "medicinal_suggestion": "Loperamide can help with diarrhea but consult a healthcare provider before use."
    },
    "earache": {
        "symptoms": ["earache", "ear pain"],
        "natural_remedy": "Apply a warm compress to the ear and avoid loud sounds.",
        "medicinal_suggestion": "Over-the-counter pain relievers like Acetaminophen can provide relief."
    },
    "eye strain": {
        "symptoms": ["eye strain", "tired eyes", "dry eyes"],
        "natural_remedy": "Follow the 20-20-20 rule (look at something 20 feet away for 20 seconds every 20 minutes).",
        "medicinal_suggestion": "Lubricating eye drops can help alleviate dryness from eye strain."
    },
    "muscle cramps": {
        "symptoms": ["muscle cramps", "tight muscles", "leg cramps"],
        "natural_remedy": "Gently stretch the affected muscle, drink water, and eat foods rich in potassium.",
        "medicinal_suggestion": "Magnesium supplements can help prevent cramps. Check with a healthcare provider for the right dosage."
    },
    "dizziness": {
        "symptoms": ["dizziness", "lightheaded", "dizzy", "faint"],
        "natural_remedy": "Sit down and rest, and sip water to stay hydrated.",
        "medicinal_suggestion": "If persistent, see a doctor to rule out underlying causes. Vitamin B12 supplements may help if deficiency-related."
    },
    "hunger pangs": {
        "symptoms": ["hunger pangs", "stomach growling", "appetite increase"],
        "natural_remedy": "Eat fiber-rich foods to stay fuller for longer and drink plenty of water.",
        "medicinal_suggestion": "Consider small, frequent meals or healthy snacks to control hunger."
    },
    "gas": {
        "symptoms": ["gas", "flatulence", "bloating"],
        "natural_remedy": "Drink peppermint tea and avoid carbonated beverages and high-fiber foods.",
        "medicinal_suggestion": "Simethicone-based over-the-counter gas relievers can help reduce bloating and gas discomfort."
    },
    "bad breath": {
        "symptoms": ["bad breath", "halitosis", "smelly mouth"],
        "natural_remedy": "Gargle with warm salt water and stay hydrated. Chew parsley or fennel seeds for fresh breath.",
        "medicinal_suggestion": "Maintain oral hygiene with mouthwash and consider a dentist visit if persistent."
    },
    "foot pain": {
        "symptoms": ["foot pain", "heel pain", "plantar pain"],
        "natural_remedy": "Soak feet in warm water with Epsom salts and wear comfortable footwear.",
        "medicinal_suggestion": "Over-the-counter pain relief creams with menthol or capsaicin may help."
    },
    "itchy scalp": {
        "symptoms": ["itchy scalp", "dandruff", "dry scalp"],
        "natural_remedy": "Massage coconut or tea tree oil into the scalp to reduce itchiness and dryness.",
        "medicinal_suggestion": "Anti-dandruff shampoos containing zinc pyrithione can help with itchy scalp and dandruff."
    },
    "hives": {
        "symptoms": ["hives", "itchy bumps", "red rash"],
        "natural_remedy": "Apply a cold compress and avoid scratching the affected area.",
        "medicinal_suggestion": "Over-the-counter antihistamines like Benadryl may reduce itching and hives."
    },
    "nosebleed": {
        "symptoms": ["nosebleed", "bleeding nose"],
        "natural_remedy": "Sit up and pinch the nose just above the nostrils for 10 minutes. Apply a cold compress to the nose bridge.",
        "medicinal_suggestion": "If nosebleeds are frequent, consult a healthcare provider for further evaluation."
    },
    "hangover": {
        "symptoms": ["hangover", "headache", "nausea"],
        "natural_remedy": "Drink plenty of water, eat light, and consider drinking coconut water or sports drinks for electrolytes.",
        "medicinal_suggestion": "Ibuprofen may relieve headache, but avoid further alcohol intake."
    },
    "sensitivity to cold": {
        "symptoms": ["sensitivity to cold", "chills"],
        "natural_remedy": "Dress warmly and drink hot fluids to stay warm.",
        "medicinal_suggestion": "Consider checking thyroid levels if sensitivity is persistent. Multivitamins can sometimes help."
    },
    "toothache": {
        "symptoms": ["toothache", "tooth pain", "sore gums"],
        "natural_remedy": "Rinse with warm salt water and apply a cold compress to the cheek.",
        "medicinal_suggestion": "Take over-the-counter pain relievers like Ibuprofen. For persistent pain, see a dentist."
    },
    "joint pain": {
        "symptoms": ["joint pain", "aching joints", "stiff joints"],
        "natural_remedy": "Apply a warm compress and consider turmeric supplements for anti-inflammatory benefits.",
        "medicinal_suggestion": "Topical creams with menthol or capsaicin may reduce joint discomfort. Consult a healthcare provider if needed."
    },
    "menstrual cramps": {
        "symptoms": ["menstrual cramps", "period pain", "cramping"],
        "natural_remedy": "Use a heating pad on the lower abdomen and drink chamomile tea.",
        "medicinal_suggestion": "Ibuprofen or Naproxen can help relieve menstrual pain. Follow dosage instructions."
    },
    "acne": {
        "symptoms": ["acne", "pimples", "blemishes"],
        "natural_remedy": "Apply tea tree oil diluted with water to the affected areas and avoid heavy makeup.",
        "medicinal_suggestion": "Over-the-counter benzoyl peroxide or salicylic acid treatments may help reduce acne."
    },
    "dry skin": {
        "symptoms": ["dry skin", "flaky skin", "itchy skin"],
        "natural_remedy": "Apply coconut oil or aloe vera gel to soothe dry areas. Avoid hot showers.",
        "medicinal_suggestion": "Use a fragrance-free moisturizer. For persistent dryness, consult a dermatologist."
    },
    "heart palpitations": {
        "symptoms": ["heart palpitations", "racing heart", "fluttering"],
        "natural_remedy": "Practice deep breathing exercises and avoid caffeine.",
        "medicinal_suggestion": "Consult a healthcare provider if palpitations are frequent. Magnesium supplements might help."
    },
    "eczema": {
        "symptoms": ["eczema", "itchy skin", "rash"],
        "natural_remedy": "Moisturize with shea butter or coconut oil and avoid known triggers.",
        "medicinal_suggestion": "Hydrocortisone cream may relieve itching. Consult a doctor for persistent symptoms."
    },
    "sciatica": {
        "symptoms": ["sciatica", "lower back pain", "leg pain"],
        "natural_remedy": "Apply a cold compress and try gentle stretching exercises.",
        "medicinal_suggestion": "NSAIDs like Ibuprofen can relieve pain. Consult a physical therapist for long-term management."
    },
    "UTI (Urinary Tract Infection)": {
        "symptoms": ["burning urination", "frequent urination", "UTI"],
        "natural_remedy": "Drink plenty of water and unsweetened cranberry juice to help flush out bacteria.",
        "medicinal_suggestion": "Over-the-counter pain relievers can reduce discomfort. See a doctor for antibiotics if symptoms persist."
    },
    "skin rash": {
        "symptoms": ["skin rash", "redness", "itchy rash"],
        "natural_remedy": "Apply cold compresses and avoid scratching the affected area.",
        "medicinal_suggestion": "Topical hydrocortisone cream can help with itching. Seek medical attention for unexplained rashes."
    },
    "acid reflux": {
        "symptoms": ["acid reflux", "heartburn", "acidic taste"],
        "natural_remedy": "Avoid large meals and acidic foods, and drink ginger tea to soothe the stomach.",
        "medicinal_suggestion": "Antacids like Ranitidine or Omeprazole can reduce acid production. Check with a pharmacist."
    },
    "eye redness": {
        "symptoms": ["eye redness", "bloodshot eyes", "eye irritation"],
        "natural_remedy": "Use a cold compress and avoid rubbing the eyes.",
        "medicinal_suggestion": "Lubricating eye drops can soothe irritation. If persistent, consult an eye specialist."
    },
    "ringworm": {
        "symptoms": ["ringworm", "itchy ring rash"],
        "natural_remedy": "Apply tea tree oil (diluted) or coconut oil to affected areas twice daily.",
        "medicinal_suggestion": "Topical antifungal creams like Clotrimazole can treat ringworm. Consult a doctor if needed."
    },
    "motion sickness": {
        "symptoms": ["motion sickness", "nausea", "dizziness"],
        "natural_remedy": "Sip on ginger tea and try focusing on a stable object.",
        "medicinal_suggestion": "Over-the-counter antihistamines like Dimenhydrinate may relieve symptoms."
    },
    "hiccups": {
        "symptoms": ["hiccups"],
        "natural_remedy": "Hold your breath briefly or sip cold water slowly.",
        "medicinal_suggestion": "Persistent hiccups may require medical attention if lasting over 48 hours."
    },
    "bruises": {
        "symptoms": ["bruising", "discoloration", "tenderness"],
        "natural_remedy": "Apply a cold compress to reduce swelling.",
        "medicinal_suggestion": "For large or painful bruises, take over-the-counter pain relievers as needed."
    },
    "burns (minor)": {
        "symptoms": ["minor burn", "redness", "swelling"],
        "natural_remedy": "Run the affected area under cool water and apply aloe vera.",
        "medicinal_suggestion": "Over-the-counter antibiotic ointment may prevent infection. Consult a doctor for severe burns."
    },
    "yeast infection": {
        "symptoms": ["itching", "discharge", "yeast infection"],
        "natural_remedy": "Apply coconut oil to soothe itching and avoid tight clothing.",
        "medicinal_suggestion": "Topical antifungal creams can provide relief. Consult a pharmacist for recommendations."
    },
    "athlete's foot": {
        "symptoms": ["itchy feet", "redness on foot", "blisters"],
        "natural_remedy": "Soak feet in saltwater and apply tea tree oil.",
        "medicinal_suggestion": "Antifungal creams like Terbinafine can treat athlete's foot. Consult a pharmacist if unsure."
    },
    "heat rash": {
        "symptoms": ["heat rash", "red rash", "itchy rash"],
        "natural_remedy": "Apply a cold compress and wear loose clothing.",
        "medicinal_suggestion": "Over-the-counter hydrocortisone cream can soothe itching. Seek medical advice if persistent."
    },
    "chapped lips": {
        "symptoms": ["chapped lips", "dry lips", "cracked lips"],
        "natural_remedy": "Apply honey or aloe vera to moisturize lips.",
        "medicinal_suggestion": "Use a lip balm with SPF to protect against sun damage and dryness."
    },
    "gastric ulcers": {
        "symptoms": ["stomach pain", "burning sensation", "nausea"],
        "natural_remedy": "Drink cabbage juice or eat bananas to protect the stomach lining.",
        "medicinal_suggestion": "Medications like Omeprazole may help. Consult a doctor for proper treatment."
    },
    "dry eyes": {
        "symptoms": ["dry eyes", "gritty eyes", "eye discomfort"],
        "natural_remedy": "Blink frequently and use warm compresses to stimulate tears.",
        "medicinal_suggestion": "Artificial tear drops can relieve dryness. Seek medical advice if persistent."
    },
    "nose congestion": {
        "symptoms": ["nose congestion", "stuffy nose", "sinus congestion", "sinus"],
        "natural_remedy": "Inhale steam with eucalyptus oil, or use a humidifier.",
        "medicinal_suggestion": "Decongestant nasal sprays or tablets can relieve congestion but avoid long-term use."
    }
}


def get_remedies(user_input):
    remedies = []
    for ailment, details in ailment_database.items():
        if any(symptom in user_input.lower() for symptom in details["symptoms"]):
            remedies.append({
                "ailment": ailment.capitalize(),
                "natural_remedy": details["natural_remedy"],
                "medicinal_suggestion": details["medicinal_suggestion"]
            })
    return remedies

# Streamlit UI
st.title("CureIT")
st.subheader("Identify ailments and get remedies")

# User input for symptoms
user_symptoms = st.text_input("Enter your symptoms separated by commas (e.g., 'cough, fever'):")

if user_symptoms:
    user_symptoms_list = [symptom.strip().lower() for symptom in user_symptoms.split(",")]
    matched_ailments = []

    # Matching symptoms to ailments
    for ailment, details in ailment_database.items():
        if any(symptom in user_symptoms_list for symptom in details["symptoms"]):
            matched_ailments.append({
                "ailment": ailment,
                "natural_remedy": details["natural_remedy"],
                "medicinal_suggestion": details["medicinal_suggestion"]
            })

    if matched_ailments:
        st.subheader("Possible Ailments and Remedies")
        for ailment in matched_ailments:
            st.markdown(f"### {ailment['ailment'].capitalize()}")
            st.markdown(f"**Natural Remedy:** {ailment['natural_remedy']}")
            st.markdown(f"**Medicinal Suggestion:** {ailment['medicinal_suggestion']}")
    else:
        st.warning("No matching ailments found. Please check your symptoms or consult a healthcare professional.")
