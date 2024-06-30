import csv

def generate_report():
    report = {}

    with open('exam_results.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            exam_name = row['Exam Name']
            score = int(row['Score'])
            grade = row['Grade']

            if exam_name not in report:
                report[exam_name] = {'candidates': 0, 'passed': 0, 'failed': 0, 'best_score': score, 'worst_score': score}

            report[exam_name]['candidates'] += 1
            if grade == 'Pass':
                report[exam_name]['passed'] += 1
            else:
                report[exam_name]['failed'] += 1

            if score > report[exam_name]['best_score']:
                report[exam_name]['best_score'] = score
            if score < report[exam_name]['worst_score']:
                report[exam_name]['worst_score'] = score

    with open('report.csv', 'w', newline='') as csvfile:
        fieldnames = ['Exam Name', 'Number of Candidates', 'Number of Passed Exams', 'Number of Failed Exams', 'Best Score', 'Worst Score']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        print(report)

        writer.writeheader()
        for exam_name, data in report.items():
            writer.writerow({
                'Exam Name': exam_name,
                'Number of Candidates': data['candidates'],
                'Number of Passed Exams': data['passed'],
                'Number of Failed Exams': data['failed'],
                'Best Score': data['best_score'],
                'Worst Score': data['worst_score']
            })
generate_report()