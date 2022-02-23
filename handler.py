resultsUnfiltered = []
resultsFiltered = []


def readJson(file):
    with open('input.json', 'r') as inp:
        for p in inp.individuals:
            resultsUnfiltered.append(Person(p.test-results.pcr-result, p.test-results.antibody-result,
                                     p.personal.nationality, p.personal.ssn, p.personal.biometric, p.personal.consent))


# Method run by calling handler.checkData(file.json, None/*simple description*)
def checkData(file, exception):
    readJson(file)
    for i in resultsUnfiltered:
        if not i.consent:
            if exception is not None:
                if checkException(exception):
                    resultsFiltered.append(i)
                return
            if i.ssn is not None or i.biometric is not None or i.nat is not None:
                return
        resultsFiltered.append(i)

    if len(resultsFiltered) is 0:
        return None

    return resultsFiltered


# Checks if exception is valid through an external AI-service via an API
def checkException(description):
    return API.exceptionAI(description)


class Person:
    def __init__(self, pcr, antibody, nat, ssn, biometric, consent):
        self.pcr = pcr
        self.antibody = antibody
        self.nat = nat
        self.ssn = ssn
        self.biometric = biometric
        self.consent = consent
