def optimize_keywords(business_name, error_keywords):
    corrected_keywords = []

    for keyword in error_keywords:
        corrected_keyword = keyword.replace('&amp;', 'and').replace('&#x27;', '')
        corrected_keywords.append(corrected_keyword)

    solution = f"{business_name}: {' '.join(corrected_keywords)}"

    return solution

def correct_errors(errors):
    corrected_errors = []

    for error in errors:
        corrected_error = error.replace('&amp;', 'and').replace('&#x27;', '')
        corrected_errors.append(corrected_error)

    return corrected_errors

def combine_documents(document_names, document_errors, document_keywords):
    combined_content = ""

    for i in range(len(document_names)):
        business = document_names[i]
        
        if i < len(document_errors):
            errors = document_errors[i]
        else:
            errors = [] 

        keywords = document_keywords[i]

       
        corrected_errors = correct_errors(errors)

        optimized_solution = optimize_keywords(business, corrected_errors + keywords)
        combined_content += optimized_solution + "\n"

    return combined_content


# Provided information for the first set of documents
document_names_set1 = ["Panchgani Tent House", "River Orchid Resort", "Royal Inn Stay", "Hotel Shelar Dhaba", "Global Rashid"]
document_errors_set1 = [
    ["Tent-House", "Panchgani", "Khinger Ring Road", "Resort in Panchgani", "Conference Hall", "Swimming Pool", "Garden", "AC &amp; Non AC Rooms"],
    ["Tapola Resorts", "Hotels in Tapola", "Tapola Hill Station Resort", "Tapola Accommodation", "Tapola Riverside Stay", "Tapola Garden View Rooms"]
]

document_keywords_set1 = [
    ["Khinger Ring Road", "Resort", "Hotel", "Marriages", "Function"],
    ["Hotels", "Best Resort in Tapola", "Lake View Stay", "Agro Tourism"],
    ["night stay in panchwad", "yavteshwar resort", "veg hotel near me", "AC rooms"],
    ["party hall", "celebration place", "events and gatherings hall", "family restaurant"],
    ["trader", "bitcoin", "Crypto", "currency", "blockchain", "trading", "learn crupto", "influencer"]
]

# Provided information for the second set of documents
document_names_set2 = ["Rticlubindia", "Mahitiadhikar", "Vidhiresorttapola", "Tanishkatours", "Alfaautomation"]
document_errors_set2 = [
    ["RTI Club India", "RTI india"],
    ["mahitiadhikar", "maharashta government"],
    ["vidhi resort in tapola", "ac rooms", "rooms", "hotel"],
    ["Car Retal For outstaion", "ranted car"],
    ["in satara", "alfa auto", "alfa automation"]
    ]

document_keywords_set2 = [
    ["vijay dighe", "rti act 2005", "RTI", "Right to information", "mahiticha adhikar", "vijay dighe", "mahiti president aadhikar", "Dr vijay Dighe"],
    ["rti act", "tax refund", "information", "club members", "organization", "mahitiadhikar"],
    ["vidhi resort in tapola", "ac rooms", "rooms", "hotel"],
    ["Car Rental In Mahabaleshwar", "taxi service", "Local Sightseeing", "Bike rental", "Self drive", "Tour Packages"],
    ["Automatic gate", "swing gate", "sliding gate", "garage shutter", "boom barrier", "folding gate"]
]

# Combine both sets of documents
combined_document_names = document_names_set1 + document_names_set2
combined_document_errors = document_errors_set1 + document_errors_set2
combined_document_keywords = document_keywords_set1 + document_keywords_set2

combined_content = combine_documents(combined_document_names, combined_document_errors, combined_document_keywords)
print(combined_content)

