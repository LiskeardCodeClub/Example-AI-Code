from deepface import DeepFace

#Uses DeepFace to check whether it's the same person. 
samePerson = DeepFace.verify("ed.jpg", "ed2.jpg")

#analyses different aspects of age, gender, emotion and race of image subject and returns a dictionary of information
result = DeepFace.analyze(
    "me.jpg", 
    actions=["age", "gender", "emotion", "race"],
    detector_backend="retinaface",
    enforce_detection = True,
    silent=True
)
#variable called demography that shows result if it's a dictionary (single face), else if it's a list (multiple faces) returns the first element.
demography = result if isinstance(result, dict) else result[0]

#assigns the result from age, gender, emotion, race of scan to variable. 
age = demography["age"]
gender = demography["dominant_gender"] #dominant is most confident result. 
emotion = demography["dominant_emotion"]
race = demography["dominant_race"]

print("\n===== FACE ANALYSIS RESULTS =====")
print(f"Age:        {age}")
print(f"Gender:     {gender}")
print(f"Emotion:    {emotion}")
print(f"Race        {race}")
print("=================================\n")
print("Is verified:", samePerson["verified"])


#Has to be run in python 3.10 or 3.11