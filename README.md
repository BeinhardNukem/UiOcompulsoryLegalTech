# UiOcompulsoryLegalTech

Legal Tech – Compulsory Exercise README.txt --------- WORDS: 300

I’m assuming that the Health Department is sending over personal data through a specified json.file – see testStructure.json. The program reads the personal data from the json.file and creates an unfiltered list of objects with all data from the json.file. 

The program iterates through all objects in the unfiltered list. First it checks if there is consent as GPPR art. 9 (2) states. If there is no consent, the program checks for exceptions. When calling the method, initially, the user either sends in None – if there is no exception precent- or a short/simple description of the exception in mind.

The description of exception should follow a simple standard set by an external API – AI that evaluates the exceptions in GDPR art. 9 (2) letter a – j. The logic behind this, is that the evaluation process of the personal data should be simplified for the AI be able to accurately handle the personal data and return accurate assessments based upon the objective data handled by our program.

If there are no exceptions, and still no registered consent from the patient, the program checks if the json.file contains registered ssn, biometric data or nationality (or any other relevant data) – as specified in GDPR art. 9 (1). In case of no exceptions or none of the variables mentioned above are present or if there is consent, the data is added to a filtered list that contains objects according to GDPR art. 9.

The checkData method then checks if the filtered list is empty, if it is, the method returns None. If the list is not empty, it is returned. 

I am not certain that the method of reading json.file works in practice, but it presents the logic behind how to gather data from the file.
