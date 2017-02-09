form_cont =
[
    {

        "name": "firstname",
        "label": "First Name",
        "type": "text",
        "max_length": 25,
        "required": 1
    },
    {
        "name": "lastname",
        "label": "Last Name",
        "type": "text",
        "max_length": 25,
        "required": 1
    },
    {
        "name": "smallcv",
        "label": "Small CV",
        "type": "textarea",
        "help_text": "Please insert a small CV"
    },
    {
        "name": "age",
        "label": "Age",
        "type": "integer",
        "max_value": 200,
        "min_value": 0
    },
    {
        "name": "marital_status",
        "label": "Marital Status",
        "type": "radio",
        "choices": [
            {"name": "Single", "value":"single"},
            {"name": "Married", "value":"married"},
            {"name": "Divorced", "value":"divorced"},
            {"name": "Widower", "value":"widower"}
        ]
    },
    {
        "name": "occupation",
        "label": "Occupation",
        "type": "select",
        "choices": [
            {"name": "Farmer", "value":"farmer"},
            {"name": "Engineer", "value":"engineer"},
            {"name": "Teacher", "value":"teacher"},
            {"name": "Office Clerk", "value":"office_clerk"},
            {"name": "Merchant", "value":"merchant"},
            {"name": "Unemployed", "value":"unemployed"},
            {"name": "Retired", "value":"retired"},
            {"name": "Other", "value":"other"}
        ]
    },
    {
        "name": "internet",
        "label": "Internet Access",
        "type": "checkbox"
    }
]
