# bmrcalc
Simple BMR calculator to help with figuring out calorie requirements of body's Basal Metabolic Rate.

Flask is the framwork used in this calculator app.

No values entered are recorded in any database.

BMR Calculation used:

            MALE: round(88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age))
                            
            FEMALE: round(447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age))
            
            round added to prettify the output.
