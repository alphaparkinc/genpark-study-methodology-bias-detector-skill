from client import StudyMethodologyBiasDetectorClient

def main():
    client = StudyMethodologyBiasDetectorClient()
    res = client.audit_methodology_bias()
    print('Methodology Bias Auditor: ' + res['bias_audit_id'] + ' (' + res['methodology_robustness_grade'] + ')')
    print('Design: ' + res['study_design'] + ' | Power: ' + str(res['statistical_power_score']))
    print('Dossier URL: ' + res['audit_dossier_url'])

if __name__ == '__main__':
    main()
