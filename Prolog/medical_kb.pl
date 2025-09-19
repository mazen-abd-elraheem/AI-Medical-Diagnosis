/* Medical Knowledge Base with 143 Diagnoses */

:- dynamic symptom/2.
:- dynamic treatment/2.

% Diagnosis rule: if at least 3 symptoms match, return the disease and its treatment.
diagnose(Disease, InputSymptoms, Treatment) :-
    symptom(Disease, DiseaseSymptoms),
    intersection(DiseaseSymptoms, InputSymptoms, MatchingSymptoms),
    length(MatchingSymptoms, Count),
    Count >= 3,  % Require at least 3 matching symptoms
    treatment(Disease, Treatment).

/* Disease Facts */

/* 1. Eczema */
symptom(eczema, [itching, skin_rash, nodal_skin_eruptions, dischromic_patches, skin_peeling, scurring]).
treatment(eczema, 'Consult doctor').

/* 2. Psoriasis */
symptom(psoriasis, [red_scaly_skin, skin_rash, dischromic_patches, nodal_skin_eruptions, silver_like_dusting, small_dents_in_nails, inflammatory_nails, scurring]).
treatment(psoriasis, 'Consult doctor').

/* 3. Contact Dermatitis */
symptom(contact_dermatitis, [itching, skin_rash, blister, red_sore_around_nose, yellow_crust_ooze]).
treatment(contact_dermatitis, 'Consult doctor').

/* 4. Fungal Infections */
symptom(fungal_infections, [itching, skin_rash, nodal_skin_eruptions, dischromic_patches, skin_peeling, blisters]).
treatment(fungal_infections, 'Consult doctor').

/* 5. Common Cold */
symptom(common_cold, [continuous_sneezing, shivering, chills, watering_from_eyes, cough, runny_nose, congestion]).
treatment(common_cold, 'Consult doctor').

/* 6. Allergic Rhinitis */
symptom(allergic_rhinitis, [continuous_sneezing, watering_from_eyes, runny_nose, sinus_pressure, loss_of_smell]).
treatment(allergic_rhinitis, 'Consult doctor').

/* 7. Asthma */
symptom(asthma, [shortness_of_breath, chest_pain, cough, wheezing, fast_heart_rate]).
treatment(asthma, 'Consult doctor').

/* 8. Bronchitis */
symptom(bronchitis, [cough, chest_pain, mucoid_sputum, throat_irritation, fast_heart_rate, breathlessness]).
treatment(bronchitis, 'Consult doctor').

/* 9. Pneumonia */
symptom(pneumonia, [cough, chest_pain, high_fever, chills, rusty_sputum, breathlessness]).
treatment(pneumonia, 'Consult doctor').

/* 10. Sinusitis */
symptom(sinusitis, [sinus_pressure, runny_nose, congestion, headache, throat_irritation]).
treatment(sinusitis, 'Consult doctor').

/* 11. Gastroenteritis */
symptom(gastroenteritis, [stomach_pain, vomiting, diarrhoea, nausea, loss_of_appetite, abdominal_pain, dehydration]).
treatment(gastroenteritis, 'Consult doctor').

/* 12. Peptic Ulcers */
symptom(peptic_ulcers, [stomach_pain, nausea, vomiting, loss_of_appetite, indigestion, internal_itching]).
treatment(peptic_ulcers, 'Consult doctor').

/* 13. Hepatitis */
symptom(hepatitis, [yellowing_of_eyes, yellowish_skin, abdominal_pain, nausea, loss_of_appetite, dark_urine]).
treatment(hepatitis, 'Consult doctor').

/* 14. Irritable Bowel Syndrome (IBS) */
symptom(ibs, [abdominal_pain, constipation, diarrhoea, bloating, gas, cramps]).
treatment(ibs, 'Consult doctor').

/* 15. Gallstones */
symptom(gallstones, [abdominal_pain, nausea, vomiting, yellowing_of_eyes, indigestion]).
treatment(gallstones, 'Consult doctor').

/* 16. Migraine */
symptom(migraine, [headache, dizziness, nausea, sensitivity_to_light, visual_disturbances]).
treatment(migraine, 'Consult doctor').

/* 17. Meningitis */
symptom(meningitis, [stiff_neck, high_fever, headache, vomiting, altered_sensorium, sensitivity_to_light]).
treatment(meningitis, 'Consult doctor').

/* 18. Stroke */
symptom(stroke, [sudden_numbness_or_weakness, confusion, trouble_speaking, dizziness, loss_of_balance, weakness_of_one_body_side]).
treatment(stroke, 'Consult doctor').

/* 19. Anxiety Disorders */
symptom(anxiety_disorders, [palpitations, restlessness, sweating, irritability, dizziness, muscle_tension]).
treatment(anxiety_disorders, 'Consult doctor').

/* 20. Epilepsy */
symptom(epilepsy, [seizures, loss_of_awareness, staring_spells, temporary_confusion, altered_sensorium]).
treatment(epilepsy, 'Consult doctor').

/* 21. Arthritis */
symptom(arthritis, [joint_pain, swelling, stiffness, muscle_weakness, painful_walking, movement_stiffness]).
treatment(arthritis, 'Consult doctor').

/* 22. Osteoarthritis */
symptom(osteoarthritis, [joint_pain, stiffness, reduced_flexibility, bone_spurs, swelling]).
treatment(osteoarthritis, 'Consult doctor').

/* 23. Fibromyalgia */
symptom(fibromyalgia, [widespread_musculoskeletal_pain, fatigue, sleep_disturbances, headaches, depression]).
treatment(fibromyalgia, 'Consult doctor').

/* 24. Muscle Strain */
symptom(muscle_strain, [muscle_pain, weakness, swelling, limited_range_of_motion, muscle_spasms]).
treatment(muscle_strain, 'Consult doctor').

/* 25. Diabetes Mellitus */
symptom(diabetes_mellitus, [excessive_hunger, increased_appetite, polyuria, weight_loss, blurred_vision, fatigue, excessive_thirst, dry_mouth]).
treatment(diabetes_mellitus, 'Consult doctor').

/* 26. Hyperthyroidism */
symptom(hyperthyroidism, [weight_loss, excessive_hunger, sweating, palpitations, irritability, brittle_nails, puffy_face_and_eyes]).
treatment(hyperthyroidism, 'Consult doctor').

/* 27. Hypothyroidism */
symptom(hypothyroidism, [weight_gain, fatigue, cold_intolerance, dry_skin, puffy_face, hoarseness, muscle_weakness]).
treatment(hypothyroidism, 'Consult doctor').

/* 28. Systemic Lupus Erythematosus */
symptom(systemic_lupus_erythematosus, [fatigue, joint_pain, fever, rash, swollen_lymph_nodes, malaise]).
treatment(systemic_lupus_erythematosus, 'Consult doctor').

/* 29. Chronic Fatigue Syndrome */
symptom(chronic_fatigue_syndrome, [severe_fatigue, unrefreshing_sleep, muscle_pain, headaches, sore_throat, difficulty_concentrating]).
treatment(chronic_fatigue_syndrome, 'Consult doctor').

/* 30. Anemia */
symptom(anemia, [fatigue, weakness, pale_skin, shortness_of_breath, dizziness, irregular_heartbeats]).
treatment(anemia, 'Consult doctor').

/* 31. Hemophilia */
symptom(hemophilia, [excessive_bleeding, easy_bruising, joint_pain, swelling, blood_in_urine]).
treatment(hemophilia, 'Consult doctor').

/* 32. Leukemia */
symptom(leukemia, [fever, fatigue, frequent_infections, weight_loss, swollen_lymph_nodes, easy_bleeding]).
treatment(leukemia, 'Consult doctor').

/* 33. Lymphoma */
symptom(lymphoma, [swollen_lymph_nodes, fatigue, night_sweats, weight_loss, itching, fever]).
treatment(lymphoma, 'Consult doctor').

/* 34. Heart Disease */
symptom(heart_disease, [chest_pain, shortness_of_breath, palpitations, fatigue, dizziness, swollen_extremities]).
treatment(heart_disease, 'Consult doctor').

/* 35. Hypertension */
symptom(hypertension, [often_asymptomatic, headaches, shortness_of_breath, nosebleeds, dizziness]).
treatment(hypertension, 'Consult doctor').

/* 36. Myocardial Infarction */
symptom(myocardial_infarction, [chest_pain, shortness_of_breath, sweating, nausea, lightheadedness, pain_in_arms_or_back]).
treatment(myocardial_infarction, 'Consult doctor').

/* 37. Tuberculosis */
symptom(tuberculosis, [chronic_cough, blood_in_sputum, chest_pain, fatigue, weight_loss, fever, night_sweats, loss_of_appetite]).
treatment(tuberculosis, 'Consult doctor').

/* 38. Influenza (Flu) */
symptom(influenza, [high_fever, chills, cough, sore_throat, muscle_aches, fatigue, headache, nasal_congestion, runny_nose]).
treatment(influenza, 'Consult doctor').

/* 39. COVID-19 */
symptom(covid_19, [fever, dry_cough, tiredness, loss_of_taste_or_smell, difficulty_breathing, chest_pain, headache, sore_throat, congestion, runny_nose, nausea, diarrhea]).
treatment(covid_19, 'Consult doctor').

/* 40. Rheumatoid Arthritis */
symptom(rheumatoid_arthritis, [joint_pain, swelling, stiffness, fatigue, fever, loss_of_appetite]).
treatment(rheumatoid_arthritis, 'Consult doctor').

/* 41. Chronic Obstructive Pulmonary Disease (COPD) */
symptom(copd, [shortness_of_breath, wheezing, chest_tightness, chronic_cough, frequent_respiratory_infections, fatigue, blueness_of_lips_or_fingernail_beds]).
treatment(copd, 'Consult doctor').

/* 42. Celiac Disease */
symptom(celiac_disease, [diarrhea, weight_loss, bloating, gas, abdominal_pain, fatigue, anemia, itchy_rash]).
treatment(celiac_disease, 'Consult doctor').

/* 43. Multiple Sclerosis */
symptom(multiple_sclerosis, [numbness_or_weakness_in_limbs, partial_or_complete_loss_of_vision, double_vision, tingling_or_pain, electric_shock_sensations, tremor, lack_of_coordination, unsteady_gait, fatigue]).
treatment(multiple_sclerosis, 'Consult doctor').

/* 44. Parkinson's Disease */
symptom(parkinsons_disease, [tremor, slowed_movement, rigid_muscles, impaired_posture_and_balance, loss_of_automatic_movements, speech_changes, writing_changes]).
treatment(parkinsons_disease, 'Consult doctor').

/* 45. Systemic Scleroderma */
symptom(systemic_scleroderma, [hardened_or_tightened_patches_of_skin, swollen_fingers_and_hands, raynauds_phenomenon, acid_reflux, difficulty_swallowing, joint_pain, shortness_of_breath]).
treatment(systemic_scleroderma, 'Consult doctor').

/* 46. Addison's Disease */
symptom(addisons_disease, [extreme_fatigue, weight_loss, decreased_appetite, darkening_of_skin, low_blood_pressure, salt_craving, low_blood_sugar, nausea, diarrhea, vomiting, abdominal_pain, muscle_or_joint_pains]).
treatment(addisons_disease, 'Consult doctor').

/* 47. Cushing's Syndrome */
symptom(cushings_syndrome, [weight_gain, pink_or_purple_stretch_marks, thinning_skin, easy_bruising, acne, fatigue, muscle_weakness, high_blood_pressure, bone_loss, diabetes]).
treatment(cushings_syndrome, 'Consult doctor').

/* 48. Pancreatitis */
symptom(pancreatitis, [upper_abdominal_pain, abdominal_pain_that_radiates_to_the_back, tenderness_when_touching_the_abdomen, fever, rapid_pulse, nausea, vomiting]).
treatment(pancreatitis, 'Consult doctor').

/* 49. Gout */
symptom(gout, [intense_joint_pain, lingering_discomfort, inflammation_and_redness, limited_range_of_motion]).
treatment(gout, 'Consult doctor').

/* 50. Hypoglycemia */
symptom(hypoglycemia, [shakiness, dizziness, sweating, hunger, irritability_or_moodiness, anxiety_or_nervousness, headache]).
treatment(hypoglycemia, 'Consult doctor').

/* 51. Hyperglycemia */
symptom(hyperglycemia, [frequent_urination, increased_thirst, blurred_vision, fatigue, headache, fruity_smelling_breath, nausea, vomiting, shortness_of_breath, dry_mouth, weakness, confusion]).
treatment(hyperglycemia, 'Consult doctor').

/* 52. Sleep Apnea */
symptom(sleep_apnea, [loud_snoring, episodes_of_breathing_cessation, abrupt_awakenings_with_gasping, morning_headache, difficulty_staying_asleep, excessive_daytime_sleepiness, irritability]).
treatment(sleep_apnea, 'Consult doctor').

/* 53. HIV/AIDS */
symptom(hiv_aids, [fever, chills, rash, night_sweats, muscle_aches, sore_throat, fatigue, swollen_lymph_nodes, mouth_ulcers]).
treatment(hiv_aids, 'Consult doctor').

/* 54. Lyme Disease */
symptom(lyme_disease, [fever, headache, fatigue, skin_rash, joint_pain, heart_palpitations, dizziness, inflammation_of_brain_and_spinal_cord]).
treatment(lyme_disease, 'Consult doctor').

/* 55. Zika Virus */
symptom(zika_virus, [fever, rash, headache, joint_pain, conjunctivitis, muscle_pain]).
treatment(zika_virus, 'Consult doctor').

/* 56. Dengue Fever */
symptom(dengue_fever, [high_fever, severe_headache, pain_behind_the_eyes, severe_joint_and_muscle_pain, fatigue, nausea, vomiting, skin_rash]).
treatment(dengue_fever, 'Consult doctor').

/* 57. Chikungunya */
symptom(chikungunya, [fever, joint_pain, muscle_pain, headache, nausea, fatigue, rash]).
treatment(chikungunya, 'Consult doctor').

/* 58. Malaria */
symptom(malaria, [fever, chills, headache, nausea, vomiting, muscle_pain, fatigue, sweating]).
treatment(malaria, 'Consult doctor').

/* 59. Typhoid Fever */
symptom(typhoid_fever, [high_fever, headache, stomach_pain, constipation_or_diarrhea, rose_colored_spots]).
treatment(typhoid_fever, 'Consult doctor').

/* 60. Mumps */
symptom(mumps, [swollen_salivary_glands, fever, headache, muscle_aches, tiredness, loss_of_appetite]).
treatment(mumps, 'Consult doctor').

/* 61. Rubella (German Measles) */
symptom(rubella, [mild_fever, headache, stuffy_or_runny_nose, inflamed_red_eyes, enlarged_tender_lymph_nodes, fine_pink_rash, aching_joints]).
treatment(rubella, 'Consult doctor').

/* 62. Measles */
symptom(measles, [high_fever, dry_cough, runny_nose, sore_throat, inflamed_eyes, tiny_white_spots_inside_mouth, skin_rash]).
treatment(measles, 'Consult doctor').

/* 63. Chickenpox */
symptom(chickenpox, [fever, loss_of_appetite, headache, tiredness_and_malaise, skin_rash_with_itchy_fluid_filled_blisters]).
treatment(chickenpox, 'Consult doctor').

/* 64. Acute Sinusitis */
symptom(acute_sinusitis, [nasal_congestion, thick_yellow_or_green_discharge, facial_pain_and_pressure, headache, fever, cough, fatigue, toothache]).
treatment(acute_sinusitis, 'Consult doctor').

/* 65. Chronic Sinusitis */
symptom(chronic_sinusitis, [nasal_congestion, facial_pain_and_pressure, nasal_obstruction, thick_discolored_discharge, reduced_sense_of_smell, reduced_sense_of_taste, headache, toothache, fatigue]).
treatment(chronic_sinusitis, 'Consult doctor').

/* 66. Conjunctivitis (Pink Eye) */
symptom(conjunctivitis, [redness_in_one_or_both_eyes, itching, gritty_feeling, discharge_that_forms_a_crust, tearing]).
treatment(conjunctivitis, 'Consult doctor').

/* 67. Otitis Media (Middle Ear Infection) */
symptom(otitis_media, [ear_pain, fever, fluid_drainage_from_the_ear, hearing_loss, irritability_in_children, difficulty_sleeping]).
treatment(otitis_media, 'Consult doctor').

/* 68. Vertigo */
symptom(vertigo, [spinning_sensation, dizziness, balance_problems, nausea, vomiting, headache, sweating]).
treatment(vertigo, 'Consult doctor').

/* 69. Hypoglycemia (Low Blood Sugar) */
symptom(hypoglycemia_low, [shakiness, dizziness, sweating, hunger, irritability_or_moodiness, anxiety_or_nervousness, headache]).
treatment(hypoglycemia_low, 'Consult doctor').

/* 70. Hyperglycemia (High Blood Sugar) */
symptom(hyperglycemia_high, [frequent_urination, increased_thirst, blurred_vision, fatigue, headache, fruity_smelling_breath, nausea, vomiting, shortness_of_breath]).
treatment(hyperglycemia_high, 'Consult doctor').

/* 71. Gastroesophageal Reflux Disease (GERD) */
symptom(gerd, [heartburn, regurgitation_of_food, difficulty_swallowing, chest_pain, chronic_cough, laryngitis, new_or_worsening_asthma]).
treatment(gerd, 'Consult doctor').

/* 72. Peptic Ulcer Disease */
symptom(peptic_ulcer_disease, [burning_stomach_pain, bloating, heartburn, nausea, intolerance_to_fatty_foods]).
treatment(peptic_ulcer_disease, 'Consult doctor').

/* 73. Urinary Tract Infection (UTI) */
symptom(uti, [strong_persistent_urge_to_urinate, burning_sensation_while_urinating, frequent_small_amounts_of_urine, cloudy_urine, strong_smelling_urine, pelvic_pain]).
treatment(uti, 'Consult doctor').

/* 74. Bacterial Vaginosis */
symptom(bacterial_vaginosis, [thin_gray_white_or_green_vaginal_discharge, foul_smelling_fishy_odor, vaginal_itching, burning_during_urination]).
treatment(bacterial_vaginosis, 'Consult doctor').

/* 75. Candida Infections (Thrush) */
symptom(candida_infections, [white_patches_on_tongue, redness_inside_mouth, difficulty_swallowing, cracking_at_corners_of_mouth]).
treatment(candida_infections, 'Consult doctor').

/* 76. Chlamydia */
symptom(chlamydia, [painful_urination, lower_abdominal_pain, vaginal_discharge, penile_discharge, painful_sexual_intercourse, bleeding_between_periods, testicular_pain]).
treatment(chlamydia, 'Consult doctor').

/* 77. Gonorrhea */
symptom(gonorrhea, [painful_urination, abnormal_discharge, pain_or_swelling_in_one_testicle, increased_vaginal_bleeding, anal_itching, soreness, bleeding, painful_bowel_movements]).
treatment(gonorrhea, 'Consult doctor').

/* 78. Syphilis */
symptom(syphilis, [painless_sores_on_genitals_rectum_or_mouth, rash, swollen_lymph_nodes, fever, sore_throat, muscle_aches, fatigue, weight_loss, headache]).
treatment(syphilis, 'Consult doctor').

/* 79. Trichomoniasis */
symptom(trichomoniasis, [frothy_greenish_yellow_vaginal_discharge, strong_vaginal_odor, vaginal_itching_or_irritation, discomfort_during_intercourse, painful_urination]).
treatment(trichomoniasis, 'Consult doctor').

/* 80. Herpes Simplex Virus (HSV) */
symptom(hsv, [painful_blisters_or_ulcers, itching, burning_sensation, flu_like_symptoms, swollen_lymph_nodes]).
treatment(hsv, 'Consult doctor').

/* 81. Human Papillomavirus (HPV) */
symptom(hpv, [genital_warts, common_warts, plantar_warts, flat_warts, cervical_dysplasia]).
treatment(hpv, 'Consult doctor').

/* 82. Human Immunodeficiency Virus (HIV) */
symptom(hiv, [fever, chills, rash, night_sweats, muscle_aches, sore_throat, fatigue, swollen_lymph_nodes, mouth_ulcers]).
treatment(hiv, 'Consult doctor').

/* 83. Endometriosis */
symptom(endometriosis, [painful_periods, pain_during_intercourse, pain_with_bowel_movements_or_urination, excessive_bleeding, infertility, fatigue, diarrhea, constipation, bloating, nausea]).
treatment(endometriosis, 'Consult doctor').

/* 84. Polycystic Ovary Syndrome (PCOS) */
symptom(pcos, [irregular_periods, excess_androgen, polycystic_ovaries, weight_gain, thinning_hair, acne, fertility_issues]).
treatment(pcos, 'Consult doctor').

/* 85. Interstitial Cystitis (Painful Bladder Syndrome) */
symptom(interstitial_cystitis, [chronic_pelvic_pain, persistent_urge_to_urinate, frequent_urination, pain_during_intercourse]).
treatment(interstitial_cystitis, 'Consult doctor').

/* 86. Irritable Bowel Syndrome (IBS) */
symptom(ibs_2, [abdominal_pain, cramping, bloating, gas, diarrhea, constipation, mucus_in_stool]).
treatment(ibs_2, 'Consult doctor').

/* 87. Celiac Disease */
symptom(celiac_disease_2, [diarrhea, fatigue, weight_loss, bloating, gas, abdominal_pain, nausea, vomiting, constipation]).
treatment(celiac_disease_2, 'Consult doctor').

/* 88. Crohn's Disease */
symptom(crohns_disease, [diarrhea, fever, fatigue, abdominal_pain_and_cramping, blood_in_stool, mouth_sores, reduced_appetite, weight_loss, perianal_disease]).
treatment(crohns_disease, 'Consult doctor').

/* 89. Ulcerative Colitis */
symptom(ulcerative_colitis, [diarrhea, blood_or_pus_in_stool, abdominal_pain_and_cramping, rectal_pain, rectal_bleeding, urgency_to_defecate, weight_loss, fatigue, fever]).
treatment(ulcerative_colitis, 'Consult doctor').

/* 90. Diverticulitis */
symptom(diverticulitis, [persistent_pain_in_lower_left_abdomen, nausea_and_vomiting, fever, abdominal_tenderness, constipation, diarrhea]).
treatment(diverticulitis, 'Consult doctor').

/* 91. Panic Disorder */
symptom(panic_disorder, [recurrent_panic_attacks, sudden_intense_fear, palpitations, sweating, trembling, shortness_of_breath, chest_pain, nausea, dizziness, fear_of_losing_control]).
treatment(panic_disorder, 'Consult doctor').

/* 92. Obsessive-Compulsive Disorder (OCD) */
symptom(ocd, [recurrent_unwanted_thoughts, repetitive_behaviors, anxiety, distress, ritualistic_behaviors]).
treatment(ocd, 'Consult doctor').

/* 93. Bipolar Disorder */
symptom(bipolar_disorder, [extreme_mood_swings, manic_episodes, depressive_episodes]).
treatment(bipolar_disorder, 'Consult doctor').

/* 94. Schizophrenia */
symptom(schizophrenia, [hallucinations, delusions, disorganized_thinking, abnormal_motor_behavior, negative_symptoms]).
treatment(schizophrenia, 'Consult doctor').

/* 95. Post-Traumatic Stress Disorder (PTSD) */
symptom(ptsd, [flashbacks, nightmares, severe_anxiety, uncontrollable_thoughts, emotional_numbness, irritability]).
treatment(ptsd, 'Consult doctor').

/* 96. Major Depressive Disorder */
symptom(major_depressive_disorder, [persistent_sadness, loss_of_interest, changes_in_appetite, changes_in_sleep_patterns, fatigue, feelings_of_worthlessness, difficulty_concentrating]).
treatment(major_depressive_disorder, 'Consult doctor').

/* 97. Anorexia Nervosa */
symptom(anorexia_nervosa, [extreme_weight_loss, restricted_eating, intense_fear_of_gaining_weight, distorted_body_image, excessive_exercise]).
treatment(anorexia_nervosa, 'Consult doctor').

/* 98. Bulimia Nervosa */
symptom(bulimia_nervosa, [episodes_of_binge_eating, purging, fear_of_gaining_weight, distorted_body_image]).
treatment(bulimia_nervosa, 'Consult doctor').

/* 99. Generalized Anxiety Disorder (GAD) */
symptom(generalized_anxiety_disorder, [excessive_worry, restlessness, fatigue, difficulty_concentrating, irritability, muscle_tension, sleep_disturbances]).
treatment(generalized_anxiety_disorder, 'Consult doctor').

/* 100. Social Anxiety Disorder */
symptom(social_anxiety_disorder, [intense_fear_of_social_situations, avoidance_of_social_interactions, fear_of_being_judged, excessive_self_consciousness, blushing, sweating]).
treatment(social_anxiety_disorder, 'Consult doctor').

/* 101. Seasonal Affective Disorder (SAD) */
symptom(seasonal_affective_disorder, [depression_in_specific_season, low_energy, hypersomnia, overeating, weight_gain, social_withdrawal]).
treatment(seasonal_affective_disorder, 'Consult doctor').

/* 102. Borderline Personality Disorder (BPD) */
symptom(borderline_personality_disorder, [intense_fear_of_abandonment, unstable_relationships, impulsive_behavior, mood_swings, feelings_of_emptiness, self_harm, difficulty_controlling_anger]).
treatment(borderline_personality_disorder, 'Consult doctor').

/* 103. Chronic Fatigue Syndrome (CFS) */
symptom(chronic_fatigue_syndrome_2, [severe_fatigue, sleep_problems, difficulty_concentrating, muscle_and_joint_pain, headaches, sore_throat, swollen_lymph_nodes]).
treatment(chronic_fatigue_syndrome_2, 'Consult doctor').

/* 104. Raynaud's Phenomenon */
symptom(raynauds_phenomenon, [color_changes_in_skin, numbness, tingling, pain_in_fingers_and_toes]).
treatment(raynauds_phenomenon, 'Consult doctor').

/* 105. Sjogren's Syndrome */
symptom(sjogrens_syndrome, [dry_eyes, dry_mouth, joint_pain, swelling, fatigue, persistent_dry_cough, skin_rashes, vaginal_dryness]).
treatment(sjogrens_syndrome, 'Consult doctor').

/* 106. Systemic Lupus Erythematosus (SLE) */
symptom(sle, [fatigue, fever, joint_pain, skin_rashes, photosensitivity, mouth_ulcers, raynauds_phenomenon, chest_pain]).
treatment(sle, 'Consult doctor').

/* 107. Rheumatic Fever */
symptom(rheumatic_fever, [fever, painful_tender_joints, red_hot_or_swollen_joints, painless_nodules, chest_pain, heart_murmur, fatigue, flat_rash]).
treatment(rheumatic_fever, 'Consult doctor').

/* 108. Psoriatic Arthritis */
symptom(psoriatic_arthritis, [joint_pain, stiffness, swelling, swollen_fingers_and_toes, foot_pain, lower_back_pain, nail_changes]).
treatment(psoriatic_arthritis, 'Consult doctor').

/* 109. Scleroderma */
symptom(scleroderma, [tightening_and_hardening_of_skin, raynauds_phenomenon, heartburn, difficulty_swallowing, shortness_of_breath, joint_pain]).
treatment(scleroderma, 'Consult doctor').

/* 110. Hypersensitivity Pneumonitis */
symptom(hypersensitivity_pneumonitis, [shortness_of_breath, cough, fatigue, chills, muscle_aches, loss_of_appetite, weight_loss]).
treatment(hypersensitivity_pneumonitis, 'Consult doctor').

/* 111. Sarcoidosis */
symptom(sarcoidosis, [fatigue, fever, swollen_lymph_nodes, weight_loss, shortness_of_breath, persistent_dry_cough, chest_pain, skin_lesions]).
treatment(sarcoidosis, 'Consult doctor').

/* 112. Amyotrophic Lateral Sclerosis (ALS) */
symptom(als, [muscle_weakness, twitching, cramping, difficulty_speaking, difficulty_swallowing, difficulty_breathing, paralysis]).
treatment(als, 'Consult doctor').

/* 113. Huntington's Disease */
symptom(huntingtons_disease, [involuntary_jerking_movements, muscle_problems, difficulty_with_speech_and_swallowing, cognitive_decline, depression, mood_swings]).
treatment(huntingtons_disease, 'Consult doctor').

/* 114. Motor Neurone Disease (MND) */
symptom(mnd, [progressive_muscle_weakness, slurred_speech, difficulty_swallowing, muscle_cramps, twitches, weight_loss]).
treatment(mnd, 'Consult doctor').

/* 115. Myasthenia Gravis */
symptom(myasthenia_gravis, [muscle_weakness, drooping_eyelids, double_vision, difficulty_swallowing, shortness_of_breath, altered_speech, facial_muscle_weakness]).
treatment(myasthenia_gravis, 'Consult doctor').

/* 116. Ehlers-Danlos Syndrome (EDS) */
symptom(ehlers_danlos_syndrome, [hypermobile_joints, stretchy_skin, fragile_skin, easy_bruising, chronic_pain, scoliosis, early_onset_arthritis]).
treatment(ehlers_danlos_syndrome, 'Consult doctor').

/* 117. Marfan Syndrome */
symptom(marfan_syndrome, [tall_and_slender_build, disproportionately_long_limbs, long_fingers, heart_murmurs, extreme_nearsightedness, curved_spine, flat_feet]).
treatment(marfan_syndrome, 'Consult doctor').

/* 118. Turner Syndrome */
symptom(turner_syndrome, [short_stature, webbed_neck, low_set_ears, low_hairline, swelling_of_hands_and_feet, cardiac_defects, infertility]).
treatment(turner_syndrome, 'Consult doctor').

/* 119. Klinefelter Syndrome */
symptom(klinefelter_syndrome, [low_testosterone, reduced_muscle_mass, reduced_body_hair, enlarged_breast_tissue, tall_stature, learning_difficulties, delayed_speech]).
treatment(klinefelter_syndrome, 'Consult doctor').

/* 120. Cystic Fibrosis */
symptom(cystic_fibrosis, [persistent_cough_with_thick_mucus, wheezing, breathlessness, repeated_lung_infections, sinusitis, poor_growth, weight_gain_despite_good_appetite, greasy_bulky_stools]).
treatment(cystic_fibrosis, 'Consult doctor').

/* 121. Alport Syndrome */
symptom(alport_syndrome, [progressive_loss_of_kidney_function, hearing_loss, eye_abnormalities]).
treatment(alport_syndrome, 'Consult doctor').

/* 122. Fabry Disease */
symptom(fabry_disease, [pain_in_hands_and_feet, clusters_of_small_dark_red_spots, decreased_sweating, corneal_opacity, hearing_loss, kidney_damage, heart_problems]).
treatment(fabry_disease, 'Consult doctor').

/* 123. Hemochromatosis */
symptom(hemochromatosis, [joint_pain, fatigue, weakness, diabetes, loss_of_sex_drive, impotence, heart_failure, liver_failure, bronze_or_gray_skin_color]).
treatment(hemochromatosis, 'Consult doctor').

/* 124. Wilson's Disease */
symptom(wilsons_disease, [fatigue, lack_of_appetite, abdominal_pain, jaundice, golden_brown_eye_discoloration, fluid_buildup_in_legs, uncontrolled_movements, muscle_stiffness, speech_problems]).
treatment(wilsons_disease, 'Consult doctor').

/* 125. Phenylketonuria (PKU) */
symptom(pku, [intellectual_disability, delayed_development, behavioral_problems, psychiatric_disorders, musty_odor, skin_or_urine_eczema, fair_skin, blue_eyes]).
treatment(pku, 'Consult doctor').

/* 126. Hyperparathyroidism */
symptom(hyperparathyroidism, [fragile_bones, kidney_stones, excessive_urination, abdominal_pain, tiredness, depression, bone_and_joint_pain, nausea, vomiting, loss_of_appetite]).
treatment(hyperparathyroidism, 'Consult doctor').

/* 127. Hypoparathyroidism */
symptom(hypoparathyroidism, [tingling_in_fingertips, tingling_in_toes, tingling_in_lips, muscle_aches, muscle_cramps, twitching, fatigue, painful_menstrual_periods, patchy_hair_loss]).
treatment(hypoparathyroidism, 'Consult doctor').

/* 128. Addison's Disease (duplicate entry as per list) */
symptom(addisons_disease_2, [extreme_fatigue, weight_loss, decreased_appetite, darkening_of_skin, low_blood_pressure, salt_craving, low_blood_sugar, nausea, diarrhea, vomiting, abdominal_pain, muscle_or_joint_pains]).
treatment(addisons_disease_2, 'Consult doctor').

/* 129. Cushing's Syndrome (duplicate entry as per list) */
symptom(cushings_syndrome_2, [weight_gain, pink_or_purple_stretch_marks, thinning_skin, easy_bruising, acne, fatigue, muscle_weakness, high_blood_pressure, bone_loss, diabetes]).
treatment(cushings_syndrome_2, 'Consult doctor').

/* 130. Graves' Disease */
symptom(graves_disease, [anxiety, irritability, tremor_of_hands, heat_sensitivity, weight_loss, enlarged_thyroid, bulging_eyes, fatigue, thick_red_skin_on_shins]).
treatment(graves_disease, 'Consult doctor').

/* 131. Hashimoto's Thyroiditis */
symptom(hashimotos_thyroiditis, [fatigue, weight_gain, cold_intolerance, muscle_weakness, joint_pain, stiffness, constipation, dry_skin, puffy_face, hoarseness]).
treatment(hashimotos_thyroiditis, 'Consult doctor').

/* 132. Pheochromocytoma */
symptom(pheochromocytoma, [high_blood_pressure, headache, sweating, rapid_heartbeat, tremors, shortness_of_breath, panic_attack_symptoms]).
treatment(pheochromocytoma, 'Consult doctor').

/* 133. Sarcoidosis (duplicate entry as per list) */
symptom(sarcoidosis_2, [fatigue, fever, swollen_lymph_nodes, weight_loss, persistent_dry_cough, shortness_of_breath, chest_pain, skin_lesions]).
treatment(sarcoidosis_2, 'Consult doctor').

/* 134. Wegener's Granulomatosis (Granulomatosis with Polyangiitis) */
symptom(wegener_granulomatosis, [sinus_pain_and_drainage, nasal_or_oral_ulcers, cough, shortness_of_breath, kidney_issues, joint_pain, rashes, fever, weight_loss]).
treatment(wegener_granulomatosis, 'Consult doctor').

/* 135. Giant Cell Arteritis */
symptom(giant_cell_arteritis, [headaches, scalp_tenderness, jaw_pain, vision_problems, fever, unintentional_weight_loss, fatigue]).
treatment(giant_cell_arteritis, 'Consult doctor').

/* 136. Takayasu's Arteritis */
symptom(takayasus_arteritis, [fatigue, unintended_weight_loss, muscle_and_joint_pain, fever, night_sweats, weak_pulse, high_blood_pressure, chest_pain]).
treatment(takayasus_arteritis, 'Consult doctor').

/* 137. Lupus Nephritis */
symptom(lupus_nephritis, [foamy_urine, high_blood_pressure, swelling_in_legs, joint_pain_and_swelling, skin_rash, fever, fatigue]).
treatment(lupus_nephritis, 'Consult doctor').

/* 138. Vasculitis */
symptom(vasculitis, [fever, headache, fatigue, weight_loss, muscle_and_joint_pain, numbness_or_weakness, rash]).
treatment(vasculitis, 'Consult doctor').

/* 139. Behcet's Disease */
symptom(behcets_disease, [mouth_sores, genital_sores, eye_inflammation, skin_problems, joint_pain, blood_vessel_inflammation, digestive_issues]).
treatment(behcets_disease, 'Consult doctor').

/* 140. Hepatitis A */
symptom(hepatitis_a, [fatigue, sudden_nausea_and_vomiting, abdominal_pain, clay_colored_bowel_movements, loss_of_appetite, low_grade_fever, dark_urine, joint_pain, jaundice]).
treatment(hepatitis_a, 'Consult doctor').

/* 141. Hepatitis B */
symptom(hepatitis_b, [fatigue, sudden_nausea_and_vomiting, abdominal_pain, loss_of_appetite, low_grade_fever, dark_urine, joint_pain, jaundice]).
treatment(hepatitis_b, 'Consult doctor').

/* 142. Hepatitis C */
symptom(hepatitis_c, [fatigue, sudden_nausea_and_vomiting, abdominal_pain, loss_of_appetite, low_grade_fever, dark_urine, joint_pain, jaundice]).
treatment(hepatitis_c, 'Consult doctor').

/* 143. Autoimmune Hepatitis */
symptom(autoimmune_hepatitis, [fatigue, enlarged_liver, jaundice, itching, skin_rashes, joint_pain, abdominal_discomfort, spider_angiomas, enlarged_spleen]).
treatment(autoimmune_hepatitis, 'Consult doctor').

/* --- Extension: Diseases 143 to 298 --- */

/* 143. Autoimmune Hepatitis */
symptom(autoimmune_hepatitis, [fatigue, enlarged_liver, jaundice, itching, skin_rashes, joint_pain, abdominal_discomfort, spider_angiomas, enlarged_spleen]).
treatment(autoimmune_hepatitis, 'Consult doctor').

/* 144. Primary Biliary Cholangitis (PBC) */
symptom(primary_biliary_cholangitis, [fatigue, itchy_skin, dry_eyes_and_mouth, pain_in_upper_right_abdomen, swelling_of_feet_and_ankles, fluid_buildup_in_abdomen, yellowing_of_skin_and_eyes]).
treatment(primary_biliary_cholangitis, 'Consult doctor').

/* 145. Hemolytic Anemia */
symptom(hemolytic_anemia, [fatigue, dizziness, paleness, shortness_of_breath, dark_urine, jaundice, fever, weakness, heart_murmur]).
treatment(hemolytic_anemia, 'Consult doctor').

/* 146. Myelodysplastic Syndromes (MDS) */
symptom(myelodysplastic_syndromes, [fatigue, shortness_of_breath, unusual_pallor, easy_bruising_or_bleeding, frequent_infections]).
treatment(myelodysplastic_syndromes, 'Consult doctor').

/* 147. Aplastic Anemia */
symptom(aplastic_anemia, [fatigue, shortness_of_breath, rapid_or_irregular_heart_rate, pale_skin, frequent_infections, easy_bruising, nosebleeds, bleeding_gums, prolonged_bleeding, skin_rash]).
treatment(aplastic_anemia, 'Consult doctor').

/* 148. Duchenne Muscular Dystrophy (DMD) */
symptom(duchenne_muscular_dystrophy, [progressive_muscle_weakness, frequent_falls, difficulty_rising, trouble_running_and_jumping, large_calf_muscles, learning_disabilities]).
treatment(duchenne_muscular_dystrophy, 'Consult doctor').

/* 149. Becker Muscular Dystrophy (BMD) */
symptom(becker_muscular_dystrophy, [muscle_weakness, delayed_motor_development, difficulty_walking, frequent_falls, muscle_cramps, enlarged_calves]).
treatment(becker_muscular_dystrophy, 'Consult doctor').

/* 150. Charcot-Marie-Tooth Disease (CMT) */
symptom(charcot_marie_toth_disease, [weakness_in_legs, ankles_and_feet, loss_of_muscle_bulk, high_foot_arches, curled_toes, difficulty_lifting_foot, decreased_ability_to_run, foot_drop, frequent_tripping]).
treatment(charcot_marie_toth_disease, 'Consult doctor').

/* 151. Friedreich's Ataxia */
symptom(friedreichs_ataxia, [difficulty_walking, poor_coordination, scoliosis, heart_disease, vision_impairment, hearing_loss, diabetes]).
treatment(friedreichs_ataxia, 'Consult doctor').

/* 152. Spinal Muscular Atrophy (SMA) */
symptom(spinal_muscular_atrophy, [muscle_weakness, lack_of_motor_development, loss_of_motor_skills, poor_muscle_tone, twitching, difficulty_breathing_and_swallowing]).
treatment(spinal_muscular_atrophy, 'Consult doctor').

/* 153. Guillain-Barre Syndrome (GBS) */
symptom(guillain_barre_syndrome, [weakness_and_tingling_in_extremities, unsteady_walking, difficulty_with_facial_movements, double_vision, difficulty_speaking, difficulty_breathing, severe_pain]).
treatment(guillain_barre_syndrome, 'Consult doctor').

/* 154. Peripheral Neuropathy */
symptom(peripheral_neuropathy, [gradual_onset_of_numbness, tingling, sharp_or_jabbing_pain, sensitivity_to_touch, muscle_weakness, lack_of_coordination, paralysis]).
treatment(peripheral_neuropathy, 'Consult doctor').

/* 155. Amyloidosis */
symptom(amyloidosis, [severe_fatigue, swelling_in_ankles_and_legs, shortness_of_breath, numbness_or_tingling, diarrhea_or_constipation, weight_loss, skin_changes]).
treatment(amyloidosis, 'Consult doctor').

/* 156. Hemolytic Uremic Syndrome (HUS) */
symptom(hemolytic_uremic_syndrome, [bloody_diarrhea, abdominal_pain, vomiting, low_urine_output, fatigue, unexplained_bruising, nosebleeds, pale_skin]).
treatment(hemolytic_uremic_syndrome, 'Consult doctor').

/* 157. Thalassemia */
symptom(thalassemia, [fatigue, weakness, pale_skin, slow_growth, abdominal_swelling, dark_urine, facial_bone_deformities]).
treatment(thalassemia, 'Consult doctor').

/* 158. Sickle Cell Disease */
symptom(sickle_cell_disease, [anemia, episodes_of_pain, swelling_of_hands_and_feet, frequent_infections, delayed_growth, vision_problems]).
treatment(sickle_cell_disease, 'Consult doctor').

/* 159. Gaucher Disease */
symptom(gaucher_disease, [enlarged_spleen_and_liver, severe_fatigue, anemia, bruising_and_bleeding, bone_pain_and_fractures]).
treatment(gaucher_disease, 'Consult doctor').

/* 160. Pompe Disease */
symptom(pompe_disease, [muscle_weakness, breathing_problems, enlarged_liver, heart_problems, difficulty_feeding_and_swallowing, poor_weight_gain]).
treatment(pompe_disease, 'Consult doctor').

/* 161. Hunter Syndrome (Mucopolysaccharidosis Type II) */
symptom(hunter_syndrome, [distinct_facial_features, enlarged_head, frequent_upper_respiratory_infections, sleep_apnea, joint_stiffness, hearing_loss, heart_problems]).
treatment(hunter_syndrome, 'Consult doctor').

/* 162. Hurler Syndrome (Mucopolysaccharidosis Type I) */
symptom(hurler_syndrome, [developmental_delay, coarse_facial_features, joint_stiffness, enlarged_liver_and_spleen, heart_disease, corneal_clouding]).
treatment(hurler_syndrome, 'Consult doctor').

/* 163. Tay-Sachs Disease */
symptom(tay_sachs_disease, [loss_of_motor_skills, increased_startle_response, seizures, vision_and_hearing_loss, muscle_weakness, movement_issues]).
treatment(tay_sachs_disease, 'Consult doctor').

/* 164. Canavan Disease */
symptom(canavan_disease, [developmental_delay, muscle_weakness, poor_head_control, abnormal_muscle_tone, large_head, blindness, seizures]).
treatment(canavan_disease, 'Consult doctor').

/* 165. Lesch-Nyhan Syndrome */
symptom(lesch_nyhan_syndrome, [self_mutilation_behaviors, muscle_rigidity, involuntary_movements, kidney_stones, gout, delayed_motor_development]).
treatment(lesch_nyhan_syndrome, 'Consult doctor').

/* 166. Krabbe Disease */
symptom(krabbe_disease, [irritability, muscle_weakness, feeding_difficulties, episodes_of_fever_without_infection, stiff_posture, slowed_development]).
treatment(krabbe_disease, 'Consult doctor').

/* 167. Metachromatic Leukodystrophy */
symptom(metachromatic_leukodystrophy, [muscle_wasting, weakness, vision_loss, hearing_loss, seizures, developmental_delays, behavior_changes]).
treatment(metachromatic_leukodystrophy, 'Consult doctor').

/* 168. Adrenoleukodystrophy (ALD) */
symptom(adrenoleukodystrophy, [progressive_loss_of_neurological_functions, hyperactivity, visual_disturbances, hearing_loss, seizures, adrenal_gland_dysfunction]).
treatment(adrenoleukodystrophy, 'Consult doctor').

/* 169. Alexander Disease */
symptom(alexander_disease, [enlarged_head, seizures, stiffness_in_arms_and_legs, intellectual_disability, developmental_delays, difficulty_swallowing]).
treatment(alexander_disease, 'Consult doctor').

/* 170. Rett Syndrome */
symptom(rett_syndrome, [slowed_growth, loss_of_normal_movement, loss_of_communication_abilities, abnormal_hand_movements, breathing_problems]).
treatment(rett_syndrome, 'Consult doctor').

/* 171. Angelman Syndrome */
symptom(angelman_syndrome, [developmental_delays, intellectual_disability, severe_speech_impairment, movement_and_balance_issues, happy_demeanor, frequent_laughter]).
treatment(angelman_syndrome, 'Consult doctor').

/* 172. Prader-Willi Syndrome */
symptom(prader_willi_syndrome, [poor_muscle_tone, feeding_difficulties, delayed_development, insatiable_appetite, obesity, intellectual_disability, behavior_problems]).
treatment(prader_willi_syndrome, 'Consult doctor').

/* 173. Noonan Syndrome */
symptom(noonan_syndrome, [unusual_facial_characteristics, short_stature, heart_defects, bleeding_problems, skeletal_malformations, learning_difficulties]).
treatment(noonan_syndrome, 'Consult doctor').

/* 174. Williams Syndrome */
symptom(williams_syndrome, [distinct_facial_features, cardiovascular_problems, developmental_delays, learning_disabilities, outgoing_personality]).
treatment(williams_syndrome, 'Consult doctor').

/* 175. Huntington's Disease */
symptom(huntingtons_disease, [involuntary_jerking_movements, muscle_problems, difficulty_with_speech_and_swallowing, cognitive_decline, depression, mood_swings]).
treatment(huntingtons_disease, 'Consult doctor').

/* 176. Treacher Collins Syndrome */
symptom(treacher_collins_syndrome, [downward_slanting_eyes, notch_in_lower_eyelids, underdeveloped_cheekbones, small_jaw, malformed_ears, hearing_loss]).
treatment(treacher_collins_syndrome, 'Consult doctor').

/* 177. Cri du Chat Syndrome */
symptom(cri_du_chat_syndrome, [high_pitched_cat_like_cry, intellectual_disability, delayed_development, microcephaly, low_birth_weight, weak_muscle_tone, distinctive_facial_features]).
treatment(cri_du_chat_syndrome, 'Consult doctor').

/* 178. Niemann-Pick Disease */
symptom(niemann_pick_disease, [difficulty_moving_limbs, enlarged_liver_and_spleen, jaundice, lung_disease, intellectual_decline, progressive_loss_of_motor_skills]).
treatment(niemann_pick_disease, 'Consult doctor').

/* 179. Tay-Sachs Disease (duplicate entry) */
symptom(tay_sachs_disease_dup, [loss_of_motor_skills, increased_startle_response, seizures, vision_and_hearing_loss, muscle_weakness, movement_issues]).
treatment(tay_sachs_disease_dup, 'Consult doctor').

/* 180. Canavan Disease (duplicate entry) */
symptom(canavan_disease_dup, [developmental_delay, muscle_weakness, poor_head_control, abnormal_muscle_tone, large_head, blindness, seizures]).
treatment(canavan_disease_dup, 'Consult doctor').

/* 181. Maple Syrup Urine Disease */
symptom(maple_syrup_urine_disease, [sweet_smelling_urine, poor_feeding, vomiting, lack_of_energy, developmental_delays, seizures]).
treatment(maple_syrup_urine_disease, 'Consult doctor').

/* 182. Zellweger Syndrome */
symptom(zellweger_syndrome, [poor_muscle_tone, feeding_problems, seizures, hearing_loss, vision_loss, distinctive_facial_features, liver_dysfunction]).
treatment(zellweger_syndrome, 'Consult doctor').

/* 183. Cockayne Syndrome */
symptom(cockayne_syndrome, [growth_failure, small_head_size, developmental_delays, photosensitivity, vision_and_hearing_loss, premature_aging]).
treatment(cockayne_syndrome, 'Consult doctor').

/* 184. Progeria */
symptom(progeria, [growth_failure, aged_looking_skin, loss_of_body_fat_and_hair, stiffness_of_joints, hip_dislocation, cardiovascular_disease]).
treatment(progeria, 'Consult doctor').

/* 185. Bloom Syndrome */
symptom(bloom_syndrome, [short_stature, sun_sensitive_skin_changes, increased_risk_of_cancer, chronic_lung_problems, diabetes]).
treatment(bloom_syndrome, 'Consult doctor').

/* 186. Werner Syndrome */
symptom(werner_syndrome, [premature_aging, short_stature, cataracts, skin_changes, diabetes, osteoporosis, increased_cancer_risk]).
treatment(werner_syndrome, 'Consult doctor').

/* 187. Fanconi Anemia */
symptom(fanconi_anemia, [bone_marrow_failure, physical_abnormalities, short_stature, skin_discoloration, increased_cancer_risk, developmental_delays]).
treatment(fanconi_anemia, 'Consult doctor').

/* 188. Lesch-Nyhan Syndrome (duplicate entry) */
symptom(lesch_nyhan_syndrome_dup, [self_mutilation_behaviors, muscle_rigidity, involuntary_movements, kidney_stones, gout, delayed_motor_development]).
treatment(lesch_nyhan_syndrome_dup, 'Consult doctor').

/* 189. Alkaptonuria */
symptom(alkaptonuria, [dark_urine, arthritis, darkened_earwax, dark_spots_on_sclera, heart_valve_issues, kidney_stones]).
treatment(alkaptonuria, 'Consult doctor').

/* 190. Porphyria */
symptom(porphyria, [severe_abdominal_pain, vomiting, sensitivity_to_light, reddish_brown_urine, muscle_weakness, seizures, mental_disturbances]).
treatment(porphyria, 'Consult doctor').

/* 191. Fabry Disease (duplicate entry) */
symptom(fabry_disease_dup, [pain_in_hands_and_feet, clusters_of_small_dark_red_spots, decreased_sweating, corneal_opacity, hearing_loss, kidney_damage, heart_problems]).
treatment(fabry_disease_dup, 'Consult doctor').

/* 192. Gaucher Disease (duplicate entry) */
symptom(gaucher_disease_dup, [enlarged_spleen_and_liver, severe_fatigue, anemia, bruising_and_bleeding, bone_pain_and_fractures]).
treatment(gaucher_disease_dup, 'Consult doctor').

/* 193. Hurler Syndrome */
symptom(hurler_syndrome, [developmental_delay, coarse_facial_features, joint_stiffness, enlarged_liver_and_spleen, heart_disease, corneal_clouding]).
treatment(hurler_syndrome, 'Consult doctor').

/* 194. Hunter Syndrome (duplicate entry) */
symptom(hunter_syndrome_dup, [distinct_facial_features, enlarged_head, frequent_upper_respiratory_infections, sleep_apnea, joint_stiffness, hearing_loss, heart_problems]).
treatment(hunter_syndrome_dup, 'Consult doctor').

/* 195. Krabbe Disease (duplicate entry) */
symptom(krabbe_disease_dup, [irritability, muscle_weakness, feeding_difficulties, episodes_of_fever_without_infection, stiff_posture, slowed_development]).
treatment(krabbe_disease_dup, 'Consult doctor').

/* 196. Metachromatic Leukodystrophy (duplicate entry) */
symptom(metachromatic_leukodystrophy_dup, [muscle_wasting, weakness, vision_loss, hearing_loss, seizures, developmental_delays, behavior_changes]).
treatment(metachromatic_leukodystrophy_dup, 'Consult doctor').

/* 197. Adrenoleukodystrophy (ALD) (duplicate entry) */
symptom(adrenoleukodystrophy_dup, [progressive_loss_of_neurological_functions, hyperactivity, visual_disturbances, hearing_loss, seizures, adrenal_gland_dysfunction]).
treatment(adrenoleukodystrophy_dup, 'Consult doctor').

/* 198. Alexander Disease (duplicate entry) */
symptom(alexander_disease_dup, [enlarged_head, seizures, stiffness_in_arms_and_legs, intellectual_disability, developmental_delays, difficulty_swallowing]).
treatment(alexander_disease_dup, 'Consult doctor').

/* 199. Rett Syndrome (duplicate entry) */
symptom(rett_syndrome_dup, [slowed_growth, loss_of_normal_movement, loss_of_communication_abilities, abnormal_hand_movements, breathing_problems]).
treatment(rett_syndrome_dup, 'Consult doctor').

/* 200. Angelman Syndrome (duplicate entry) */
symptom(angelman_syndrome_dup, [developmental_delays, intellectual_disability, severe_speech_impairment, movement_and_balance_issues, happy_demeanor, frequent_laughter]).
treatment(angelman_syndrome_dup, 'Consult doctor').

/* 201. Prader-Willi Syndrome (duplicate entry) */
symptom(prader_willi_syndrome_dup, [poor_muscle_tone, feeding_difficulties, delayed_development, insatiable_appetite, obesity, intellectual_disability, behavior_problems]).
treatment(prader_willi_syndrome_dup, 'Consult doctor').

/* 202. Noonan Syndrome (duplicate entry) */
symptom(noonan_syndrome_dup, [unusual_facial_characteristics, short_stature, heart_defects, bleeding_problems, skeletal_malformations, learning_difficulties]).
treatment(noonan_syndrome_dup, 'Consult doctor').

/* 203. Williams Syndrome (duplicate entry) */
symptom(williams_syndrome_dup, [distinct_facial_features, cardiovascular_problems, developmental_delays, learning_disabilities, outgoing_personality]).
treatment(williams_syndrome_dup, 'Consult doctor').

/* 204. Huntington's Disease (duplicate entry) */
symptom(huntingtons_disease_dup, [involuntary_jerking_movements, muscle_problems, difficulty_with_speech_and_swallowing, cognitive_decline, depression, mood_swings]).
treatment(huntingtons_disease_dup, 'Consult doctor').

/* 205. Tuberous Sclerosis Complex (TSC) */
symptom(tuberous_sclerosis_complex, [seizures, developmental_delay, behavioral_problems, skin_abnormalities, lung_and_kidney_disease, benign_tumors]).
treatment(tuberous_sclerosis_complex, 'Consult doctor').

/* 206. von Hippel-Lindau Disease */
symptom(von_hippel_lindau_disease, [tumors_and_cysts, headaches, balance_problems, hypertension, vision_problems, dizziness]).
treatment(von_hippel_lindau_disease, 'Consult doctor').

/* 207. Neurofibromatosis Type 1 (NF1) */
symptom(neurofibromatosis_type_1, [cafe_au_lait_spots, neurofibromas, bone_deformities, learning_disabilities, vision_problems]).
treatment(neurofibromatosis_type_1, 'Consult doctor').

/* 208. Neurofibromatosis Type 2 (NF2) */
symptom(neurofibromatosis_type_2, [hearing_loss, ringing_in_ears, balance_issues, cataracts, skin_flaps]).
treatment(neurofibromatosis_type_2, 'Consult doctor').

/* 209. Schwannomatosis */
symptom(schwannomatosis, [chronic_pain, numbness, muscle_weakness, tumors_in_nervous_system]).
treatment(schwannomatosis, 'Consult doctor').

/* 210. Sturge-Weber Syndrome */
symptom(sturge_weber_syndrome, [port_wine_stain, seizures, intellectual_disability, glaucoma, unilateral_paralysis]).
treatment(sturge_weber_syndrome, 'Consult doctor').

/* 211. Wiskott-Aldrich Syndrome */
symptom(wiskott_aldrich_syndrome, [easy_bruising, bleeding, recurrent_infections, eczema, reduced_platelet_count]).
treatment(wiskott_aldrich_syndrome, 'Consult doctor').

/* 212. Xeroderma Pigmentosum */
symptom(xeroderma_pigmentosum, [extreme_sensitivity_to_uv, severe_sunburns, skin_blisters, freckles, skin_cancer]).
treatment(xeroderma_pigmentosum, 'Consult doctor').

/* 213. Sjogren-Larsson Syndrome */
symptom(sjogren_larsson_syndrome, [dry_scaly_skin, intellectual_disability, speech_difficulties, seizures, spasticity]).
treatment(sjogren_larsson_syndrome, 'Consult doctor').

/* 214. Rothmund-Thomson Syndrome */
symptom(rothmund_thomson_syndrome, [skin_abnormalities, sparse_hair, skeletal_abnormalities, dental_issues, cataracts]).
treatment(rothmund_thomson_syndrome, 'Consult doctor').

/* 215. Thalassemia (duplicate entry) */
symptom(thalassemia_dup, [fatigue, weakness, pale_or_yellowish_skin, facial_bone_deformities, slow_growth, abdominal_swelling, dark_urine]).
treatment(thalassemia_dup, 'Consult doctor').

/* 216. Hypophosphatemia */
symptom(hypophosphatemia, [muscle_weakness, bone_pain, fractures, confusion, irritability]).
treatment(hypophosphatemia, 'Consult doctor').

/* 217. Hyperphosphatemia */
symptom(hyperphosphatemia, [itching, muscle_cramps, joint_pain, calcification_in_tissues]).
treatment(hyperphosphatemia, 'Consult doctor').

/* 218. Hypomagnesemia */
symptom(hypomagnesemia, [muscle_cramps, seizures, abnormal_heart_rhythms, personality_changes]).
treatment(hypomagnesemia, 'Consult doctor').

/* 219. Hypermagnesemia */
symptom(hypermagnesemia, [nausea, vomiting, neurological_impairment, muscle_weakness, hypotension]).
treatment(hypermagnesemia, 'Consult doctor').

/* 220. Hypocalcemia */
symptom(hypocalcemia, [muscle_cramps, confusion, tingling_in_lips_and_fingers, seizures]).
treatment(hypocalcemia, 'Consult doctor').

/* 221. Hypercalcemia */
symptom(hypercalcemia, [nausea, vomiting, constipation, abdominal_pain, increased_thirst_and_urination, confusion]).
treatment(hypercalcemia, 'Consult doctor').

/* 222. Hypokalemia */
symptom(hypokalemia, [weakness, fatigue, muscle_cramps, heart_palpitations, constipation]).
treatment(hypokalemia, 'Consult doctor').

/* 223. Hyperkalemia */
symptom(hyperkalemia, [nausea, fatigue, muscle_weakness, tingling_sensations, slow_or_irregular_heartbeats]).
treatment(hyperkalemia, 'Consult doctor').

/* 224. Hypochloremia */
symptom(hypochloremia, [dehydration, fluid_loss, weakness, difficulty_breathing]).
treatment(hypochloremia, 'Consult doctor').

/* 225. Hyperchloremia */
symptom(hyperchloremia, [fatigue, weakness, excessive_thirst, high_blood_pressure]).
treatment(hyperchloremia, 'Consult doctor').

/* 226. Glycogen Storage Disease */
symptom(glycogen_storage_disease, [low_blood_sugar, enlarged_liver, muscle_cramps, delayed_growth, fatigue]).
treatment(glycogen_storage_disease, 'Consult doctor').

/* 227. Phenylketonuria (PKU) (duplicate entry) */
symptom(pku_dup, [intellectual_disability, delayed_development, behavioral_problems, psychiatric_disorders, musty_odor, skin_rashes]).
treatment(pku_dup, 'Consult doctor').

/* 228. Albinism */
symptom(albinism, [lack_of_pigment, vision_problems, increased_risk_of_skin_cancer]).
treatment(albinism, 'Consult doctor').

/* 229. Color Blindness */
symptom(color_blindness, [difficulty_distinguishing_between_colors, inability_to_see_shades]).
treatment(color_blindness, 'Consult doctor').

/* 230. Hemophilia (duplicate entry) */
symptom(hemophilia_dup, [excessive_bleeding, frequent_nosebleeds, joint_pain_and_swelling, blood_in_urine_or_stool]).
treatment(hemophilia_dup, 'Consult doctor').

/* 231. Leukodystrophy */
symptom(leukodystrophy, [progressive_loss_of_motor_skills, muscle_stiffness, seizures, developmental_delays]).
treatment(leukodystrophy, 'Consult doctor').

/* 232. Alzheimer's Disease */
symptom(alzheimers_disease, [memory_loss, confusion, difficulty_with_language, mood_swings, behavioral_changes]).
treatment(alzheimers_disease, 'Consult doctor').

/* 233. Parkinson's Disease (duplicate entry) */
symptom(parkinsons_disease_dup, [tremors, slowed_movement, muscle_stiffness, impaired_balance, changes_in_speech]).
treatment(parkinsons_disease_dup, 'Consult doctor').

/* 234. Multiple System Atrophy (MSA) */
symptom(multiple_system_atrophy, [muscle_rigidity, tremors, poor_balance, urinary_incontinence, blood_pressure_issues]).
treatment(multiple_system_atrophy, 'Consult doctor').

/* 235. Progressive Supranuclear Palsy (PSP) */
symptom(progressive_supranuclear_psy, [loss_of_balance, muscle_stiffness, difficulty_moving_eyes, speech_and_swallowing_difficulties]).
treatment(progressive_supranuclear_psy, 'Consult doctor').

/* 236. Creutzfeldt-Jakob Disease */
symptom(creutzfeldt_jakob_disease, [rapid_mental_deterioration, muscle_stiffness, twitching, difficulty_speaking, visual_disturbances]).
treatment(creutzfeldt_jakob_disease, 'Consult doctor').

/* 237. Acanthosis Nigricans */
symptom(acanthosis_nigricans, [dark_thickened_patches_of_skin]).
treatment(acanthosis_nigricans, 'Consult doctor').

/* 238. Acromegaly */
symptom(acromegaly, [enlarged_hands_and_feet, facial_changes, joint_pain, thickened_skin, vision_problems]).
treatment(acromegaly, 'Consult doctor').

/* 239. Addisonian Crisis */
symptom(addisonian_crisis, [severe_pain, vomiting, diarrhea, low_blood_pressure, loss_of_consciousness]).
treatment(addisonian_crisis, 'Consult doctor').

/* 240. Adult Still's Disease */
symptom(adult_stills_disease, [high_fevers, joint_pain, salmon_colored_bumpy_rash, sore_throat, muscle_pain]).
treatment(adult_stills_disease, 'Consult doctor').

/* 241. Agnosia */
symptom(agnosia, [inability_to_recognize_objects_people_sounds]).
treatment(agnosia, 'Consult doctor').

/* 242. Alopecia Areata */
symptom(alopecia_areata, [sudden_hair_loss_in_round_patches]).
treatment(alopecia_areata, 'Consult doctor').

/* 243. Aortic Aneurysm */
symptom(aortic_aneurysm, [sudden_intense_back_or_abdominal_pain, low_blood_pressure, loss_of_consciousness]).
treatment(aortic_aneurysm, 'Consult doctor').

/* 244. Appendicitis */
symptom(appendicitis, [pain_around_navel_shifting_to_lower_right_abdomen, nausea, vomiting, loss_of_appetite, fever]).
treatment(appendicitis, 'Consult doctor').

/* 245. Aphasia */
symptom(aphasia, [difficulty_speaking, difficulty_understanding, difficulty_reading_or_writing]).
treatment(aphasia, 'Consult doctor').

/* 246. Aplastic Anemia (duplicate entry) */
symptom(aplastic_anemia_dup, [fatigue, shortness_of_breath, rapid_or_irregular_heart_rate, pale_skin, frequent_infections]).
treatment(aplastic_anemia_dup, 'Consult doctor').

/* 247. Arrhythmias */
symptom(arrhythmias, [palpitations, shortness_of_breath, chest_pain, dizziness, fainting]).
treatment(arrhythmias, 'Consult doctor').

/* 248. Arteriosclerosis */
symptom(arteriosclerosis, [chest_pain, leg_pain, numbness, difficulty_speaking, vision_loss]).
treatment(arteriosclerosis, 'Consult doctor').

/* 249. Asperger's Syndrome */
symptom(aspergers_syndrome, [difficulty_with_social_interactions, restricted_interests, desire_for_sameness, delayed_motor_skills]).
treatment(aspergers_syndrome, 'Consult doctor').

/* 250. Asphyxia */
symptom(asphyxia, [difficulty_breathing, cyanosis, confusion, unconsciousness]).
treatment(asphyxia, 'Consult doctor').

/* 251. Barrett's Esophagus */
symptom(barretts_esophagus, [frequent_heartburn, difficulty_swallowing, chest_pain, chronic_cough, hoarseness]).
treatment(barretts_esophagus, 'Consult doctor').

/* 252. Biliary Atresia */
symptom(biliary_atresia, [yellowing_of_skin_and_eyes, dark_urine, pale_stools, poor_weight_gain, irritability]).
treatment(biliary_atresia, 'Consult doctor').

/* 253. Brugada Syndrome */
symptom(brugada_syndrome, [fainting, irregular_heartbeats, sudden_cardiac_arrest]).
treatment(brugada_syndrome, 'Consult doctor').

/* 254. Carcinoid Syndrome */
symptom(carcinoid_syndrome, [flushing, diarrhea, difficulty_breathing, rapid_heartbeat]).
treatment(carcinoid_syndrome, 'Consult doctor').

/* 255. Carpal Tunnel Syndrome */
symptom(carpal_tunnel_syndrome, [numbness, tingling, pain_in_hand_and_arm, hand_weakness]).
treatment(carpal_tunnel_syndrome, 'Consult doctor').

/* 256. Celiac Disease (duplicate entry) */
symptom(celiac_disease_dup, [diarrhea, fatigue, weight_loss, bloating, gas, abdominal_pain, nausea, vomiting, constipation]).
treatment(celiac_disease_dup, 'Consult doctor').

/* 257. Cervical Spondylosis */
symptom(cervical_spondylosis, [neck_pain_and_stiffness, headache, shoulder_and_arm_pain, muscle_weakness, tingling_in_arms]).
treatment(cervical_spondylosis, 'Consult doctor').

/* 258. Chondrocalcinosis (Pseudogout) */
symptom(chondrocalcinosis, [sudden_severe_joint_pain, swelling, redness, warmth_in_joints]).
treatment(chondrocalcinosis, 'Consult doctor').

/* 259. Chronic Fatigue Syndrome (CFS) (duplicate entry) */
symptom(chronic_fatigue_syndrome_dup, [severe_fatigue, sleep_problems, difficulty_concentrating, muscle_and_joint_pain, headaches, sore_throat, swollen_lymph_nodes]).
treatment(chronic_fatigue_syndrome_dup, 'Consult doctor').

/* 260. Chronic Obstructive Pulmonary Disease (COPD) (duplicate entry) */
symptom(copd_dup, [shortness_of_breath, wheezing, chest_tightness, chronic_cough, frequent_respiratory_infections, fatigue, blueness_of_lips]).
treatment(copd_dup, 'Consult doctor').

/* 261. Cirrhosis */
symptom(cirrhosis, [fatigue, easy_bruising, loss_of_appetite, nausea, leg_swelling, weight_loss, itchy_skin, jaundice]).
treatment(cirrhosis, 'Consult doctor').

/* 262. Cluster Headache */
symptom(cluster_headache, [severe_burning_pain_around_one_eye, swelling_around_eye, redness_in_eye, stuffy_or_runny_nose]).
treatment(cluster_headache, 'Consult doctor').

/* 263. Congenital Adrenal Hyperplasia */
symptom(congenital_adrenal_hyperplasia, [ambiguous_genitalia, early_puberty, rapid_childhood_growth, severe_acne, infertility]).
treatment(congenital_adrenal_hyperplasia, 'Consult doctor').

/* 264. Costochondritis */
symptom(costochondritis, [sharp_aching_chest_pain, pain_on_deep_breathing_or_coughing, chest_tenderness]).
treatment(costochondritis, 'Consult doctor').

/* 265. Creutzfeldt-Jakob Disease (CJD) */
symptom(creutzfeldt_jakob_disease_dup, [rapid_mental_deterioration, personality_changes, memory_problems, blurred_vision, difficulty_speaking, difficulty_swallowing, muscle_stiffness]).
treatment(creutzfeldt_jakob_disease_dup, 'Consult doctor').

/* 266. Cushing's Syndrome (duplicate entry) */
symptom(cushings_syndrome_dup, [weight_gain, pink_or_purple_stretch_marks, thinning_skin, easy_bruising, acne, fatigue, muscle_weakness, high_blood_pressure, bone_loss, diabetes]).
treatment(cushings_syndrome_dup, 'Consult doctor').

/* 267. Cystic Fibrosis (CF) (duplicate entry) */
symptom(cystic_fibrosis_dup, [persistent_cough_with_thick_mucus, wheezing, breathlessness, repeated_lung_infections, sinusitis, poor_growth, weight_gain_despite_good_appetite, greasy_bulky_stools]).
treatment(cystic_fibrosis_dup, 'Consult doctor').

/* 268. Deep Vein Thrombosis (DVT) */
symptom(deep_vein_thrombosis, [swelling_in_one_leg, pain_or_tenderness_in_one_leg, warm_skin_on_affected_leg, red_or_discolored_skin, visible_veins]).
treatment(deep_vein_thrombosis, 'Consult doctor').

/* 269. Degenerative Disc Disease */
symptom(degenerative_disc_disease, [pain_in_lower_back, buttocks_or_thighs, pain_worsening_with_sitting_or_lifting, pain_improving_with_walking]).
treatment(degenerative_disc_disease, 'Consult doctor').

/* 270. Diabetes Insipidus */
symptom(diabetes_insipidus, [extreme_thirst, large_amounts_of_diluted_urine, frequent_urination, dehydration, fatigue]).
treatment(diabetes_insipidus, 'Consult doctor').

/* 271. Diabetic Ketoacidosis (DKA) */
symptom(diabetic_ketoacidosis, [excessive_thirst, frequent_urination, nausea_and_vomiting, abdominal_pain, weakness, shortness_of_breath, fruity_scented_breath, confusion]).
treatment(diabetic_ketoacidosis, 'Consult doctor').

/* 272. Diverticulitis (duplicate entry) */
symptom(diverticulitis_dup, [persistent_lower_left_abdominal_pain, nausea_and_vomiting, fever, abdominal_tenderness, constipation, diarrhea]).
treatment(diverticulitis_dup, 'Consult doctor').

/* 273. Dysautonomia */
symptom(dysautonomia, [lightheadedness, fainting, unstable_blood_pressure, abnormal_heart_rates, malnutrition]).
treatment(dysautonomia, 'Consult doctor').

/* 274. Ehlers-Danlos Syndrome (EDS) (duplicate entry) */
symptom(ehlers_danlos_syndrome_dup, [hypermobile_joints, stretchy_skin, fragile_skin, easy_bruising, chronic_pain, scoliosis, early_onset_arthritis]).
treatment(ehlers_danlos_syndrome_dup, 'Consult doctor').

/* 275. Epilepsy (duplicate entry) */
symptom(epilepsy_dup, [seizures, loss_of_awareness, staring_spells, temporary_confusion, unusual_sensations, muscle_stiffness, sudden_jerking_movements]).
treatment(epilepsy_dup, 'Consult doctor').

/* 276. Esophageal Varices */
symptom(esophageal_varices, [vomiting_blood, black_tarry_stools, lightheadedness, loss_of_consciousness]).
treatment(esophageal_varices, 'Consult doctor').

/* 277. Fibromyalgia (duplicate entry) */
symptom(fibromyalgia_dup, [widespread_musculoskeletal_pain, fatigue, sleep_disturbances, headaches, cognitive_difficulties, irritable_bowel_syndrome, anxiety, depression]).
treatment(fibromyalgia_dup, 'Consult doctor').

/* 278. Frozen Shoulder */
symptom(frozen_shoulder, [shoulder_pain, stiffness, decreased_range_of_motion]).
treatment(frozen_shoulder, 'Consult doctor').

/* 279. Gastroparesis */
symptom(gastroparesis, [nausea, vomiting, early_satiety, bloating, abdominal_pain, weight_loss, malnutrition]).
treatment(gastroparesis, 'Consult doctor').

/* 280. Glaucoma */
symptom(glaucoma, [severe_eye_pain, nausea_and_vomiting, headache, sudden_visual_disturbance, blurred_vision, halos_around_lights, eye_redness]).
treatment(glaucoma, 'Consult doctor').

/* 281. Graves' Disease (duplicate entry) */
symptom(graves_disease_dup, [anxiety, irritability, tremor_of_hands, heat_sensitivity, weight_loss, enlarged_thyroid, bulging_eyes, fatigue, thick_red_skin_on_shins]).
treatment(graves_disease_dup, 'Consult doctor').

/* 282. Guillain-Barre Syndrome (duplicate entry) */
symptom(guillain_barre_syndrome_dup, [weakness_and_tingling_in_extremities, unsteady_walking, difficulty_with_facial_movements, double_vision, difficulty_speaking, difficulty_breathing, severe_pain]).
treatment(guillain_barre_syndrome_dup, 'Consult doctor').

/* 283. Gum Disease (Periodontitis) */
symptom(gum_disease, [swollen_puffy_gums, bright_red_or_dusky_red_gums, tender_gums, bleeding_gums, bad_breath, pus_between_teeth_and_gums, loose_teeth, painful_chewing]).
treatment(gum_disease, 'Consult doctor').

/* 284. Hemochromatosis (duplicate entry) */
symptom(hemochromatosis_dup, [joint_pain, fatigue, weakness, diabetes, loss_of_sex_drive, impotence, heart_failure, liver_failure, bronze_or_gray_skin_color]).
treatment(hemochromatosis_dup, 'Consult doctor').

/* 285. Hepatitis (A, B, C) */
symptom(hepatitis_abc, [fatigue, sudden_nausea_and_vomiting, abdominal_pain, clay_colored_bowel_movements, loss_of_appetite, low_grade_fever, dark_urine, joint_pain, jaundice]).
treatment(hepatitis_abc, 'Consult doctor').

/* 286. Hereditary Angioedema */
symptom(hereditary_angioedema, [swelling_of_hands_feet_face_airway_and_intestinal_tract, severe_abdominal_pain, vomiting, diarrhea, difficulty_breathing]).
treatment(hereditary_angioedema, 'Consult doctor').

/* 287. Hidradenitis Suppurativa */
symptom(hidradenitis_suppurativa, [blackheads, painful_lumps, connecting_tunnels_between_lumps]).
treatment(hidradenitis_suppurativa, 'Consult doctor').

/* 288. Hirschsprung's Disease */
symptom(hirschsprungs_disease, [failure_to_pass_stool_in_first_days, swollen_belly, vomiting, constipation_or_gas, diarrhea]).
treatment(hirschsprungs_disease, 'Consult doctor').

/* 289. Hyperemesis Gravidarum */
symptom(hyperemesis_gravidarum, [severe_nausea_and_vomiting, dehydration, electrolyte_imbalances, weight_loss, lightheadedness]).
treatment(hyperemesis_gravidarum, 'Consult doctor').

/* 290. Idiopathic Pulmonary Fibrosis */
symptom(idiopathic_pulmonary_fibrosis, [shortness_of_breath, chronic_dry_cough, fatigue, unexplained_weight_loss, aching_muscles_and_joints, clubbing_of_fingers]).
treatment(idiopathic_pulmonary_fibrosis, 'Consult doctor').

/* 291. Interstitial Cystitis (Painful Bladder Syndrome) */
symptom(interstitial_cystitis, [chronic_pelvic_pain, persistent_urge_to_urinate, frequent_urination, pain_during_intercourse]).
treatment(interstitial_cystitis, 'Consult doctor').

/* 292. Irritable Bowel Syndrome (IBS) (duplicate entry) */
symptom(ibs_dup, [abdominal_pain, cramping, bloating, gas, diarrhea, constipation, mucus_in_stool]).
treatment(ibs_dup, 'Consult doctor').

/* 293. Kawasaki Disease */
symptom(kawasaki_disease, [high_fever, rash, swollen_hands_and_feet, redness_in_eyes, swollen_lymph_nodes, inflammation_of_blood_vessels, irritability]).
treatment(kawasaki_disease, 'Consult doctor').

/* 294. Klinefelter Syndrome */
symptom(klinefelter_syndrome, [low_testosterone, reduced_muscle_mass, reduced_facial_and_body_hair, enlarged_breast_tissue, tall_stature, learning_disabilities, delayed_speech]).
treatment(klinefelter_syndrome, 'Consult doctor').

/* 295. Meniere's Disease */
symptom(menieres_disease, [vertigo, hearing_loss, tinnitus, feeling_of_fullness_in_ear]).
treatment(menieres_disease, 'Consult doctor').

/* 296. Mesenteric Ischemia */
symptom(mesenteric_ischemia, [severe_abdominal_pain, vomiting, diarrhea, fever, rapid_heartbeat, blood_in_stool]).
treatment(mesenteric_ischemia, 'Consult doctor').

/* 297. Myasthenia Gravis (duplicate entry) */
symptom(myasthenia_gravis_dup, [muscle_weakness, drooping_of_eyelids, double_vision, difficulty_swallowing, shortness_of_breath, altered_speech, facial_muscle_weakness]).
treatment(myasthenia_gravis_dup, 'Consult doctor').

/* 298. Myelodysplastic Syndromes (MDS) (duplicate entry) */
symptom(myelodysplastic_syndromes_dup, [fatigue, shortness_of_breath]).
treatment(myelodysplastic_syndromes_dup, 'Consult doctor').

/* --- End of Extension --- */
